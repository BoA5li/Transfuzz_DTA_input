#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os
import re
import subprocess
from collections import defaultdict

HEX_PC_RE = re.compile(r"^0x[0-9a-fA-F]+$")
OBJDUMP_INST_RE = re.compile(r"^\s*([0-9a-fA-F]+):\s")
TOKEN_RE = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")
ANGLE_SYMBOL_RE = re.compile(r"<([^>]+)>")
REGISTER_TOKEN_RE = re.compile(r"\b(?:r(?:1[0-5]|[0-9]|ax|bx|cx|dx|si|di|bp|sp)|e(?:ax|bx|cx|dx|si|di|bp|sp)|[abcd][lh]|[cdefgs]s|[sd]il|bpl|spl|rip|xmm\d+|ymm\d+|zmm\d+)\b", re.IGNORECASE)

SCAFFOLD_TAGS = {
    "prologue",
    "epilogue",
    "stack_alignment",
    "argument_shuffle",
    "callee_save_spill",
    "callee_save_restore",
}

IMM_SEMANTIC_PRIORITY = [
    "rip_relative_displacement",
    "plt_got_offset",
    "stack_alignment_constant",
    "frame_offset_constant",
    "comparison_constant",
    "loop_bound_constant",
    "store_constant",
    "address_scale_constant",
]


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def safe_read_lines(path):
    if not path:
        return []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.readlines()


def normalize_pc(pc):
    if isinstance(pc, str) and HEX_PC_RE.match(pc):
        return pc.lower()
    return None


def sorted_pcs(pcs):
    return sorted({pc for pc in pcs if normalize_pc(pc)}, key=lambda x: int(x, 16))


def normalize_path(p):
    if not p:
        return None
    return os.path.abspath(p)


def parse_objdump_with_addresses(path):
    """
    解析 objdump -drwCS 输出。
    返回:
      asm_by_pc: {
        "0x801": {
          "line": "...",
          "index": 行号索引,
          "raw_pc": 0x801
        }
      }
      asm_lines: 全部汇编文本行
    """
    asm_lines = safe_read_lines(path)
    asm_by_pc = {}

    for idx, line in enumerate(asm_lines):
        m = OBJDUMP_INST_RE.match(line)
        if not m:
            continue
        pc_int = int(m.group(1), 16)
        pc = hex(pc_int)
        asm_by_pc[pc] = {
            "line": line.rstrip("\n"),
            "index": idx,
            "raw_pc": pc_int,
        }

    return asm_by_pc, asm_lines


def addr2line_lookup(binary, pcs):
    """
    使用 addr2line 将 PC 映射到 file:line。
    返回:
      {
        "0x801": {"file": "...", "line": 123, "function": "...", "raw": "..."}
      }
    """
    if not binary or not pcs:
        return {}

    uniq = sorted(set(pcs), key=lambda x: int(x, 16))
    results = {}

    for pc in uniq:
        try:
            out = subprocess.check_output(
                ["addr2line", "-e", binary, "-f", "-C", pc],
                stderr=subprocess.DEVNULL,
                text=True,
            ).splitlines()
            func = out[0].strip() if len(out) >= 1 else None
            loc = out[1].strip() if len(out) >= 2 else None

            file_part = None
            line_no = None
            if loc and loc != "??:0" and ":" in loc:
                parts = loc.rsplit(":", 1)
                file_part = parts[0]
                try:
                    line_no = int(parts[1])
                except ValueError:
                    line_no = None

            results[pc] = {
                "file": file_part,
                "line": line_no,
                "function": func,
                "raw": loc,
            }
        except Exception:
            results[pc] = {
                "file": None,
                "line": None,
                "function": None,
                "raw": None,
            }

    return results


def load_source_files(paths):
    source_files = {}
    for p in paths:
        if p and os.path.exists(p):
            source_files[os.path.abspath(p)] = safe_read_lines(p)
    return source_files


def get_source_snippet(source_files, file_path, line_no, context=2):
    """
    返回源码附近若干行。
    """
    if not file_path or not line_no:
        return []

    file_abs = normalize_path(file_path)
    lines = source_files.get(file_abs)
    if lines is None:
        for k, v in source_files.items():
            if os.path.basename(k) == os.path.basename(file_path):
                lines = v
                file_abs = k
                break

    if lines is None:
        return []

    start = max(1, line_no - context)
    end = min(len(lines), line_no + context)
    out = []
    for ln in range(start, end + 1):
        out.append({
            "line": ln,
            "text": lines[ln - 1].rstrip("\n")
        })
    return out


def get_asm_snippet(asm_lines, asm_by_pc, pc, context=2):
    ent = asm_by_pc.get(pc)
    if not ent:
        return []

    idx = ent["index"]
    start = max(0, idx - context)
    end = min(len(asm_lines), idx + context + 1)
    out = []
    for i in range(start, end):
        out.append({
            "index": i + 1,
            "text": asm_lines[i].rstrip("\n")
        })
    return out


