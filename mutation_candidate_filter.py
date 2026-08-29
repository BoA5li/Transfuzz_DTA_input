#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Filter backward leaf dependency items and map them to user-code anchors.

This module deliberately does not rank candidates or recommend mutation
operators.  Leaf identity and dependency semantics are authoritative upstream
facts from dependency_summary.json.  The filter only removes unsupported,
unstable, runtime/ABI-structural items and preserves direct mapping evidence.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple


def norm_hex(value: Any) -> str:
    if isinstance(value, int):
        return hex(value)
    text = str(value).strip().lower()
    if text.startswith("0x"):
        try:
            return hex(int(text, 16))
        except ValueError:
            return text
    return text


def safe_list(value: Any) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (set, tuple)):
        return list(value)
    return [value]


def stable_pc_key(pc: str) -> Tuple[int, Any]:
    try:
        return (0, int(norm_hex(pc), 16))
    except (TypeError, ValueError):
        return (1, str(pc))


def is_valid_pc(value: Any) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return value >= 0
    text = str(value).strip().lower()
    return bool(re.fullmatch(r"0x[0-9a-f]+", text))


def sorted_pcs(values: Iterable[str]) -> List[str]:
    return sorted({norm_hex(v) for v in values if v is not None}, key=stable_pc_key)


def dump_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False), encoding="utf-8")


def is_register_object(object_id: str) -> bool:
    return object_id.startswith("reg:")


def is_flag_object(object_id: str) -> bool:
    if not is_register_object(object_id):
        return False
    return object_id[4:].lower() in {
        "cf", "zf", "sf", "of", "pf", "af", "df", "tf", "if",
        "eflags", "rflags", "flags",
    }


def is_execution_position_object(object_id: str) -> bool:
    return object_id.lower() in {"reg:rip", "reg:eip", "reg:ip"}


def is_structural_register(object_id: str) -> bool:
    return object_id.lower() in {"reg:rsp", "reg:esp", "reg:rbp", "reg:ebp"}


def is_analysis_temporary(object_id: str) -> bool:
    return object_id.lower() in {
        "reg:unknown", "reg:temp", "reg:tmp", "unknown", "temp", "tmp"
    }


def object_type(object_id: str, detail: Optional[dict] = None) -> str:
    if detail and detail.get("type"):
        return str(detail["type"])
    if object_id.startswith("imm_occurrence:"):
        return "imm_occurrence"
    for prefix in ("reg:", "var:", "mem:", "stack:", "imm:"):
        if object_id.startswith(prefix):
            return prefix[:-1]
    return "other"


_IMM_OCCURRENCE_RE = re.compile(
    r"^imm_occurrence:0x([0-9a-fA-F]+):"
    r"(mem_disp|mem_scale|mem_base|mem_index|operand_imm|reg_imm):"
    r"(\d+):0x([0-9a-fA-F]+):.*$"
)


def parse_imm_occurrence(object_id: str) -> Optional[Dict[str, Any]]:
    match = _IMM_OCCURRENCE_RE.match(object_id)
    if not match:
        return None
    return {
        "pc": "0x" + match.group(1).lower(),
        "component": match.group(2),
        "operand_index": int(match.group(3)),
        "value": int(match.group(4), 16),
    }


@dataclass(frozen=True)
class FilterReason:
    code: str
    category: str
    message: str


@dataclass
class EligibleLeafObject:
    object_id: str
    object_type: str
    leaf_role: str
    semantic_tags: List[str]
    source_kind: Optional[str]
    occurrence_pc: Optional[str]
    operand_index: Optional[int]
    value_hex: Optional[str]
    bit_size: Optional[int]
    dependency_edges: Dict[str, Any]
    dependency_semantics: List[str]
    object_pc_relations: List[Dict[str, Any]]
    anchor_pcs: List[str]
    mapping_evidence: Optional[Dict[str, Any]]


@dataclass
class EligibleLeafInstruction:
    pc: str
    leaf_role: str
    disasm: str
    mnemonic: str
    mnemonic_provenance: Optional[str]
    operands: List[Dict[str, Any]]
    implicit_reads: List[str]
    implicit_writes: List[str]
    instruction_role: str
    instruction_role_provenance: str
    function_id: Optional[str]
    frame_operation: Optional[Dict[str, Any]]
    code_region: str
    code_region_provenance: str
    source_location: Optional[Dict[str, Any]]
    module: Optional[str]
    section: Optional[str]
    symbol: Optional[str]
    function: Optional[str]
    is_user_code: Optional[bool]
    semantic_tags: List[str]
    use_objects: List[str]
    def_objects: List[str]
    addr_objects: List[str]
    immediates: List[str]
    controlled_by: List[str]
    control_evidence: Dict[str, Any]
    instruction_parent_edges: Dict[str, Any]
    instruction_child_edges: Dict[str, Any]
    dependency_semantics: List[str]
    uses_taint: bool
    suppressed_repeat_records: int


class DependencyModel:
    DIRECT_MAPPING_GROUPS = {"direct_operand", "structural_role"}

    def __init__(self, dep: dict, mapping: Optional[dict] = None):
        self.dep = dep
        self.mapping = mapping or {}

        taint_source = dep.get("taint_source") or {}
        self.seed_objects = set(taint_source.get("seed_object_nodes") or [])
        self.seed_instruction_pcs = {
            norm_hex(pc) for pc in taint_source.get("seed_instruction_pcs") or []
        }

        backward = dep.get("backward") or {}
        self.backward_objects = set(backward.get("objects") or [])
        self.leaf_object_ids = set(backward.get("leaf_objects") or [])
        self.backward_instruction_pcs = {
            norm_hex(pc) for pc in backward.get("instructions") or []
        }
        self.leaf_instruction_pcs = {
            norm_hex(pc) for pc in backward.get("leaf_instructions") or []
        }

        self.object_details: Dict[str, dict] = dep.get("object_details") or {}
        self.instruction_details: Dict[str, dict] = {
            norm_hex(pc): detail
            for pc, detail in (dep.get("instruction_details") or {}).items()
        }
        self.input_warnings: List[dict] = []
        self._validate_input_sets()

        self.mapping_by_object: Dict[str, dict] = {
            entry.get("node_id"): entry
            for entry in self.mapping.get("backward_leaf_mappings", [])
            if isinstance(entry, dict) and entry.get("node_id")
        }

        self.object_pc_relations: Dict[str, Dict[str, Set[str]]] = defaultdict(
            lambda: defaultdict(set)
        )
        self.pc_direct_objects: Dict[str, Set[str]] = defaultdict(set)
        self._build_direct_relation_indexes()
        self._merge_terminal_mapping_relations()

    def _validate_input_sets(self) -> None:
        for object_id in sorted(self.leaf_object_ids):
            if object_id not in self.object_details:
                self.input_warnings.append({
                    "code": "input.leaf-object-detail-missing",
                    "item": object_id,
                })
            if object_id not in self.backward_objects:
                self.input_warnings.append({
                    "code": "input.leaf-object-not-listed-in-backward-set",
                    "item": object_id,
                })
        for pc in sorted_pcs(self.leaf_instruction_pcs):
            if pc not in self.instruction_details:
                self.input_warnings.append({
                    "code": "input.leaf-instruction-detail-missing",
                    "item": pc,
                })
            if pc not in self.backward_instruction_pcs:
                self.input_warnings.append({
                    "code": "input.leaf-instruction-not-listed-in-backward-set",
                    "item": pc,
                })

    def _add_relation(self, object_id: str, pc: Any, relation: str) -> None:
        if not isinstance(object_id, str) or pc is None:
            return
        normalized = norm_hex(pc)
        if not normalized:
            return
        self.object_pc_relations[object_id][normalized].add(relation)
        self.pc_direct_objects[normalized].add(object_id)

    def _build_direct_relation_indexes(self) -> None:
        object_fields = {
            "defined_by": "object_details.defined_by",
            "used_by": "object_details.used_by",
            "addr_used_by": "object_details.addr_used_by",
            "ctrl_used_by": "object_details.ctrl_used_by",
        }
        for object_id, detail in self.object_details.items():
            for field, relation in object_fields.items():
                for pc in safe_list(detail.get(field)):
                    self._add_relation(object_id, pc, relation)
            if detail.get("occurrence_pc") is not None:
                self._add_relation(
                    object_id, detail["occurrence_pc"],
                    "object_details.occurrence_pc",
                )

        instruction_fields = {
            "use_objects": "instruction_details.use_objects",
            "def_objects": "instruction_details.def_objects",
            "addr_objects": "instruction_details.addr_objects",
            "immediates": "instruction_details.immediates",
        }
        for pc, detail in self.instruction_details.items():
            for field, relation in instruction_fields.items():
                for object_id in safe_list(detail.get(field)):
                    self._add_relation(object_id, pc, relation)

    def _merge_terminal_mapping_relations(self) -> None:
        for object_id, entry in self.mapping_by_object.items():
            for relation_entry in safe_list(entry.get("pc_relation_entries")):
                if not isinstance(relation_entry, dict):
                    continue
                groups = set(relation_entry.get("relation_groups") or [])
                if not groups & self.DIRECT_MAPPING_GROUPS:
                    continue
                pc = relation_entry.get("pc")
                for kind in relation_entry.get("relation_kinds") or ["direct_anchor"]:
                    self._add_relation(
                        object_id, pc, f"terminal_mapping.{kind}"
                    )

    def code_region(self, pc: str) -> Tuple[str, str]:
        normalized = norm_hex(pc)
        detail = self.instruction_details.get(normalized)
        if detail is not None:
            return (
                detail.get("code_region") or "unknown",
                detail.get("code_region_provenance") or "missing",
            )
        return "unknown", "instruction-detail-missing"

    def direct_object_pc_relations(self, object_id: str) -> List[dict]:
        result = []
        for pc in sorted_pcs(self.object_pc_relations.get(object_id, {})):
            result.append({
                "pc": pc,
                "relation_kinds": sorted(
                    self.object_pc_relations[object_id][pc]
                ),
            })
        return result

    def object_dependency_edges(self, object_id: str) -> Dict[str, Any]:
        detail = self.object_details.get(object_id, {})
        return {
            "parent_edges": detail.get("parent_edge_details") or {},
            "child_edges": detail.get("child_edge_details") or {},
        }

    def object_dependency_semantics(self, object_id: str) -> List[str]:
        edges = self.object_dependency_edges(object_id)
        kinds = set()
        for direction in ("parent_edges", "child_edges"):
            for edge in edges[direction].values():
                kinds.update(edge.get("kinds") or [])
        return sorted(kinds)

    def mapping_evidence(self, object_id: str) -> Optional[dict]:
        entry = self.mapping_by_object.get(object_id)
        if not entry:
            return None
        executed = entry.get("executed_code_reference") or {}
        return {
            "pc_relation_entries": entry.get("pc_relation_entries") or [],
            "direct_anchor_instruction_evidence": (
                executed.get("direct_anchor_instruction_evidence") or []
            ),
            "source_evidence": executed.get("source_evidence") or [],
            "mapping_inference": entry.get("mapping_inference"),
        }