def _collect_strings(value, out):
    if value is None:
        return
    if isinstance(value, str):
        if value:
            out.add(value)
        return
    if isinstance(value, (list, tuple, set)):
        for item in value:
            _collect_strings(item, out)
        return
    if isinstance(value, dict):
        for item in value.values():
            _collect_strings(item, out)


def get_object_semantic_tags(node_detail):
    tags = set()
    for key in (
        "semantic_tag",
        "semantic_tags",
        "semantic_role",
        "semantic_roles",
        "role_tags",
        "roles",
        "subtype",
        "source_role",
        "source_roles",
        "instruction_region_tags",
        "structural_tags",
    ):
        _collect_strings(node_detail.get(key), tags)
    return sorted(tags)


def get_instruction_semantic_tags(inst_detail):
    tags = set()
    for key in (
        "semantic_tag",
        "semantic_tags",
        "instruction_tags",
        "abi_tags",
        "structural_tags",
        "role_tags",
        "tags",
    ):
        _collect_strings(inst_detail.get(key), tags)
    return sorted(tags)


def parse_occurrence_from_label(label):
    if not isinstance(label, str):
        return {}
    m = re.match(r"^(?:imm@|imm_occurrence:)(0x[0-9a-fA-F]+|[0-9]+)(?::(\d+))?:(.+)$", label)
    if not m:
        return {}

    pc_raw = m.group(1)
    operand_index = m.group(2)
    remainder = m.group(3)

    occ = {
        "occurrence_pc": pc_raw if pc_raw.startswith("0x") else hex(int(pc_raw)),
        "operand_index": int(operand_index) if operand_index is not None else None,
        "raw_suffix": remainder,
    }
    return occ


def analyze_call_target(disasm, asm_line):
    if not disasm:
        return None

    parts = disasm.strip().split(None, 1)
    if not parts or parts[0].lower() != "call":
        return None

    operand = parts[1].strip() if len(parts) > 1 else ""
    asm_text = asm_line or disasm
    symbols = ANGLE_SYMBOL_RE.findall(asm_text)
    resolved_symbol = symbols[-1] if symbols else None
    operand_lower = operand.lower()

    result = {
        "operand": operand,
        "resolved_symbol": resolved_symbol,
        "call_kind": None,
        "display_target": resolved_symbol or operand,
    }

    if resolved_symbol and "@plt" in resolved_symbol:
        result["call_kind"] = "plt_got_thunk"
        return result

    is_indirect = (
        operand.startswith("*")
        or "ptr" in operand_lower
        or "(" in operand
        or ")" in operand
        or "[" in operand
        or "]" in operand
    )

    if not is_indirect and resolved_symbol:
        result["call_kind"] = "direct_call_symbol"
        return result

    if not is_indirect and operand:
        result["call_kind"] = "direct_call_symbol"
        return result

    if REGISTER_TOKEN_RE.search(operand) and not any(ch in operand for ch in "([") and "ptr" not in operand_lower:
        result["call_kind"] = "indirect_call_through_register"
        return result

    if resolved_symbol and ("@got" in resolved_symbol.lower() or "got" in operand_lower or "ptr" in operand_lower or "(" in operand or "[" in operand):
        result["call_kind"] = "indirect_call_through_memory"
        return result

    if resolved_symbol:
        result["call_kind"] = "indirect_call_through_memory"
        return result

    result["call_kind"] = "unresolved_indirect_target"
    return result


def scan_instruction_direct_pcs(node_id, instruction_details):
    rel = {
        "direct_use_pcs": set(),
        "direct_def_pcs": set(),
        "direct_addr_pcs": set(),
        "direct_imm_pcs": set(),
    }

    for pc, inst in instruction_details.items():
        norm_pc = normalize_pc(pc)
        if not norm_pc:
            continue
        if node_id in inst.get("use_objects", []):
            rel["direct_use_pcs"].add(norm_pc)
        if node_id in inst.get("def_objects", []):
            rel["direct_def_pcs"].add(norm_pc)
        if node_id in inst.get("addr_objects", []):
            rel["direct_addr_pcs"].add(norm_pc)
        if node_id in inst.get("immediates", []):
            rel["direct_imm_pcs"].add(norm_pc)

    return rel


def collect_path_related_pcs(node_id, path_report):
    related = set()
    relation_sources = defaultdict(set)

    if not path_report:
        return related, relation_sources

    for section in ("backward_paths", "forward_paths"):
        section_kind = "path_backward_related" if section == "backward_paths" else "path_forward_related"
        for target_block in path_report.get(section, []):
            for path in target_block.get("paths", []):
                for step in path.get("steps", []):
                    if step.get("src") != node_id and step.get("dst") != node_id:
                        continue
                    for pc in step.get("pcs", []):
                        norm_pc = normalize_pc(pc)
                        if norm_pc:
                            related.add(norm_pc)
                            relation_sources[norm_pc].add(section_kind)

    return related, relation_sources


def parse_pcs_from_asm_context(snippet):
    pcs = set()
    for item in snippet or []:
        text = item.get("text", "")
        m = OBJDUMP_INST_RE.match(text)
        if not m:
            continue
        pcs.add(hex(int(m.group(1), 16)).lower())
    return pcs


def _new_relation_record():
    return {
        "relation_kinds": set(),
        "relation_groups": set(),
        "sources": set(),
    }


def add_pc_relation(relation_map, pc, relation_kind, relation_group, source):
    norm_pc = normalize_pc(pc)
    if not norm_pc:
        return
    rec = relation_map[norm_pc]
    rec["relation_kinds"].add(relation_kind)
    rec["relation_groups"].add(relation_group)
    rec["sources"].add(source)


def build_pc_relation_layers(node_id, node_detail, instruction_details, path_report, asm_by_pc, asm_lines, asm_context=2):
    scanned = scan_instruction_direct_pcs(node_id, instruction_details)

    direct_use_pcs = set(normalize_pc(pc) for pc in node_detail.get("used_by", [])) | scanned["direct_use_pcs"]
    direct_use_pcs = {pc for pc in direct_use_pcs if pc}

    direct_def_pcs = set(normalize_pc(pc) for pc in node_detail.get("defined_by", [])) | scanned["direct_def_pcs"]
    direct_def_pcs = {pc for pc in direct_def_pcs if pc}

    direct_addr_pcs = set(normalize_pc(pc) for pc in node_detail.get("addr_used_by", [])) | scanned["direct_addr_pcs"]
    direct_addr_pcs = {pc for pc in direct_addr_pcs if pc}

    direct_ctrl_pcs = set(normalize_pc(pc) for pc in node_detail.get("ctrl_used_by", []))
    direct_ctrl_pcs = {pc for pc in direct_ctrl_pcs if pc}

    direct_imm_pcs = scanned["direct_imm_pcs"]

    path_related_pcs, path_relation_sources = collect_path_related_pcs(node_id, path_report)

    direct_operand_pcs = set(direct_use_pcs) | set(direct_imm_pcs)
    structural_role_pcs = set(direct_def_pcs) | set(direct_addr_pcs) | set(direct_ctrl_pcs)
    anchor_pcs = set(direct_operand_pcs) | set(structural_role_pcs)
    derived_or_related_pcs = set(path_related_pcs) - set(anchor_pcs)

    evidence_pcs = set()
    for pc in anchor_pcs | derived_or_related_pcs:
        context_pcs = parse_pcs_from_asm_context(get_asm_snippet(asm_lines, asm_by_pc, pc, context=asm_context))
        evidence_pcs.update(context_pcs)
    evidence_pcs -= anchor_pcs
    evidence_pcs -= derived_or_related_pcs

    relation_map = defaultdict(_new_relation_record)

    for pc in direct_use_pcs:
        add_pc_relation(relation_map, pc, "direct_use", "direct_operand", "object_detail.used_by/instruction_details.use_objects")
    for pc in direct_imm_pcs:
        add_pc_relation(relation_map, pc, "direct_immediate_occurrence", "direct_operand", "instruction_details.immediates")
    for pc in direct_def_pcs:
        add_pc_relation(relation_map, pc, "store_target", "structural_role", "object_detail.defined_by/instruction_details.def_objects")
    for pc in direct_addr_pcs:
        add_pc_relation(relation_map, pc, "address_component", "structural_role", "object_detail.addr_used_by/instruction_details.addr_objects")
    for pc in direct_ctrl_pcs:
        add_pc_relation(relation_map, pc, "branch_condition", "structural_role", "object_detail.ctrl_used_by")
    for pc in derived_or_related_pcs:
        kinds = sorted(path_relation_sources.get(pc) or {"propagated_related"})
        for kind in kinds:
            add_pc_relation(relation_map, pc, kind, "derived_or_related", "path_report")
    for pc in evidence_pcs:
        add_pc_relation(relation_map, pc, "evidence_only", "evidence_only", "asm_context")

    direct_use_pcs = sorted_pcs(direct_use_pcs)
    direct_def_pcs = sorted_pcs(direct_def_pcs)
    direct_addr_pcs = sorted_pcs(direct_addr_pcs)
    direct_ctrl_pcs = sorted_pcs(direct_ctrl_pcs)
    direct_imm_pcs = sorted_pcs(direct_imm_pcs)
    direct_operand_pcs = sorted_pcs(direct_operand_pcs)
    structural_role_pcs = sorted_pcs(structural_role_pcs)
    anchor_pcs = sorted_pcs(anchor_pcs)
    derived_or_related_pcs = sorted_pcs(derived_or_related_pcs)
    evidence_pcs = sorted_pcs(evidence_pcs)
    all_mapped_pcs = sorted_pcs(set(anchor_pcs) | set(derived_or_related_pcs) | set(evidence_pcs))

    group_order = {
        "direct_operand": 0,
        "structural_role": 1,
        "derived_or_related": 2,
        "evidence_only": 3,
    }

    pc_relation_entries = []
    for pc in all_mapped_pcs:
        rec = relation_map.get(pc, _new_relation_record())
        relation_groups = sorted(rec["relation_groups"], key=lambda x: (group_order.get(x, 99), x))
        primary_group = relation_groups[0] if relation_groups else None
        pc_relation_entries.append({
            "pc": pc,
            "relation_kinds": sorted(rec["relation_kinds"]),
            "relation_groups": relation_groups,
            "primary_relation_group": primary_group,
            "sources": sorted(rec["sources"]),
        })

    relation_index = {item["pc"]: item for item in pc_relation_entries}

    return {
        "direct_use_pcs": direct_use_pcs,
        "direct_def_pcs": direct_def_pcs,
        "direct_addr_pcs": direct_addr_pcs,
        "direct_ctrl_pcs": direct_ctrl_pcs,
        "direct_imm_pcs": direct_imm_pcs,
        "direct_operand_pcs": direct_operand_pcs,
        "structural_role_pcs": structural_role_pcs,
        "anchor_pcs": anchor_pcs,
        "derived_or_related_pcs": derived_or_related_pcs,
        "evidence_pcs": evidence_pcs,
        "all_mapped_pcs": all_mapped_pcs,
        "pc_relation_entries": pc_relation_entries,
        "relation_index": relation_index,
    }