class LeafDependencyFilter:
    OBSERVATION_CALL_SYMBOLS = {
        "printf", "puts", "putchar", "write", "fprintf", "sprintf",
        "snprintf", "vprintf", "vfprintf", "vsprintf", "vsnprintf",
        "__printf_chk", "__fprintf_chk", "__sprintf_chk", "__snprintf_chk",
    }
    SUPPORTED_OBJECT_TYPES = {
        "reg", "register", "var", "stack", "mem", "memory",
        "imm", "immediate", "imm_occurrence", "flag",
    }
    UNRESOLVED_CATEGORIES = {
        "missing_metadata", "unresolved_representation",
        "non_user_code_unresolved",
    }

    def __init__(self, model: DependencyModel, *, include_seed_leaves: bool = False,
                 include_observation_only: bool = False):
        self.m = model
        self.include_seed_leaves = include_seed_leaves
        self.include_observation_only = include_observation_only

    @staticmethod
    def _reason(code: str, category: str, message: str) -> FilterReason:
        return FilterReason(code, category, message)

    @classmethod
    def _decision(cls, reasons: Sequence[FilterReason]) -> str:
        return (
            "unresolved"
            if any(reason.category in cls.UNRESOLVED_CATEGORIES for reason in reasons)
            else "filtered"
        )

    def _is_observation_only(self, pcs: Sequence[str]) -> bool:
        if not pcs:
            return False
        for pc in pcs:
            detail = self.m.instruction_details.get(norm_hex(pc), {})
            if detail.get("mnemonic") != "call":
                return False
            target = (detail.get("call_target_symbol") or "").lower().strip()
            target = target.split("@", 1)[0]
            if target not in self.OBSERVATION_CALL_SYMBOLS:
                return False
        return True

    def _structural_instruction_reason(self, pc: str) -> Optional[FilterReason]:
        detail = self.m.instruction_details.get(norm_hex(pc))
        if detail is None:
            return self._reason(
                "leaf-instruction.detail-missing", "missing_metadata",
                "instruction_details does not contain this PC",
            )
        mnemonic = (detail.get("mnemonic") or "").lower()
        if not mnemonic:
            return self._reason(
                "leaf-instruction.structured-decoding-missing", "missing_metadata",
                "instruction has no structured mnemonic",
            )
        if mnemonic == "nop":
            return self._reason(
                "leaf-instruction.padding", "runtime_structure",
                "NOP is a padding instruction",
            )
        if mnemonic in {"endbr64", "endbr32"}:
            return self._reason(
                "leaf-instruction.control-flow-protection", "runtime_structure",
                "instruction is a CET control-flow protection marker",
            )
        if mnemonic in {"int3", "ud2"}:
            return self._reason(
                "leaf-instruction.trap-or-invalid", "runtime_structure",
                "instruction is a trap or explicit invalid operation",
            )
        role = detail.get("instruction_role") or "unknown"
        frame_operation = detail.get("frame_operation") or {}
        operation_kind = frame_operation.get("kind")
        if role in {"prologue", "epilogue"}:
            reason_by_operation = {
                "allocate": (
                    "leaf-instruction.stack-space-maintenance",
                    "instruction allocates stack space in function prologue context",
                ),
                "release": (
                    "leaf-instruction.stack-space-maintenance",
                    "instruction releases stack space in function epilogue context",
                ),
                "argument-spill": (
                    "leaf-instruction.argument-spill",
                    "instruction spills an ABI argument in function-entry context",
                ),
                "callee-save-spill": (
                    "leaf-instruction.callee-saved-maintenance",
                    "instruction saves a callee-saved register in prologue context",
                ),
                "callee-save-restore": (
                    "leaf-instruction.callee-saved-maintenance",
                    "instruction restores a callee-saved register in epilogue context",
                ),
                "return": (
                    "leaf-instruction.return-structural",
                    "instruction performs function return in epilogue context",
                ),
                "leave": (
                    "leaf-instruction.return-structural",
                    "instruction tears down the frame in epilogue context",
                ),
            }
            code, message = reason_by_operation.get(operation_kind, (
                "leaf-instruction.stack-frame-structural",
                "instruction is identified as function prologue/epilogue structure",
            ))
            return self._reason(code, "abi_structure", message)
        return None

    def _instruction_filter_reasons(self, pc: str, *, leaf_input: bool) -> List[FilterReason]:
        reasons = []
        normalized = norm_hex(pc)
        if not is_valid_pc(pc):
            reasons.append(self._reason(
                "leaf-instruction.invalid-pc", "unresolved_representation",
                "instruction PC is not a canonical non-negative hexadecimal address",
            ))
        if leaf_input and not self.include_seed_leaves and normalized in self.m.seed_instruction_pcs:
            reasons.append(self._reason(
                "leaf-instruction.analysis-seed", "analysis_boundary",
                "instruction is a slicing seed rather than an upstream leaf item",
            ))
        region, _ = self.m.code_region(normalized)
        if region == "runtime":
            reasons.append(self._reason(
                "leaf-instruction.runtime-code", "non_user_code",
                "upstream structured code-region evidence classifies this instruction as runtime",
            ))
        elif region != "user":
            reasons.append(self._reason(
                "leaf-instruction.user-code-region-unresolved",
                "non_user_code_unresolved",
                "instruction lacks affirmative structured user-code-region evidence",
            ))
        structural = self._structural_instruction_reason(normalized)
        if structural is not None:
            reasons.append(structural)
        return reasons

    def _immediate_filter_reasons(self, object_id: str, detail: dict) -> List[FilterReason]:
        parsed = parse_imm_occurrence(object_id)
        if parsed is None:
            return []
        reasons = []
        pc = parsed["pc"]
        component = parsed["component"]
        instruction = self.m.instruction_details.get(pc, {})
        mnemonic = (instruction.get("mnemonic") or "").lower()
        operand = next((
            item for item in instruction.get("operands") or []
            if item.get("index") == parsed["operand_index"]
        ), {})
        tags = set(detail.get("semantic_tags") or [])

        if component == "operand_imm" and (
            mnemonic.startswith("j") or mnemonic.startswith("loop")
        ):
            reasons.append(self._reason(
                "leaf-object.control-flow-target-immediate",
                "unsupported_representation",
                "direct branch target is not treated as a standalone data immediate",
            ))
        if component == "operand_imm" and mnemonic == "call":
            reasons.append(self._reason(
                "leaf-object.call-target-immediate",
                "unsupported_representation",
                "direct call target is not treated as a standalone data immediate",
            ))
        if component == "mem_disp" and operand.get("kind") == "memory":
            base = operand.get("base")
            displacement = operand.get("displacement")
            if base in {"rsp", "esp", "rbp", "ebp"} and displacement is not None:
                reasons.append(self._reason(
                    "leaf-object.stack-layout-displacement", "abi_structure",
                    "stack/frame-relative displacement identifies a stack layout slot",
                ))
        if (
            component == "mem_disp"
            and operand.get("kind") == "memory"
            and operand.get("base") in {"rip", "eip"}
        ):
            reasons.append(self._reason(
                "leaf-object.relocation-displacement", "runtime_structure",
                "RIP-relative displacement is treated as code/data relocation structure",
            ))
        if tags & {"structural_abi_constant", "stack_alignment_constant"}:
            reasons.append(self._reason(
                "leaf-object.abi-structural-immediate", "abi_structure",
                "immediate is tagged as ABI or stack-alignment structure",
            ))
        if component in {"mem_scale", "mem_disp"}:
            stable_occurrence = (
                detail.get("occurrence_pc") is not None
                and detail.get("operand_index") is not None
            )
            if not stable_occurrence:
                reasons.append(self._reason(
                    "leaf-object.no-standalone-encoding",
                    "unsupported_representation",
                    "address component lacks a stable encoded occurrence",
                ))
        return reasons

    def _eligible_anchor_relations(self, object_id: str) -> List[dict]:
        eligible = []
        for relation in self.m.direct_object_pc_relations(object_id):
            pc = relation["pc"]
            if not self._instruction_filter_reasons(pc, leaf_input=False):
                region, evidence = self.m.code_region(pc)
                eligible.append({
                    **relation,
                    "code_region": region,
                    "code_region_evidence": evidence,
                })
        return eligible

    def _user_context_relations(self, object_id: str) -> List[dict]:
        """Return valid user-code mappings without applying mutability rules."""
        result = []
        for relation in self.m.direct_object_pc_relations(object_id):
            pc = relation["pc"]
            detail = self.m.instruction_details.get(norm_hex(pc))
            region, evidence = self.m.code_region(pc)
            if (
                is_valid_pc(pc) and detail is not None and region == "user"
                and bool(detail.get("mnemonic"))
            ):
                result.append({
                    **relation,
                    "code_region": region,
                    "code_region_evidence": evidence,
                })
        return result

    def _evaluate_leaf_object(self, object_id: str) -> Tuple[List[FilterReason], List[dict]]:
        detail = self.m.object_details.get(object_id)
        if detail is None:
            return [self._reason(
                "leaf-object.detail-missing", "missing_metadata",
                "object_details does not contain this leaf object",
            )], []

        reasons: List[FilterReason] = []
        resolved_type = object_type(object_id, detail).lower()
        if resolved_type not in self.SUPPORTED_OBJECT_TYPES:
            reasons.append(self._reason(
                "leaf-object.type-unresolved", "unresolved_representation",
                f"unsupported or unknown object representation: {resolved_type}",
            ))
        if not self.include_seed_leaves and object_id in self.m.seed_objects:
            reasons.append(self._reason(
                "leaf-object.analysis-seed", "analysis_boundary",
                "object is a slicing seed rather than an upstream leaf item",
            ))
        if is_execution_position_object(object_id):
            reasons.append(self._reason(
                "leaf-object.execution-position-state", "runtime_structure",
                "instruction pointer state has no standalone data-object representation",
            ))
        elif is_analysis_temporary(object_id):
            reasons.append(self._reason(
                "leaf-object.analysis-temporary", "noise",
                "object identity is an analysis temporary or unknown value",
            ))
        elif is_flag_object(object_id):
            reasons.append(self._reason(
                "leaf-object.implicit-flag-state", "unsupported_representation",
                "flags are implicit machine state represented by their instructions",
            ))
        elif is_structural_register(object_id):
            reasons.append(self._reason(
                "leaf-object.stack-frame-structural-register", "abi_structure",
                "stack/frame pointer is structural ABI state",
            ))
        elif object_id.startswith("mem:"):
            reasons.append(self._reason(
                "leaf-object.runtime-memory-instance", "unstable_identity",
                "concrete runtime memory address is not a stable static object",
            ))

        reasons.extend(self._immediate_filter_reasons(object_id, detail))
        direct_relations = self.m.direct_object_pc_relations(object_id)
        all_direct_pcs = [item["pc"] for item in direct_relations]
        if any(not is_valid_pc(item["pc"]) for item in direct_relations):
            reasons.append(self._reason(
                "leaf-object.anchor-pc-invalid", "unresolved_representation",
                "one or more direct object mappings use an invalid PC",
            ))
        if (
            not self.include_observation_only
            and self._is_observation_only(all_direct_pcs)
        ):
            reasons.append(self._reason(
                "leaf-object.observation-only", "observation_only",
                "object is directly used only by observation/printing calls",
            ))

        anchors = self._eligible_anchor_relations(object_id)
        if not anchors:
            regions = {
                self.m.code_region(item["pc"])[0]
                for item in direct_relations if is_valid_pc(item["pc"])
            }
            if regions and "user" not in regions and regions != {"runtime"}:
                reasons.append(self._reason(
                    "leaf-object.user-anchor-region-unresolved",
                    "non_user_code_unresolved",
                    "direct mappings lack affirmative structured user-code evidence",
                ))
            reasons.append(self._reason(
                "leaf-object.user-anchor-missing", "unsupported_representation",
                "object has no directly mapped non-structural user-code instruction",
            ))
        return reasons, anchors

    def filter_leaf_objects(self) -> Tuple[List[dict], List[dict]]:
        eligible, filtered = [], []
        for object_id in sorted(self.m.leaf_object_ids):
            reasons, anchors = self._evaluate_leaf_object(object_id)
            detail = self.m.object_details.get(object_id, {})
            if reasons:
                filtered.append({
                    "item_id": object_id,
                    "item_kind": "object",
                    "leaf_role": "backward_leaf",
                    "decision": self._decision(reasons),
                    "object_type": object_type(object_id, detail),
                    "semantic_tags": sorted(detail.get("semantic_tags") or []),
                    "dependency_edges": self.m.object_dependency_edges(object_id),
                    "dependency_semantics": self.m.object_dependency_semantics(object_id),
                    "object_pc_relations": self.m.direct_object_pc_relations(object_id),
                    "mapping_evidence": self.m.mapping_evidence(object_id),
                    "reason_codes": sorted({reason.code for reason in reasons}),
                    "reasons": [asdict(reason) for reason in sorted(reasons, key=lambda r: r.code)],
                    "related_pcs": sorted_pcs(
                        item["pc"] for item in self.m.direct_object_pc_relations(object_id)
                    ),
                })
                continue
            eligible.append(asdict(EligibleLeafObject(
                object_id=object_id,
                object_type=object_type(object_id, detail),
                leaf_role="backward_leaf",
                semantic_tags=sorted(detail.get("semantic_tags") or []),
                source_kind=detail.get("source_kind"),
                occurrence_pc=(norm_hex(detail["occurrence_pc"])
                               if detail.get("occurrence_pc") is not None else None),
                operand_index=detail.get("operand_index"),
                value_hex=detail.get("value_hex"),
                bit_size=detail.get("bit_size"),
                dependency_edges=self.m.object_dependency_edges(object_id),
                dependency_semantics=self.m.object_dependency_semantics(object_id),
                object_pc_relations=anchors,
                anchor_pcs=[item["pc"] for item in anchors],
                mapping_evidence=self.m.mapping_evidence(object_id),
            )))
        return eligible, filtered

    def filter_leaf_instructions(self) -> Tuple[List[dict], List[dict]]:
        eligible, filtered = [], []
        for pc in sorted(self.m.leaf_instruction_pcs, key=stable_pc_key):
            reasons = self._instruction_filter_reasons(pc, leaf_input=True)
            detail = self.m.instruction_details.get(pc, {})
            if reasons:
                filtered.append({
                    "item_id": pc,
                    "item_kind": "instruction",
                    "leaf_role": "backward_leaf",
                    "decision": self._decision(reasons),
                    "disasm": detail.get("disasm"),
                    "mnemonic": detail.get("mnemonic"),
                    "mnemonic_provenance": detail.get("mnemonic_provenance"),
                    "instruction_role": detail.get("instruction_role"),
                    "instruction_role_provenance": detail.get(
                        "instruction_role_provenance"
                    ),
                    "function_id": detail.get("function_id"),
                    "module": detail.get("module"),
                    "section": detail.get("section"),
                    "symbol": detail.get("symbol"),
                    "function": detail.get("function"),
                    "is_user_code": detail.get("is_user_code"),
                    "code_region": detail.get("code_region") or "unknown",
                    "code_region_provenance": detail.get(
                        "code_region_provenance"
                    ) or "missing",
                    "semantic_tags": sorted(detail.get("semantic_tags") or []),
                    "use_objects": sorted(detail.get("use_objects") or []),
                    "def_objects": sorted(detail.get("def_objects") or []),
                    "addr_objects": sorted(detail.get("addr_objects") or []),
                    "immediates": sorted(detail.get("immediates") or []),
                    "controlled_by": sorted_pcs(detail.get("controlled_by") or []),
                    "control_evidence": detail.get("control_evidence") or {},
                    "instruction_parent_edges": detail.get(
                        "instruction_parent_edges"
                    ) or {},
                    "instruction_child_edges": detail.get(
                        "instruction_child_edges"
                    ) or {},
                    "dependency_semantics": sorted(
                        detail.get("dependency_semantics") or []
                    ),
                    "reason_codes": sorted({reason.code for reason in reasons}),
                    "reasons": [asdict(reason) for reason in sorted(reasons, key=lambda r: r.code)],
                })
                continue
            eligible.append(asdict(EligibleLeafInstruction(
                pc=pc,
                leaf_role="backward_leaf",
                disasm=detail.get("disasm") or "",
                mnemonic=detail.get("mnemonic") or "",
                mnemonic_provenance=detail.get("mnemonic_provenance"),
                operands=detail.get("operands") or [],
                implicit_reads=detail.get("implicit_reads") or [],
                implicit_writes=detail.get("implicit_writes") or [],
                instruction_role=detail.get("instruction_role") or "unknown",
                instruction_role_provenance=(
                    detail.get("instruction_role_provenance") or "missing"
                ),
                function_id=detail.get("function_id"),
                frame_operation=detail.get("frame_operation"),
                code_region=detail.get("code_region") or "unknown",
                code_region_provenance=(
                    detail.get("code_region_provenance") or "missing"
                ),
                source_location=detail.get("source_location"),
                module=detail.get("module"),
                section=detail.get("section"),
                symbol=detail.get("symbol"),
                function=detail.get("function"),
                is_user_code=detail.get("is_user_code"),
                semantic_tags=sorted(detail.get("semantic_tags") or []),
                use_objects=sorted(detail.get("use_objects") or []),
                def_objects=sorted(detail.get("def_objects") or []),
                addr_objects=sorted(detail.get("addr_objects") or []),
                immediates=sorted(detail.get("immediates") or []),
                controlled_by=sorted_pcs(detail.get("controlled_by") or []),
                control_evidence=detail.get("control_evidence") or {},
                instruction_parent_edges=(
                    detail.get("instruction_parent_edges") or {}
                ),
                instruction_child_edges=(
                    detail.get("instruction_child_edges") or {}
                ),
                dependency_semantics=sorted(
                    detail.get("dependency_semantics") or []
                ),
                uses_taint=bool(detail.get("uses_taint", False)),
                suppressed_repeat_records=int(
                    detail.get("suppressed_repeat_records", 0) or 0
                ),
            )))
        return eligible, filtered

    def _related_slice_objects(self, pc: str) -> List[str]:
        return sorted(
            object_id for object_id in self.m.pc_direct_objects.get(pc, set())
            if object_id in self.m.backward_objects
        )

    def _anchor_dependency_semantics(self, object_entries: Sequence[dict],
                                     instruction: Optional[dict]) -> List[str]:
        semantics = set()
        for entry in object_entries:
            semantics.update(entry.get("dependency_semantics") or [])
        if instruction and (
            instruction.get("controlled_by") or instruction.get("control_evidence")
        ):
            semantics.add("control")
        if instruction:
            semantics.update(instruction.get("dependency_semantics") or [])
            leaf_instruction = instruction.get("leaf_instruction_dependency") or {}
            semantics.update(leaf_instruction.get("dependency_semantics") or [])
        for entry in (instruction or {}).get("filtered_leaf_context") or []:
            semantics.update(entry.get("dependency_semantics") or [])
        return sorted(semantics)

    @staticmethod
    def _normalized_source_location(value: Any, provenance: str) -> Optional[dict]:
        if not isinstance(value, dict) or not value.get("file") or not value.get("line"):
            return None
        return {
            "file": value.get("file"),
            "line": value.get("line"),
            "function": value.get("function"),
            "provenance": provenance,
        }

    def _object_source_locations_for_pc(self, obj: dict, pc: str) -> List[dict]:
        locations = []
        mapping = obj.get("mapping_evidence") or {}
        for evidence in mapping.get("source_evidence") or []:
            if norm_hex(pc) not in {norm_hex(value) for value in evidence.get("pcs") or []}:
                continue
            location = self._normalized_source_location(
                evidence, "terminal-mapping-source-evidence"
            )
            if location is not None:
                locations.append(location)
        return locations

    def build_anchor_instructions(self, eligible_objects: List[dict],
                                  eligible_instructions: List[dict],
                                  filtered_objects: Optional[List[dict]] = None,
                                  filtered_instructions: Optional[List[dict]] = None) -> List[dict]:
        anchors: Dict[str, dict] = {}

        def ensure_anchor(pc: str) -> dict:
            pc = norm_hex(pc)
            detail = self.m.instruction_details.get(pc, {})
            region, evidence = self.m.code_region(pc)
            direct_source_location = self._normalized_source_location(
                detail.get("source_location"),
                "dependency-summary-structured-source",
            )
            return anchors.setdefault(pc, {
                "pc": pc,
                "disasm": detail.get("disasm") or "",
                "mnemonic": detail.get("mnemonic") or "",
                "mnemonic_provenance": detail.get("mnemonic_provenance"),
                "operands": detail.get("operands") or [],
                "implicit_reads": detail.get("implicit_reads") or [],
                "implicit_writes": detail.get("implicit_writes") or [],
                "instruction_role": detail.get("instruction_role") or "unknown",
                "instruction_role_provenance": detail.get(
                    "instruction_role_provenance"
                ) or "missing",
                "function_id": detail.get("function_id"),
                "frame_operation": detail.get("frame_operation"),
                "module": detail.get("module"),
                "section": detail.get("section"),
                "symbol": detail.get("symbol"),
                "function": detail.get("function"),
                "is_user_code": detail.get("is_user_code"),
                "source_location": None,
                "source_locations": (
                    [direct_source_location] if direct_source_location else []
                ),
                "code_region": region,
                "code_region_provenance": evidence,
                "anchor_sources": set(),
                "leaf_object_dependencies": [],
                "leaf_instruction_dependency": None,
                "filtered_leaf_context": [],
                "instruction_objects": {
                    "use_objects": sorted(detail.get("use_objects") or []),
                    "def_objects": sorted(detail.get("def_objects") or []),
                    "addr_objects": sorted(detail.get("addr_objects") or []),
                    "immediates": sorted(detail.get("immediates") or []),
                },
                "related_slice_objects": self._related_slice_objects(pc),
                "dependency_semantics": set(),
                "semantic_tags": sorted(detail.get("semantic_tags") or []),
                "controlled_by": sorted_pcs(detail.get("controlled_by") or []),
                "control_evidence": detail.get("control_evidence") or {},
                "instruction_parent_edges": detail.get(
                    "instruction_parent_edges"
                ) or {},
                "instruction_child_edges": detail.get(
                    "instruction_child_edges"
                ) or {},
                "input_capability_notes": [
                    "instruction dependency edge kinds are consumed from upstream; "
                    "they are never inferred from mnemonic text by this filter"
                ],
            })

        for obj in eligible_objects:
            for relation in obj.get("object_pc_relations") or []:
                anchor = ensure_anchor(relation["pc"])
                anchor["anchor_sources"].add("eligible_leaf_object")
                dependency = {
                    "object_id": obj["object_id"],
                    "object_type": obj["object_type"],
                    "relation_kinds": relation.get("relation_kinds") or [],
                    "semantic_tags": obj.get("semantic_tags") or [],
                    "dependency_semantics": obj.get("dependency_semantics") or [],
                }
                if dependency not in anchor["leaf_object_dependencies"]:
                    anchor["leaf_object_dependencies"].append(dependency)
                anchor["source_locations"].extend(
                    self._object_source_locations_for_pc(obj, relation["pc"])
                )

        for instruction in eligible_instructions:
            anchor = ensure_anchor(instruction["pc"])
            anchor["anchor_sources"].add("eligible_leaf_instruction")
            anchor["leaf_instruction_dependency"] = {
                "is_leaf_instruction": True,
                "dependency_semantics": instruction.get(
                    "dependency_semantics"
                ) or [],
                "controlled_by": instruction.get("controlled_by") or [],
                "control_evidence": instruction.get("control_evidence") or {},
            }
        for obj in filtered_objects or []:
            for relation in self._user_context_relations(obj["item_id"]):
                anchor = ensure_anchor(relation["pc"])
                anchor["anchor_sources"].add("filtered_leaf_object_context")
                context = {
                    "item_id": obj["item_id"],
                    "item_kind": "object",
                    "decision": obj.get("decision") or "filtered",
                    "object_type": obj.get("object_type"),
                    "relation_kinds": relation.get("relation_kinds") or [],
                    "reason_codes": obj.get("reason_codes") or [],
                    "dependency_semantics": obj.get("dependency_semantics") or [],
                }
                if context not in anchor["filtered_leaf_context"]:
                    anchor["filtered_leaf_context"].append(context)
        for instruction in filtered_instructions or []:
            pc = instruction["item_id"]
            detail = self.m.instruction_details.get(norm_hex(pc), {})
            region, _evidence = self.m.code_region(pc)
            if not (is_valid_pc(pc) and region == "user" and detail.get("mnemonic")):
                continue
            anchor = ensure_anchor(pc)
            anchor["anchor_sources"].add("filtered_leaf_instruction_context")
            context = {
                "item_id": pc,
                "item_kind": "instruction",
                "decision": instruction.get("decision") or "filtered",
                "reason_codes": instruction.get("reason_codes") or [],
                "dependency_semantics": instruction.get(
                    "dependency_semantics"
                ) or [],
            }
            if context not in anchor["filtered_leaf_context"]:
                anchor["filtered_leaf_context"].append(context)
        result = []
        for pc in sorted(anchors, key=stable_pc_key):
            anchor = anchors[pc]
            anchor["anchor_sources"] = sorted(anchor["anchor_sources"])
            anchor["leaf_object_dependencies"].sort(key=lambda item: item["object_id"])
            anchor["filtered_leaf_context"].sort(
                key=lambda item: (item["item_kind"], item["item_id"])
            )
            anchor["eligible_for_mutation_stage"] = bool(
                {"eligible_leaf_object", "eligible_leaf_instruction"}
                & set(anchor["anchor_sources"])
            )
            anchor["dependency_semantics"] = self._anchor_dependency_semantics(
                anchor["leaf_object_dependencies"], anchor
            )
            unique_locations = {}
            for item in anchor["source_locations"]:
                key = (item.get("file"), item.get("line"), item.get("function"))
                provenance = item.get("provenance")
                if key not in unique_locations:
                    unique_locations[key] = {
                        "file": item.get("file"),
                        "line": item.get("line"),
                        "function": item.get("function"),
                        "provenances": [],
                    }
                if provenance and provenance not in unique_locations[key]["provenances"]:
                    unique_locations[key]["provenances"].append(provenance)
            for item in unique_locations.values():
                item["provenances"].sort()
            anchor["source_locations"] = sorted(
                unique_locations.values(),
                key=lambda item: (
                    item.get("file") or "", item.get("line") or 0,
                    item.get("function") or "",
                ),
            )
            anchor["source_location"] = (
                anchor["source_locations"][0]
                if len(anchor["source_locations"]) == 1 else None
            )
            result.append(anchor)
        return result