def build_instruction_evidence(pcs, instruction_details, asm_by_pc, asm_lines, addr2line_info, relation_index=None):
    evidence = []

    for pc in sorted_pcs(pcs):
        inst = instruction_details.get(pc, {})
        a2l = addr2line_info.get(pc, {})
        asm_line = asm_by_pc.get(pc, {}).get("line")
        semantic_tags = get_instruction_semantic_tags(inst)
        relation = (relation_index or {}).get(pc, {})

        evidence.append({
            "pc": pc,
            "relation_kinds": relation.get("relation_kinds", []),
            "relation_groups": relation.get("relation_groups", []),
            "primary_relation_group": relation.get("primary_relation_group"),
            "relation_sources": relation.get("sources", []),
            "disasm": inst.get("disasm"),
            "use_objects": inst.get("use_objects", []),
            "def_objects": inst.get("def_objects", []),
            "addr_objects": inst.get("addr_objects", []),
            "immediates": inst.get("immediates", []),
            "controlled_by": inst.get("controlled_by", []),
            "uses_taint": inst.get("uses_taint"),
            "suppressed_repeat_records": inst.get("suppressed_repeat_records"),
            "instruction_semantic_tags": semantic_tags,
            "call_target": analyze_call_target(inst.get("disasm"), asm_line),
            "addr2line": {
                "file": a2l.get("file"),
                "line": a2l.get("line"),
                "function": a2l.get("function"),
                "raw": a2l.get("raw"),
            },
            "asm_line": asm_line,
            "asm_context": get_asm_snippet(asm_lines, asm_by_pc, pc, context=2),
        })

    return evidence


def build_source_evidence(pcs, addr2line_info, source_files, relation_index=None):
    refs = {}

    for pc in sorted_pcs(pcs):
        a2l = addr2line_info.get(pc, {})
        src_file = a2l.get("file")
        src_line = a2l.get("line")
        if not src_file or not src_line:
            continue

        key = (src_file, src_line)
        ref = refs.get(key)
        if ref is None:
            ref = {
                "file": src_file,
                "line": src_line,
                "function": a2l.get("function"),
                "snippet": get_source_snippet(source_files, src_file, src_line, context=2),
                "pcs": set(),
                "relation_kinds": set(),
                "relation_groups": set(),
            }
            refs[key] = ref

        ref["pcs"].add(pc)
        rel = (relation_index or {}).get(pc, {})
        ref["relation_kinds"].update(rel.get("relation_kinds", []))
        ref["relation_groups"].update(rel.get("relation_groups", []))

    out = []
    for key in sorted(refs.keys(), key=lambda x: (x[0], x[1])):
        ref = refs[key]
        out.append({
            "file": ref["file"],
            "line": ref["line"],
            "function": ref["function"],
            "snippet": ref["snippet"],
            "pcs": sorted_pcs(ref["pcs"]),
            "relation_kinds": sorted(ref["relation_kinds"]),
            "relation_groups": sorted(ref["relation_groups"]),
        })
    return out


def build_asm_references(pcs, asm_by_pc, relation_index=None):
    out = []
    seen = set()
    for pc in sorted_pcs(pcs):
        if pc in seen:
            continue
        asm_line = asm_by_pc.get(pc, {}).get("line")
        if not asm_line:
            continue
        rel = (relation_index or {}).get(pc, {})
        out.append({
            "pc": pc,
            "asm_line": asm_line,
            "relation_kinds": rel.get("relation_kinds", []),
            "relation_groups": rel.get("relation_groups", []),
            "primary_relation_group": rel.get("primary_relation_group"),
        })
        seen.add(pc)
    return out


def extract_source_texts(source_evidence):
    texts = []
    for item in source_evidence:
        for line in item.get("snippet", []):
            texts.append(line["text"])
    return texts


def infer_object_mapping(node_id, node_detail, related_source_lines, anchor_instruction_tags=None):
    """
    给出对象与程序元素的解释。
    """
    typ = node_detail.get("type")
    label = node_detail.get("label", "")
    object_semantic_tags = get_object_semantic_tags(node_detail)
    anchor_instruction_tags = sorted(set(anchor_instruction_tags or []))
    combined_tags = set(object_semantic_tags) | set(anchor_instruction_tags)
    scaffold_tags = sorted(combined_tags & SCAFFOLD_TAGS)

    result = {
        "object_kind": typ,
        "label": label,
        "mapping_kind": None,
        "confidence": None,
        "candidate_program_elements": [],
        "reason": "",
        "object_semantic_tags": object_semantic_tags,
        "anchor_instruction_tags": anchor_instruction_tags,
        "scaffolding_tags": scaffold_tags,
        "occurrence": parse_occurrence_from_label(label),
    }

    def with_scaffold_reason(base_reason):
        if not scaffold_tags:
            return base_reason
        return base_reason + " 检测到 ABI/脚手架标签：" + ", ".join(scaffold_tags) + "，应更偏向解释为结构性对象，而非优先可变异语义对象。"

    if typ == "var":
        result["mapping_kind"] = "global_or_static_variable"
        result["confidence"] = "exact"
        result["candidate_program_elements"] = [label]
        result["reason"] = with_scaffold_reason("对象类型为 var，通常直接对应全局/静态对象。")
        return result

    if typ == "imm":
        for tag in IMM_SEMANTIC_PRIORITY:
            if tag in combined_tags:
                result["mapping_kind"] = tag
                result["confidence"] = "semantic"
                result["candidate_program_elements"] = [label]
                reasons = {
                    "comparison_constant": "该 immediate 带有 comparison_constant 标签，更适合作为比较语义常量解释。",
                    "store_constant": "该 immediate 带有 store_constant 标签，更适合作为写入值常量解释。",
                    "loop_bound_constant": "该 immediate 带有 loop_bound_constant 标签，更适合作为循环边界或步长常量解释。",
                    "stack_alignment_constant": "该 immediate 带有 stack_alignment_constant 标签，更适合作为栈对齐常量解释。",
                    "rip_relative_displacement": "该 immediate 带有 rip_relative_displacement 标签，更适合作为 RIP 相对寻址位移解释。",
                    "plt_got_offset": "该 immediate 带有 plt_got_offset 标签，更适合作为 PLT/GOT 相关位移解释。",
                    "frame_offset_constant": "该 immediate 带有 frame_offset_constant 标签，更适合作为栈帧偏移常量解释。",
                    "address_scale_constant": "该 immediate 带有 address_scale_constant 标签，更适合作为地址 scale 常量解释。",
                }
                result["reason"] = with_scaffold_reason(reasons.get(tag, "该 immediate 具有明确语义标签。"))
                return result

        result["mapping_kind"] = "constant_or_address_component"
        result["confidence"] = "structural"
        result["candidate_program_elements"] = [label]
        result["reason"] = with_scaffold_reason("对象类型为 imm，更适合作为常量、位移、scale、比较值或地址组成部分解释。")
        return result

    if typ == "reg":
        if "controlling_operand" in combined_tags:
            result["mapping_kind"] = "control_register"
            result["confidence"] = "semantic"
            result["candidate_program_elements"] = [label]
            result["reason"] = with_scaffold_reason("寄存器带有 controlling_operand 标签，更适合作为分支/控制条件寄存器解释。")
            return result
        if "address_base" in combined_tags or "address_index" in combined_tags:
            result["mapping_kind"] = "address_computation_register"
            result["confidence"] = "semantic"
            result["candidate_program_elements"] = [label]
            result["reason"] = with_scaffold_reason("寄存器带有 address_base/address_index 标签，更适合作为地址计算寄存器解释。")
            return result
        if "transient_move_only_carrier" in combined_tags:
            result["mapping_kind"] = "transient_value_carrier"
            result["confidence"] = "semantic"
            result["candidate_program_elements"] = [label]
            result["reason"] = with_scaffold_reason("寄存器带有 transient_move_only_carrier 标签，更像纯搬运载体寄存器。")
            return result
        if "carrier" in combined_tags:
            result["mapping_kind"] = "execution_register_carrier"
            result["confidence"] = "semantic"
            result["candidate_program_elements"] = [label]
            result["reason"] = with_scaffold_reason("寄存器带有 carrier 标签，表示执行时承载值的寄存器。")
            return result

        result["mapping_kind"] = "execution_register_carrier"
        result["confidence"] = "structural"
        result["candidate_program_elements"] = [label]
        result["reason"] = with_scaffold_reason("对象类型为 reg，表示执行时承载值的寄存器，而不是稳定的 C 变量名。")
        return result

    if typ == "stack":
        if scaffold_tags:
            result["mapping_kind"] = "stack_slot_scaffold_or_spill"
            result["confidence"] = "semantic"
            result["candidate_program_elements"] = [label]
            result["reason"] = with_scaffold_reason("对象类型为 stack，且关联到脚手架标签，通常对应形参搬运、callee-save spill/restore 或对齐槽位。")
            return result
        result["mapping_kind"] = "stack_slot_local_or_spill"
        result["confidence"] = "probable"
        result["candidate_program_elements"] = [label]
        result["reason"] = "对象类型为 stack，通常对应局部变量、形参栈槽或编译器 spill 槽位。"
        return result

    if typ == "mem":
        if "plt_got_offset" in combined_tags:
            result["mapping_kind"] = "plt_or_got_memory_slot"
            result["confidence"] = "semantic"
            result["candidate_program_elements"] = [label]
            result["reason"] = with_scaffold_reason("对象类型为 mem，且带有 plt_got_offset 相关标签，更适合作为 GOT/PLT 或外部调用相关内存槽解释。")
            return result
        result["mapping_kind"] = "runtime_memory_object"
        result["confidence"] = "probable"
        result["candidate_program_elements"] = [label]
        result["reason"] = with_scaffold_reason("对象类型为 mem，通常对应运行时指针解引用到的内存对象。")
        return result

    tokens = set()
    for s in related_source_lines:
        for t in TOKEN_RE.findall(s):
            tokens.add(t)

    result["mapping_kind"] = "unknown"
    result["confidence"] = "weak"
    result["candidate_program_elements"] = sorted(tokens)[:10]
    result["reason"] = with_scaffold_reason("未能仅凭对象类型稳定判断，只保留源码上下文中的候选标识符。")
    return result