def build_filter_summary(model: DependencyModel, eligible_objects: List[dict],
                         eligible_instructions: List[dict], anchors: List[dict],
                         filtered_objects: List[dict],
                         filtered_instructions: List[dict]) -> dict:
    reason_counts = Counter()
    for item in filtered_objects + filtered_instructions:
        reason_counts.update(item.get("reason_codes") or [])

    unresolved_object_count = sum(
        item.get("decision") == "unresolved" for item in filtered_objects
    )
    unresolved_instruction_count = sum(
        item.get("decision") == "unresolved" for item in filtered_instructions
    )
    if model.input_warnings or unresolved_object_count or unresolved_instruction_count:
        status = "partial_unresolved"
    elif not eligible_objects and not eligible_instructions:
        status = "no_eligible_leaf_items"
    else:
        status = "ok"

    return {
        "status": status,
        "contract": "leaf-dependency-filter-and-user-anchor-mapper.v3",
        "input": {
            "leaf_objects": len(model.leaf_object_ids),
            "leaf_instructions": len(model.leaf_instruction_pcs),
        },
        "eligible": {
            "leaf_objects": len(eligible_objects),
            "leaf_instructions": len(eligible_instructions),
            "anchor_instructions": sum(
                bool(item.get("eligible_for_mutation_stage")) for item in anchors
            ),
            "context_only_anchor_instructions": sum(
                not bool(item.get("eligible_for_mutation_stage")) for item in anchors
            ),
        },
        "filtered": {
            "leaf_objects": len(filtered_objects),
            "leaf_instructions": len(filtered_instructions),
        },
        "unresolved": {
            "leaf_objects": unresolved_object_count,
            "leaf_instructions": unresolved_instruction_count,
        },
        "filter_reason_counts": dict(sorted(reason_counts.items())),
        "input_consistency_warnings": model.input_warnings,
        "capabilities": {
            "object_dependency_edge_kinds": True,
            "instruction_control_evidence": True,
            "full_instruction_dependency_edge_kinds": all(
                "instruction_parent_edges" in detail
                and "instruction_child_edges" in detail
                and "dependency_semantics" in detail
                for detail in model.instruction_details.values()
            ),
            "terminal_mapping_loaded": bool(model.mapping_by_object),
            "structured_instruction_operands": all(
                "operands" in detail and "mnemonic" in detail
                for detail in model.instruction_details.values()
            ),
            "structured_code_regions": all(
                "code_region" in detail and "code_region_provenance" in detail
                for detail in model.instruction_details.values()
            ),
        },
        "non_responsibilities": [
            "mutation operator recommendation",
            "candidate ranking or priority",
            "mutation effectiveness estimation",
            "reachability recomputation",
        ],
    }


def load_optional_json(path: Optional[str], label: str) -> Optional[dict]:
    if not path:
        return None
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"[WARN] cannot load {label}: {path}: {exc}", file=sys.stderr)
        return None


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Filter backward leaf dependency objects/instructions and map "
            "eligible items to user-code instruction anchors."
        )
    )
    parser.add_argument("--dependency-summary", required=True)
    parser.add_argument("--terminal-mapping", default=None)
    parser.add_argument("--outdir", default="filter_out")
    parser.add_argument("--include-seed-leaves", action="store_true")
    parser.add_argument("--include-observation-only", action="store_true")
    args = parser.parse_args()

    with open(args.dependency_summary, "r", encoding="utf-8") as handle:
        dependency_summary = json.load(handle)

    mapping = load_optional_json(args.terminal_mapping, "terminal mapping")
    model = DependencyModel(dependency_summary, mapping)
    leaf_filter = LeafDependencyFilter(
        model,
        include_seed_leaves=args.include_seed_leaves,
        include_observation_only=args.include_observation_only,
    )

    eligible_objects, filtered_objects = leaf_filter.filter_leaf_objects()
    eligible_instructions, filtered_instructions = (
        leaf_filter.filter_leaf_instructions()
    )
    anchors = leaf_filter.build_anchor_instructions(
        eligible_objects,
        eligible_instructions,
        filtered_objects,
        filtered_instructions,
    )
    summary = build_filter_summary(
        model,
        eligible_objects,
        eligible_instructions,
        anchors,
        filtered_objects,
        filtered_instructions,
    )

    outdir = Path(args.outdir)
    dump_json(outdir / "eligible_leaf_objects.json", eligible_objects)
    dump_json(outdir / "eligible_leaf_instructions.json", eligible_instructions)
    dump_json(outdir / "mutation_anchor_instructions.json", anchors)
    dump_json(outdir / "filtered_leaf_items.json", {
        "objects": filtered_objects,
        "instructions": filtered_instructions,
    })
    dump_json(outdir / "filter_summary.json", summary)

    print(
        f"[OK] {len(eligible_objects)} eligible leaf objects, "
        f"{len(eligible_instructions)} eligible leaf instructions, "
        f"{len(anchors)} anchors -> {outdir}/"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