def build_terminal_mapping(summary, path_report, asm_by_pc, asm_lines, addr2line_info, source_files):
    instruction_details = summary.get("instruction_details", {})
    object_details = summary.get("object_details", {})

    backward_leafs = summary.get("backward", {}).get("leaf_objects", [])
    forward_sinks = summary.get("forward", {}).get("sink_objects", [])

    report = {
        "meta": {
            "taint_source": summary.get("taint_source", {}),
            "stats": summary.get("stats", {}),
            "notes": [
                "映射以 PC/汇编为主锚点，再回映到 C 源码。",
                "object-PC 关系被显式分层为 direct_operand / structural_role / derived_or_related / evidence_only。",
                "source_evidence 与 instruction_evidence 已分层；源码片段不应被直接当成可变异锚点。",
                "var 通常可精确对应；stack/mem/reg/imm 更多是结构性或概率性对应。",
                "局部变量名的精确恢复通常依赖 DWARF 变量位置信息；本脚本默认只做源码行级与结构级映射。"
            ],
        },
        "backward_leaf_mappings": [],
        "forward_sink_mappings": [],
    }

    def make_entry(node_id, direction):
        detail = dict(object_details.get(node_id, {}))
        detail["_node_id"] = node_id

        pc_layers = build_pc_relation_layers(
            node_id=node_id,
            node_detail=detail,
            instruction_details=instruction_details,
            path_report=path_report,
            asm_by_pc=asm_by_pc,
            asm_lines=asm_lines,
        )
        relation_index = pc_layers["relation_index"]

        anchor_instruction_evidence = build_instruction_evidence(
            pc_layers["anchor_pcs"],
            instruction_details,
            asm_by_pc,
            asm_lines,
            addr2line_info,
            relation_index=relation_index,
        )
        related_instruction_evidence = build_instruction_evidence(
            pc_layers["derived_or_related_pcs"],
            instruction_details,
            asm_by_pc,
            asm_lines,
            addr2line_info,
            relation_index=relation_index,
        )
        evidence_only_instruction_evidence = build_instruction_evidence(
            pc_layers["evidence_pcs"],
            instruction_details,
            asm_by_pc,
            asm_lines,
            addr2line_info,
            relation_index=relation_index,
        )

        source_evidence = build_source_evidence(
            pc_layers["all_mapped_pcs"],
            addr2line_info,
            source_files,
            relation_index=relation_index,
        )
        source_texts = extract_source_texts(source_evidence)

        anchor_instruction_tags = set()
        for item in anchor_instruction_evidence:
            anchor_instruction_tags.update(item.get("instruction_semantic_tags", []))

        inferred = infer_object_mapping(
            node_id=node_id,
            node_detail=detail,
            related_source_lines=source_texts,
            anchor_instruction_tags=sorted(anchor_instruction_tags),
        )

        asm_refs = build_asm_references(
            pc_layers["all_mapped_pcs"],
            asm_by_pc,
            relation_index=relation_index,
        )

        return {
            "node_id": node_id,
            "direction_role": direction,
            "object_type": detail.get("type"),
            "object_label": detail.get("label"),
            "defined_by": detail.get("defined_by", []),
            "used_by": detail.get("used_by", []),
            "addr_used_by": detail.get("addr_used_by", []),
            "ctrl_used_by": detail.get("ctrl_used_by", []),
            "direct_parents": detail.get("direct_parents", []),
            "direct_children": detail.get("direct_children", []),
            "incoming_provenance_total": detail.get("incoming_provenance_total"),
            "outgoing_provenance_total": detail.get("outgoing_provenance_total"),
            "mapping_inference": inferred,
            "pc_relation_layers": {
                "direct_use_pcs": pc_layers["direct_use_pcs"],
                "direct_def_pcs": pc_layers["direct_def_pcs"],
                "direct_addr_pcs": pc_layers["direct_addr_pcs"],
                "direct_ctrl_pcs": pc_layers["direct_ctrl_pcs"],
                "direct_imm_pcs": pc_layers["direct_imm_pcs"],
                "direct_operand_pcs": pc_layers["direct_operand_pcs"],
                "structural_role_pcs": pc_layers["structural_role_pcs"],
                "anchor_pcs": pc_layers["anchor_pcs"],
                "derived_or_related_pcs": pc_layers["derived_or_related_pcs"],
                "evidence_pcs": pc_layers["evidence_pcs"],
                "all_mapped_pcs": pc_layers["all_mapped_pcs"],
            },
            "pc_relation_entries": pc_layers["pc_relation_entries"],
            "executed_code_reference": {
                "asm_references": asm_refs,
                "source_evidence": source_evidence,
                "direct_anchor_instruction_evidence": anchor_instruction_evidence,
                "related_instruction_evidence": related_instruction_evidence,
                "evidence_only_instruction_evidence": evidence_only_instruction_evidence,
            },
        }

    for node_id in backward_leafs:
        if node_id in object_details:
            report["backward_leaf_mappings"].append(make_entry(node_id, "backward_leaf"))

    for node_id in forward_sinks:
        if node_id in object_details:
            report["forward_sink_mappings"].append(make_entry(node_id, "forward_sink"))

    return report


def write_json(obj, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)


def render_snippet(snippet):
    return "\n".join(f"{x['line']:>5}: {x['text']}" for x in snippet)


def write_markdown(report, path, max_items_per_section=None):
    with open(path, "w", encoding="utf-8") as f:
        meta = report["meta"]
        f.write("# Terminal Object Mapping Report\n\n")
        f.write("## Meta\n\n")
        f.write(f"- Taint source: `{meta['taint_source'].get('symbol')}`\n")
        f.write(f"- Executed instructions: `{meta['stats'].get('executed_instructions')}`\n")
        f.write(f"- Backward objects: `{meta['stats'].get('backward_object_nodes')}`\n")
        f.write(f"- Forward objects: `{meta['stats'].get('forward_object_nodes')}`\n\n")

        def dump_section(title, items):
            f.write(f"## {title}\n\n")
            dump_items = items
            if max_items_per_section is not None:
                dump_items = dump_items[:max_items_per_section]

            for idx, item in enumerate(dump_items, 1):
                inf = item["mapping_inference"]
                layers = item["pc_relation_layers"]
                f.write(f"### {idx}. `{item['node_id']}`\n\n")
                f.write(f"- Role: `{item['direction_role']}`\n")
                f.write(f"- Type: `{item['object_type']}`\n")
                f.write(f"- Label: `{item['object_label']}`\n")
                f.write(f"- Mapping kind: `{inf['mapping_kind']}`\n")
                f.write(f"- Confidence: `{inf['confidence']}`\n")
                f.write(f"- Object semantic tags: `{inf.get('object_semantic_tags', [])}`\n")
                f.write(f"- Anchor instruction tags: `{inf.get('anchor_instruction_tags', [])}`\n")
                f.write(f"- Scaffolding tags: `{inf.get('scaffolding_tags', [])}`\n")
                if inf.get("occurrence"):
                    f.write(f"- Occurrence: `{inf['occurrence']}`\n")
                f.write(f"- Reason: {inf['reason']}\n")
                f.write(f"- Candidate program elements: `{inf['candidate_program_elements']}`\n")
                f.write(f"- direct_use_pcs: `{layers['direct_use_pcs']}`\n")
                f.write(f"- direct_def_pcs: `{layers['direct_def_pcs']}`\n")
                f.write(f"- direct_addr_pcs: `{layers['direct_addr_pcs']}`\n")
                f.write(f"- direct_ctrl_pcs: `{layers['direct_ctrl_pcs']}`\n")
                f.write(f"- direct_imm_pcs: `{layers['direct_imm_pcs']}`\n")
                f.write(f"- direct_operand_pcs: `{layers['direct_operand_pcs']}`\n")
                f.write(f"- structural_role_pcs: `{layers['structural_role_pcs']}`\n")
                f.write(f"- anchor_pcs: `{layers['anchor_pcs']}`\n")
                f.write(f"- derived_or_related_pcs: `{layers['derived_or_related_pcs']}`\n")
                f.write(f"- evidence_pcs: `{layers['evidence_pcs']}`\n")
                f.write(f"- all_mapped_pcs: `{layers['all_mapped_pcs']}`\n")
                f.write(f"- direct_parents: `{item['direct_parents']}`\n")
                f.write(f"- direct_children: `{item['direct_children']}`\n\n")

                f.write("#### PC Relation Entries\n\n")
                if not item["pc_relation_entries"]:
                    f.write("_No PC relation entries._\n\n")
                else:
                    for rel in item["pc_relation_entries"]:
                        f.write(
                            f"- `{rel['pc']}` kinds=`{rel['relation_kinds']}` groups=`{rel['relation_groups']}` "
                            f"primary_group=`{rel.get('primary_relation_group')}` sources=`{rel['sources']}`\n"
                        )
                    f.write("\n")

                f.write("#### Direct Anchor Instruction Evidence\n\n")
                evs = item["executed_code_reference"]["direct_anchor_instruction_evidence"]
                if not evs:
                    f.write("_No direct anchor instruction evidence._\n\n")
                else:
                    for ev in evs:
                        f.write(
                            f"- PC `{ev['pc']}`: `{ev.get('disasm')}` "
                            f"groups=`{ev.get('relation_groups')}` kinds=`{ev.get('relation_kinds')}`\n"
                        )
                        a2l = ev.get("addr2line", {})
                        if a2l.get("file"):
                            f.write(f"  - Source: `{a2l['file']}:{a2l['line']}` function=`{a2l.get('function')}`\n")
                        if ev.get("instruction_semantic_tags"):
                            f.write(f"  - instruction_semantic_tags: `{ev['instruction_semantic_tags']}`\n")
                        if ev.get("call_target"):
                            f.write(f"  - call_target: `{ev['call_target']}`\n")
                        if ev.get("use_objects"):
                            f.write(f"  - use_objects: `{ev['use_objects']}`\n")
                        if ev.get("def_objects"):
                            f.write(f"  - def_objects: `{ev['def_objects']}`\n")
                        if ev.get("addr_objects"):
                            f.write(f"  - addr_objects: `{ev['addr_objects']}`\n")
                        if ev.get("immediates"):
                            f.write(f"  - immediates: `{ev['immediates']}`\n")
                    f.write("\n")

                f.write("#### Related Instruction Evidence\n\n")
                evs = item["executed_code_reference"]["related_instruction_evidence"]
                if not evs:
                    f.write("_No related instruction evidence._\n\n")
                else:
                    for ev in evs:
                        f.write(
                            f"- PC `{ev['pc']}`: `{ev.get('disasm')}` "
                            f"groups=`{ev.get('relation_groups')}` kinds=`{ev.get('relation_kinds')}`\n"
                        )
                    f.write("\n")

                f.write("#### Evidence-only Instruction Evidence\n\n")
                evs = item["executed_code_reference"]["evidence_only_instruction_evidence"]
                if not evs:
                    f.write("_No evidence-only instruction evidence._\n\n")
                else:
                    for ev in evs:
                        f.write(
                            f"- PC `{ev['pc']}`: `{ev.get('disasm')}` "
                            f"groups=`{ev.get('relation_groups')}` kinds=`{ev.get('relation_kinds')}`\n"
                        )
                    f.write("\n")

                f.write("#### Assembly References\n\n")
                asm_refs = item["executed_code_reference"]["asm_references"]
                if not asm_refs:
                    f.write("_No assembly reference found._\n\n")
                else:
                    for a in asm_refs:
                        f.write(
                            f"- `{a['pc']}` {a['asm_line']} "
                            f"groups=`{a['relation_groups']}` kinds=`{a['relation_kinds']}`\n"
                        )
                    f.write("\n")

                f.write("#### Source Evidence\n\n")
                c_refs = item["executed_code_reference"]["source_evidence"]
                if not c_refs:
                    f.write("_No source evidence found._\n\n")
                else:
                    for c in c_refs:
                        f.write(
                            f"- `{c['file']}:{c['line']}` function=`{c.get('function')}` "
                            f"pcs=`{c.get('pcs')}` groups=`{c.get('relation_groups')}` kinds=`{c.get('relation_kinds')}`\n\n"
                        )
                        if c["snippet"]:
                            f.write("```c\n")
                            f.write(render_snippet(c["snippet"]))
                            f.write("\n```\n\n")

        dump_section("Backward Leaf Mappings", report["backward_leaf_mappings"])
        dump_section("Forward Sink Mappings", report["forward_sink_mappings"])


def main():
    ap = argparse.ArgumentParser(description="Map backward leaf / forward sink objects to asm and C source evidence.")
    ap.add_argument("--summary", required=True, help="dependency_summary.json")
    ap.add_argument("--path-report", default=None, help="path_report.json")
    ap.add_argument("--asm", required=True, help="objdump -drwCS output with addresses")
    ap.add_argument("--binary", default=None, help="binary for addr2line")
    ap.add_argument("--source", action="append", default=[], help="C source file(s), can be repeated")
    ap.add_argument("--out-json", default="terminal_node_mapping.json")
    ap.add_argument("--out-md", default="terminal_node_mapping.md")
    ap.add_argument("--max-md-items", type=int, default=None, help="limit markdown output count per section")
    args = ap.parse_args()

    summary = load_json(args.summary)
    path_report = load_json(args.path_report) if args.path_report else None
    asm_by_pc, asm_lines = parse_objdump_with_addresses(args.asm)

    all_pcs = list(summary.get("instruction_details", {}).keys())
    addr2line_info = addr2line_lookup(args.binary, all_pcs) if args.binary else {}

    source_files = load_source_files(args.source)

    report = build_terminal_mapping(
        summary=summary,
        path_report=path_report,
        asm_by_pc=asm_by_pc,
        asm_lines=asm_lines,
        addr2line_info=addr2line_info,
        source_files=source_files,
    )

    write_json(report, args.out_json)
    write_markdown(report, args.out_md, args.max_md_items)

    print("[+] Wrote JSON:", args.out_json)
    print("[+] Wrote Markdown:", args.out_md)


if __name__ == "__main__":
    main()
