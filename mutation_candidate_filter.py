#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

v2.4 相对 v2.3 的变化：
─────────────────────────
1. Tier 分级精细化：
   - primary: 比较/条件分支/关键立即数/核心算术/涉及 var 对象的操作
   - secondary: 仅涉及 stack 的普通 mov/地址计算/一般内存操作
   - contextual: 函数序言尾声/参数保存/callee-saved/generic

2. 函数序言/尾声指令识别与降级：
   - 参数保存 (mov [rbp-N], rdi/rsi/rdx/rcx/r8/r9)
   - callee-saved 保存/恢复 (push/pop rbx/r12-r15)
   - 栈帧分配 (sub rsp, N)
   这些指令降级为 contextual tier，不参与 primary 分级。

3. anchor 增加 is_prologue_epilogue 标记，便于变异器优先选择
   非序言/尾声的 anchor。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, FrozenSet, List, Optional, Set, Tuple


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def norm_hex(v) -> str:
    if isinstance(v, int):
        return hex(v)
    s = str(v).strip().lower()
    if s.startswith("0x"):
        try:
            return hex(int(s, 16))
        except ValueError:
            return s
    return s


def to_signed_64(val: int) -> int:
    if val >= (1 << 63):
        return val - (1 << 64)
    return val


def safe_list(v) -> list:
    if v is None:
        return []
    if isinstance(v, list):
        return v
    if isinstance(v, (set, tuple)):
        return list(v)
    return [v]


def uniq_keep_order(seq):
    seen = set()
    out = []
    for x in seq:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out


def dump_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# object type helpers
# ---------------------------------------------------------------------------

def is_register_object(oid: str) -> bool:
    return oid.startswith("reg:")

def is_flag_object(oid: str) -> bool:
    if not oid.startswith("reg:"):
        return False
    name = oid[4:].lower()
    return name in {"cf", "zf", "sf", "of", "pf", "af", "df", "tf", "if",
                    "eflags", "rflags", "flags"}

def is_imm_object(oid: str) -> bool:
    return oid.startswith("imm_occurrence:") or oid.startswith("imm:")

def is_var_object(oid: str) -> bool:
    return oid.startswith("var:")

def is_mem_object(oid: str) -> bool:
    return oid.startswith("mem:")

def is_stack_object(oid: str) -> bool:
    return oid.startswith("stack:")

def is_noise_object(oid: str) -> bool:
    lo = oid.lower()
    return lo in {"reg:rip", "reg:eip", "reg:unknown", "reg:temp", "reg:tmp"}

def is_structural_register(oid: str) -> bool:
    lo = oid.lower()
    return lo in {"reg:rsp", "reg:esp", "reg:rbp", "reg:ebp"}

def object_type(oid: str) -> str:
    if oid.startswith("imm_occurrence:"):
        return "imm_occurrence"
    for p in ("reg:", "var:", "mem:", "stack:", "imm:"):
        if oid.startswith(p):
            return p.rstrip(":")
    return "other"


# ---------------------------------------------------------------------------
# imm_occurrence structural parsing
# ---------------------------------------------------------------------------

_IMM_OCC_RE = re.compile(
    r"^imm_occurrence:0x([0-9a-fA-F]+):(mem_disp|mem_scale|mem_base|mem_index|operand_imm|reg_imm)"
    r":(\d+):0x([0-9a-fA-F]+):.*$"
)

def parse_imm_occurrence(oid: str) -> Optional[Dict[str, Any]]:
    m = _IMM_OCC_RE.match(oid)
    if not m:
        return None
    return {
        "pc": "0x" + m.group(1).lower(),
        "component": m.group(2),
        "operand_index": int(m.group(3)),
        "value": int(m.group(4), 16),
    }


# ---------------------------------------------------------------------------
# stack object parsing
# ---------------------------------------------------------------------------

_STACK_RE = re.compile(r"^stack:\[(\w+)([+-]0x[0-9a-fA-F]+)\]$")

def parse_stack_object(oid: str) -> Optional[Dict[str, Any]]:
    m = _STACK_RE.match(oid)
    if not m:
        return None
    base = m.group(1).lower()
    offset_str = m.group(2)
    try:
        offset = int(offset_str, 16)
    except ValueError:
        offset = 0
    return {"base": base, "offset": offset}


# ---------------------------------------------------------------------------
# Type-conversion instruction detection
# ---------------------------------------------------------------------------

_TYPE_CONV_PATTERNS = [
    (re.compile(r"^mov\s+(e[a-d]x|e[sd]i|esp|ebp),\s+\1$", re.I), "32→64 zero-extension"),
    (re.compile(r"^movzx\s+\w+,\s+(al|ah|bl|bh|cl|ch|dl|dh|ax|bx|cx|dx|si|di|bp|sp|sil|dil|bpl|spl|r\d+b|r\d+w)$", re.I),
     "zero-extension"),
    (re.compile(r"^movsx[d]?\s+\w+,\s+\w+$", re.I), "sign-extension"),
    (re.compile(r"^(cdq|cdqe|cqo|cwde|cbw|cwd)$", re.I), "implicit sign-extension"),
]

def is_type_conversion_instruction(disasm: str) -> Tuple[bool, str]:
    dis_stripped = disasm.strip()
    if ":" in dis_stripped:
        dis_stripped = dis_stripped.split(":", 1)[1].strip()
    for pattern, desc in _TYPE_CONV_PATTERNS:
        if pattern.match(dis_stripped):
            return True, desc
    return False, ""


# ---------------------------------------------------------------------------
# Prologue / epilogue instruction detection  (v2.4 新增)
# ---------------------------------------------------------------------------

# 函数参数寄存器 (System V AMD64 ABI)
_ARG_REGS = {"rdi", "edi", "rsi", "esi", "rdx", "edx", "rcx", "ecx", "r8", "r8d", "r9", "r9d"}
# callee-saved 寄存器
_CALLEE_SAVED_REGS = {"rbx", "ebx", "r12", "r12d", "r13", "r13d", "r14", "r14d", "r15", "r15d"}

def is_prologue_epilogue_instruction(mnemonic: str, disasm: str) -> Tuple[bool, str]:
    """
    识别函数序言/尾声指令。
    返回 (is_prologue_epilogue, description)。
    注意：push rbp / pop rbp / mov rbp,rsp / ret 等已在
    _is_pure_structural_instruction 中处理，这里处理其余的序言/尾声指令。
    """
    dl = disasm.strip().lower()

    # 1. 参数保存: mov [rbp - N], rdi/rsi/rdx/rcx/r8/r9
    if mnemonic == "mov":
        # mov qword/dword ptr [rbp - 0xXX], <arg_reg>
        m = re.match(r"mov\s+(?:qword|dword|word|byte)\s+ptr\s+\[rbp\s*-\s*0x[0-9a-f]+\]\s*,\s*(\w+)", dl)
        if m:
            src_reg = m.group(1)
            if src_reg in _ARG_REGS:
                return True, f"函数参数保存 ({src_reg} → 栈)"

    # 2. callee-saved 寄存器保存: push rbx / push r12-r15
    if mnemonic == "push":
        m = re.match(r"push\s+(\w+)", dl)
        if m and m.group(1) in _CALLEE_SAVED_REGS:
            return True, f"callee-saved 寄存器保存 (push {m.group(1)})"

    # 3. callee-saved 寄存器恢复: pop rbx / pop r12-r15
    if mnemonic == "pop":
        m = re.match(r"pop\s+(\w+)", dl)
        if m and m.group(1) in _CALLEE_SAVED_REGS:
            return True, f"callee-saved 寄存器恢复 (pop {m.group(1)})"

    # 4. 栈帧分配: sub rsp, N
    if mnemonic == "sub":
        m = re.match(r"sub\s+rsp\s*,\s*0x[0-9a-f]+", dl)
        if m:
            return True, "栈帧分配 (sub rsp, N)"
        m = re.match(r"sub\s+esp\s*,\s*0x[0-9a-f]+", dl)
        if m:
            return True, "栈帧分配 (sub esp, N)"

    # 5. 栈帧释放: add rsp, N
    if mnemonic == "add":
        m = re.match(r"add\s+rsp\s*,\s*0x[0-9a-f]+", dl)
        if m:
            return True, "栈帧释放 (add rsp, N)"
        m = re.match(r"add\s+esp\s*,\s*0x[0-9a-f]+", dl)
        if m:
            return True, "栈帧释放 (add esp, N)"

    return False, ""


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class StrongCausalObject:
    object_id: str
    object_type: str
    causal_role_class: str
    direct_mutation_preferred: bool
    deletion_candidate_only: bool
    recommended_actions: List[str]
    semantic_tags: List[str]
    direct_semantic_roles: List[str]
    contextual_semantic_roles: List[str]
    qualification_reasons: List[str]
    root_evidence: List[str]
    rationale: List[str]
    representative_pcs: List[str]
    representative_disasm: List[str]
    related_anchor_pcs: List[str]
    contextual_related_pcs: List[str]
    source_refs: List[str]
    backward_distance: Optional[int] = None


@dataclass
class AnchorCandidate:
    pc: str
    mnemonic: str
    disasm: str
    function: Optional[str]
    source_file: Optional[str]
    source_line: Optional[int]
    anchor_tier: str
    anchor_kinds: List[str]
    recommended_mutations: List[str]
    causal_objects: List[str]
    explanatory_objects: List[str]
    related_strong_objects: List[str]
    rationale: List[str]
    is_prologue_epilogue: bool = False
    prologue_epilogue_desc: Optional[str] = None


# ---------------------------------------------------------------------------
# DependencyModel
# ---------------------------------------------------------------------------

class DependencyModel:

    def __init__(self, dep: dict, mapping: Optional[dict], path_report: Optional[dict]):
        # ---- taint_source ----
        ts = dep.get("taint_source") or {}
        seed_nodes = ts.get("seed_object_nodes") or []
        self.seed_object: str = seed_nodes[0] if seed_nodes else ts.get("symbol", "")
        self.seed_pcs: Set[str] = {norm_hex(pc) for pc in (ts.get("seed_instruction_pcs") or [])}
        self.seed_symbol: str = ts.get("symbol", "")
        self.seed_address: int = ts.get("address", 0)
        self.seed_size: int = ts.get("size", 0)

        # ---- backward / forward ----
        bw = dep.get("backward") or {}
        fw = dep.get("forward") or {}
        self.backward_objects: Set[str] = set(bw.get("objects") or [])
        self.backward_leaf_objects: Set[str] = set(bw.get("leaf_objects") or [])
        self.backward_instructions: Set[str] = {norm_hex(pc) for pc in (bw.get("instructions") or [])}
        self.backward_leaf_instructions: Set[str] = {norm_hex(pc) for pc in (bw.get("leaf_instructions") or [])}
        self.forward_objects: Set[str] = set(fw.get("objects") or [])
        self.forward_sink_objects: Set[str] = set(fw.get("sink_objects") or [])

        # ---- instruction_details ----
        raw_instr = dep.get("instruction_details") or {}
        self.instruction_details: Dict[str, dict] = {}
        for k, v in raw_instr.items():
            self.instruction_details[norm_hex(k)] = v

        # ---- object_details ----
        self.object_details: Dict[str, dict] = dep.get("object_details") or {}

        # ---- Detect CRT code range ----
        self._detect_crt_range()

        # ---- build derived indices ----
        self._build_backward_edges()
        self._build_object_pc_index()
        self._build_pc_object_index()
        self._build_register_fanout()
        self._build_stack_dedup_groups()
        self._detect_prologue_epilogue_pcs()

        # caches
        self._bw_dist_cache: Dict[str, Optional[int]] = {}
        self._bw_dist_computed = False
        self._print_only: Optional[Set[str]] = None

    # ---- CRT detection ----

    def _detect_crt_range(self):
        self.crt_pcs: Set[str] = set()
        pcs_sorted = sorted(self.instruction_details.keys(), key=lambda x: int(x, 16))
        if not pcs_sorted:
            return
        first_user_func_pc = None
        for i, pc in enumerate(pcs_sorted):
            idet = self.instruction_details[pc]
            dis = (idet.get("disasm") or "").lower()
            if "push rbp" in dis:
                if i + 1 < len(pcs_sorted):
                    next_idet = self.instruction_details.get(pcs_sorted[i + 1], {})
                    next_dis = (next_idet.get("disasm") or "").lower()
                    if "mov rbp, rsp" in next_dis:
                        first_user_func_pc = pc
                        break
        if first_user_func_pc:
            threshold = int(first_user_func_pc, 16)
            for pc in pcs_sorted:
                if int(pc, 16) < threshold:
                    self.crt_pcs.add(pc)

    def is_crt_pc(self, pc_hex: str) -> bool:
        return pc_hex in self.crt_pcs

    # ---- prologue/epilogue detection (v2.4) ----

    def _detect_prologue_epilogue_pcs(self):
        """
        识别所有函数序言/尾声指令 PC，并记录描述。
        使用两轮扫描：
        1. 找到所有函数入口 (push rbp; mov rbp, rsp 模式)
        2. 从每个入口向后扫描，标记序言指令
           (sub rsp / 参数保存 / callee-saved push)
        3. 从函数末尾向前扫描，标记尾声指令
           (add rsp / callee-saved pop)
        """
        self.prologue_epilogue_pcs: Dict[str, str] = {}  # pc -> description

        pcs_sorted = sorted(self.instruction_details.keys(), key=lambda x: int(x, 16))

        for pc in pcs_sorted:
            mn = self._get_mnemonic_at(pc)
            dis = self._get_disasm_at(pc)
            is_pe, desc = is_prologue_epilogue_instruction(mn, dis)
            if is_pe:
                self.prologue_epilogue_pcs[pc] = desc

    def is_prologue_epilogue_pc(self, pc_hex: str) -> bool:
        return pc_hex in self.prologue_epilogue_pcs

    def get_prologue_epilogue_desc(self, pc_hex: str) -> Optional[str]:
        return self.prologue_epilogue_pcs.get(pc_hex)

    def _get_disasm_at(self, pc_hex: str) -> str:
        idet = self.instruction_details.get(pc_hex, {})
        return idet.get("disasm") or ""

    def _get_mnemonic_at(self, pc_hex: str) -> str:
        dis = self._get_disasm_at(pc_hex)
        if dis:
            parts = dis.strip().split()
            if parts:
                return parts[0].lower()
        return ""

    # ---- backward edge extraction ----

    def _build_backward_edges(self):
        self._backward_edges: Dict[str, Set[str]] = {}
        for obj_id, odet in self.object_details.items():
            if obj_id not in self.backward_objects:
                continue
            parents = set()
            for p in safe_list(odet.get("direct_parents")):
                if isinstance(p, str):
                    parents.add(p)
            self._backward_edges[obj_id] = parents

    # ---- object -> PC index ----

    def _build_object_pc_index(self):
        self.obj_direct_pcs: Dict[str, Set[str]] = defaultdict(set)
        for obj_id, odet in self.object_details.items():
            for key in ("defined_by", "used_by", "addr_used_by", "ctrl_used_by"):
                for pc in safe_list(odet.get(key)):
                    if isinstance(pc, str):
                        self.obj_direct_pcs[obj_id].add(norm_hex(pc))
            opc = odet.get("occurrence_pc")
            if opc and isinstance(opc, str):
                self.obj_direct_pcs[obj_id].add(norm_hex(opc))
        for pc_hex, idet in self.instruction_details.items():
            for key in ("use_objects", "def_objects", "addr_objects", "immediates"):
                for obj in safe_list(idet.get(key)):
                    if isinstance(obj, str):
                        self.obj_direct_pcs[obj].add(pc_hex)

    # ---- PC -> objects index ----

    def _build_pc_object_index(self):
        self.pc_direct_objects: Dict[str, Set[str]] = defaultdict(set)
        for pc_hex, idet in self.instruction_details.items():
            for key in ("use_objects", "def_objects", "addr_objects", "immediates"):
                for obj in safe_list(idet.get(key)):
                    if isinstance(obj, str):
                        self.pc_direct_objects[pc_hex].add(obj)
        self.pc_controlled_by: Dict[str, Set[str]] = defaultdict(set)
        for pc_hex, idet in self.instruction_details.items():
            for ctrl_pc in safe_list(idet.get("controlled_by")):
                if isinstance(ctrl_pc, str):
                    self.pc_controlled_by[pc_hex].add(norm_hex(ctrl_pc))

    # ---- register fanout ----

    def _build_register_fanout(self):
        self.register_fanout: Dict[str, int] = {}
        for obj_id, odet in self.object_details.items():
            if not is_register_object(obj_id):
                continue
            n_def = len(safe_list(odet.get("defined_by")))
            n_use = len(safe_list(odet.get("used_by")))
            self.register_fanout[obj_id] = n_def + n_use

    def get_register_fanout(self, obj_id: str) -> int:
        return self.register_fanout.get(obj_id, 0)

    # ---- stack dedup ----

    def _build_stack_dedup_groups(self):
        self.stack_dedup_representatives: Dict[str, str] = {}
        self.stack_dedup_groups: Dict[str, List[str]] = defaultdict(list)

        stack_objs = []
        for obj_id in self.backward_objects:
            if not is_stack_object(obj_id):
                continue
            odet = self.object_details.get(obj_id, {})
            parsed = parse_stack_object(obj_id)
            if not parsed:
                continue
            n_def = len(safe_list(odet.get("defined_by")))
            n_use = len(safe_list(odet.get("used_by")))
            tags = tuple(sorted(odet.get("semantic_tags") or []))
            def_pcs = frozenset(norm_hex(pc) for pc in safe_list(odet.get("defined_by")))
            stack_objs.append((obj_id, parsed["base"], parsed["offset"],
                               n_def, n_use, tags, def_pcs))

        groups: Dict[tuple, List[tuple]] = defaultdict(list)
        for item in stack_objs:
            oid, base, offset, n_def, n_use, tags, def_pcs = item
            key = (base, n_def, n_use, tags, def_pcs)
            groups[key].append(item)

        for key, members in groups.items():
            if len(members) <= 1:
                for item in members:
                    self.stack_dedup_representatives[item[0]] = item[0]
                    self.stack_dedup_groups[item[0]].append(item[0])
                continue
            members.sort(key=lambda x: x[2])
            representative = members[0][0]
            for item in members:
                self.stack_dedup_representatives[item[0]] = representative
                self.stack_dedup_groups[representative].append(item[0])

    def is_stack_representative(self, obj_id: str) -> bool:
        rep = self.stack_dedup_representatives.get(obj_id, obj_id)
        return rep == obj_id

    def get_stack_group_size(self, obj_id: str) -> int:
        rep = self.stack_dedup_representatives.get(obj_id, obj_id)
        return len(self.stack_dedup_groups.get(rep, [obj_id]))

    # ---- backward distance ----

    def backward_distance_to_seed(self, obj_id: str) -> Optional[int]:
        if not self._bw_dist_computed:
            self._compute_all_backward_distances()
        return self._bw_dist_cache.get(obj_id)

    def _compute_all_backward_distances(self):
        self._bw_dist_computed = True
        from collections import deque
        queue = deque()
        queue.append((self.seed_object, 0))
        self._bw_dist_cache[self.seed_object] = 0
        visited = {self.seed_object}
        while queue:
            node, dist = queue.popleft()
            for parent in self._backward_edges.get(node, set()):
                if parent not in visited and parent in self.backward_objects:
                    visited.add(parent)
                    self._bw_dist_cache[parent] = dist + 1
                    queue.append((parent, dist + 1))

    def is_backward_leaf(self, obj_id: str) -> bool:
        return obj_id in self.backward_leaf_objects

    # ---- print-only objects ----

    def is_print_only_object(self, obj_id: str) -> bool:
        if self._print_only is None:
            self._build_print_only()
        return obj_id in self._print_only

    def _build_print_only(self):
        self._print_only = set()
        print_call_pcs = set()
        for pc_hex, idet in self.instruction_details.items():
            dis = (idet.get("disasm") or "").lower()
            if dis.startswith("call"):
                if any(kw in dis for kw in ("print", "printf", "puts", "write", "fprintf",
                                            "sprintf", "snprintf", "vprintf", "cout")):
                    print_call_pcs.add(pc_hex)
        if not print_call_pcs:
            return
        for obj_id in self.object_details:
            dpcs = self.obj_direct_pcs.get(obj_id, set())
            if dpcs and dpcs <= print_call_pcs:
                self._print_only.add(obj_id)

    # ---- helpers ----

    def get_object_semantic_tags(self, obj_id: str) -> List[str]:
        odet = self.object_details.get(obj_id, {})
        return list(odet.get("semantic_tags") or [])

    def get_disasm_at(self, pc_hex: str) -> str:
        return self._get_disasm_at(pc_hex)

    def get_mnemonic_at(self, pc_hex: str) -> str:
        return self._get_mnemonic_at(pc_hex)

    def get_representative_pcs(self, obj_id: str, limit: int = 5) -> List[str]:
        dpcs = sorted(self.obj_direct_pcs.get(obj_id, set()))
        return dpcs[:limit]

    def get_representative_disasm(self, obj_id: str, limit: int = 3) -> List[str]:
        lines = []
        for pc in sorted(self.obj_direct_pcs.get(obj_id, set())):
            dis = self.get_disasm_at(pc)
            if dis:
                lines.append(f"{pc}: {dis}")
            if len(lines) >= limit:
                break
        return lines

    def has_only_crt_pcs(self, obj_id: str) -> bool:
        dpcs = self.obj_direct_pcs.get(obj_id, set())
        if not dpcs:
            return False
        return all(self.is_crt_pc(pc) for pc in dpcs)

    def has_any_non_crt_pc(self, obj_id: str) -> bool:
        dpcs = self.obj_direct_pcs.get(obj_id, set())
        return any(not self.is_crt_pc(pc) for pc in dpcs)

    def get_non_crt_pcs(self, obj_id: str) -> Set[str]:
        dpcs = self.obj_direct_pcs.get(obj_id, set())
        return {pc for pc in dpcs if not self.is_crt_pc(pc)}


# ---------------------------------------------------------------------------
# CausalCandidateFilter
# ---------------------------------------------------------------------------

class CausalCandidateFilter:

    def __init__(self, model: DependencyModel):
        self.m = model

    # ================================================================
    # imm_occurrence structural filtering
    # ================================================================

    def _is_trivial_imm(self, obj_id: str) -> Tuple[bool, str]:
        parsed = parse_imm_occurrence(obj_id)
        if parsed is None:
            return False, ""

        component = parsed["component"]
        value = parsed["value"]
        pc_hex = parsed["pc"]
        signed_val = to_signed_64(value)

        if component == "mem_scale" and value == 1:
            return True, "恒等 scale 因子 (×1)，不具备独立变异价值"
        if component == "mem_scale" and value == 0:
            return True, "scale=0 无变异价值"
        if component == "mem_disp" and value == 0:
            return True, "零偏移量，不改变寻址结果"

        if component == "mem_disp":
            if -256 <= signed_val < 0:
                disasm = self.m.get_disasm_at(pc_hex).lower()
                if "rbp" in disasm or "ebp" in disasm:
                    return True, "栈帧局部变量偏移 (rbp-relative)，变异只会破坏栈帧布局"
            if 0 < signed_val <= 256:
                disasm = self.m.get_disasm_at(pc_hex).lower()
                if "rbp" in disasm or "ebp" in disasm:
                    return True, "栈帧局部变量偏移 (rbp+offset)，变异只会破坏栈帧布局"

        if component == "mem_disp" and value > 0x100000:
            disasm = self.m.get_disasm_at(pc_hex).lower()
            mn = self.m.get_mnemonic_at(pc_hex)
            if "rip" in disasm and mn in ("call", "jmp"):
                return True, "GOT/PLT 重定位偏移 (rip-relative call/jmp)，变异导致调用非法地址"

        if component == "mem_disp":
            mn = self.m.get_mnemonic_at(pc_hex)
            disasm = self.m.get_disasm_at(pc_hex).lower()
            if mn == "lea" and "rip" in disasm and value > 0x100:
                return True, "rip-relative lea 地址加载偏移，变异导致指向无效数据区域"

        tags = set(self.m.get_object_semantic_tags(obj_id))
        if "structural_abi_constant" in tags:
            return True, "ABI 结构性常量，不适合作为语义变异对象"
        if "stack_alignment_constant" in tags:
            return True, "栈对齐常量"

        return False, ""

    def _is_branch_target_imm(self, obj_id: str) -> Tuple[bool, str]:
        parsed = parse_imm_occurrence(obj_id)
        if parsed is None:
            return False, ""
        if parsed["component"] == "operand_imm":
            pc_hex = parsed["pc"]
            mn = self.m.get_mnemonic_at(pc_hex)
            if mn and (mn.startswith("j") or mn.startswith("loop")):
                return True, "分支目标地址应通过 branch_flip/branch_replace 变异，非立即数直接替换"
            if mn == "call":
                disasm = self.m.get_disasm_at(pc_hex).lower()
                if "call 0x" in disasm or "call  0x" in disasm:
                    return True, "call 直接目标地址应通过 call_skip_or_replace 变异，非立即数直接替换"
        return False, ""

    # ================================================================
    # Semantic role inference
    # ================================================================

    def _infer_semantic_roles(self, obj_id: str) -> Tuple[List[str], List[str]]:
        odet = self.m.object_details.get(obj_id, {})
        tags = set(odet.get("semantic_tags") or [])
        direct_roles = list(tags)
        contextual_roles = []

        if obj_id in self.m.backward_objects:
            contextual_roles.append("backward_related")
            if self.m.is_backward_leaf(obj_id):
                contextual_roles.append("backward_leaf")
        if obj_id in self.m.forward_objects:
            contextual_roles.append("forward_related")

        dist = self.m.backward_distance_to_seed(obj_id)
        if dist is not None and dist <= 3:
            direct_roles.append("near_seed_path")

        pcs = self.m.get_non_crt_pcs(obj_id) if self.m.has_any_non_crt_pc(obj_id) \
              else self.m.obj_direct_pcs.get(obj_id, set())

        for pc in pcs:
            idet = self.m.instruction_details.get(pc, {})
            mn = self.m.get_mnemonic_at(pc)
            disasm = self.m.get_disasm_at(pc).lower()

            use_objs = set(safe_list(idet.get("use_objects")))
            def_objs = set(safe_list(idet.get("def_objects")))
            addr_objs = set(safe_list(idet.get("addr_objects")))

            if mn in ("cmp", "test") and obj_id in use_objs:
                if "comparison_operand" not in direct_roles:
                    direct_roles.append("comparison_operand")
                if "comparison_related" not in direct_roles:
                    direct_roles.append("comparison_related")

            if mn.startswith("j") and mn != "jmp":
                if "branch_related" not in direct_roles:
                    direct_roles.append("branch_related")

            if mn == "call":
                if "call_related" not in direct_roles:
                    direct_roles.append("call_related")

            if obj_id in addr_objs:
                if "address_related" not in direct_roles:
                    direct_roles.append("address_related")

            if "[" in disasm:
                if obj_id in use_objs or obj_id in def_objs:
                    if "memory_related" not in direct_roles:
                        direct_roles.append("memory_related")

            if obj_id in def_objs and mn not in ("cmp", "test"):
                if "value_defined" not in direct_roles:
                    direct_roles.append("value_defined")

            if mn in ("add", "sub", "imul", "mul", "shl", "shr", "sar", "sal",
                       "and", "or", "xor", "inc", "dec", "neg", "not"):
                if obj_id in use_objs or obj_id in def_objs:
                    if "arithmetic_related" not in direct_roles:
                        direct_roles.append("arithmetic_related")

        return uniq_keep_order(direct_roles), uniq_keep_order(contextual_roles)

    # ================================================================
    # Mutation value assessment
    # ================================================================

    def _has_mutation_value(self, obj_id: str, direct_roles: List[str],
                            tags: Set[str]) -> Tuple[bool, str]:
        role_set = set(direct_roles)

        high_value_roles = {
            "comparison_related", "comparison_operand", "comparison_constant",
            "branch_condition_operand", "branch_semantic_constant",
            "store_constant", "timing_threshold_constant", "cache_threshold_constant",
            "seed_adjacent_index_or_scale_constant",
            "control_related", "memory_value_operand",
            "arithmetic_related",
        }
        if high_value_roles & role_set:
            return True, "参与比较/条件/关键常量/算术运算"

        high_value_tags = {
            "comparison_constant", "branch_semantic_constant", "store_constant",
            "timing_threshold", "cache_threshold", "generic_arithmetic_constant",
            "program_semantic_constant", "loop_bound_constant",
        }
        if high_value_tags & tags:
            return True, "分析器标记为高价值语义常量"

        if is_var_object(obj_id):
            return True, "具备变量语义"
        if is_stack_object(obj_id):
            return True, "具备栈变量语义"

        if is_register_object(obj_id):
            meaningful_reg_roles = {
                "control_related", "branch_condition_operand", "comparison_related",
                "comparison_operand", "memory_value_operand", "near_seed_path",
                "arithmetic_related",
            }
            meaningful_tags = {"address_base", "address_index"}
            if (meaningful_reg_roles & role_set) or (meaningful_tags & tags):
                return True, "寄存器参与有意义的语义角色"
            if is_structural_register(obj_id):
                return False, "纯栈/帧指针结构用途"
            return False, "普通寄存器无高价值语义角色"

        if is_imm_object(obj_id):
            pure_addr_roles = {"address_related", "memory_related", "address_component_usage"}
            contextual_meta = {"backward_related", "backward_leaf", "forward_related",
                               "near_seed_path", "value_defined"}
            substantial = role_set - pure_addr_roles - contextual_meta
            if not substantial and not (tags - {"address_base", "address_index"}):
                if "near_seed_path" in role_set:
                    return True, "立即数靠近 seed 路径"
                return False, "纯地址机械组件 imm，无独立语义变异价值"

        return True, "默认通过"

    # ================================================================
    # Strong admission evaluation
    # ================================================================

    def _evaluate_strong_admission(self, obj_id: str) -> Dict[str, Any]:
        reasons = []
        qualification = []
        root_evidence = []
        actions = []

        odet = self.m.object_details.get(obj_id, {})
        tags = set(odet.get("semantic_tags") or [])
        direct_roles, contextual_roles = self._infer_semantic_roles(obj_id)
        all_roles = uniq_keep_order(direct_roles + contextual_roles)
        direct_pcs = self.m.obj_direct_pcs.get(obj_id, set())
        role_set = set(direct_roles)

        non_crt_pcs = self.m.get_non_crt_pcs(obj_id)
        anchor_pcs = set()
        for pc in non_crt_pcs:
            if pc in self.m.instruction_details:
                anchor_pcs.add(pc)

        dist = self.m.backward_distance_to_seed(obj_id)

        # ========== Exclusion rules ==========

        if obj_id not in self.m.backward_objects:
            reasons.append("对象不在 backward 强相关集合中")

        if obj_id == self.m.seed_object:
            reasons.append("seed 本身是分析中心，不作为首选上游变异对象")

        if is_noise_object(obj_id):
            if obj_id.lower() == "reg:rip":
                reasons.append("rip 是执行推进副产物")
            else:
                reasons.append("对象语义不稳定")

        if self.m.is_print_only_object(obj_id):
            reasons.append("对象只出现在打印/观测调用上下文")

        if is_flag_object(obj_id):
            reasons.append("flags 更适合作为分支语义解释，不作为首选直接对象变异入口")

        if is_mem_object(obj_id):
            reasons.append("mem:* 具体内存地址对象不可在汇编层直接变异，需通过变异其上游地址计算或值写入来间接影响")

        if not non_crt_pcs:
            if direct_pcs:
                reasons.append("对象所有 direct PC 均在 CRT 启动代码区间内")
            else:
                reasons.append("对象缺少 direct 对象-PC 映射")

        if non_crt_pcs and not anchor_pcs:
            reasons.append("对象在用户代码中缺少可变异锚点")

        if direct_pcs and self.m.has_only_crt_pcs(obj_id):
            if "对象所有 direct PC 均在 CRT 启动代码区间内" not in reasons:
                reasons.append("对象仅存在于 CRT 启动代码中")

        if is_imm_object(obj_id):
            trivial, trivial_reason = self._is_trivial_imm(obj_id)
            if trivial:
                reasons.append(trivial_reason)
            branch_target, bt_reason = self._is_branch_target_imm(obj_id)
            if branch_target:
                reasons.append(bt_reason)
            parsed = parse_imm_occurrence(obj_id)
            if parsed and self.m.is_crt_pc(parsed["pc"]):
                reasons.append("立即数位于 CRT 启动代码中")

        if is_register_object(obj_id) and not is_flag_object(obj_id):
            if is_structural_register(obj_id):
                reasons.append("纯栈/帧指针结构用途")
            else:
                critical_reg_roles = {
                    "comparison_related", "comparison_operand",
                    "arithmetic_related", "near_seed_path",
                }
                critical_tags = {"address_base", "address_index"}
                if not ((critical_reg_roles & role_set) or (critical_tags & tags)):
                    reasons.append("寄存器无高价值语义角色")

        if is_stack_object(obj_id):
            if not self.m.is_stack_representative(obj_id):
                group_size = self.m.get_stack_group_size(obj_id)
                rep = self.m.stack_dedup_representatives.get(obj_id, obj_id)
                reasons.append(f"同质化栈变量去重（组大小 {group_size}），代表为 {rep}")

        has_value, value_reason = self._has_mutation_value(obj_id, direct_roles, tags)
        if not has_value:
            reasons.append(value_reason)

        if reasons:
            return {
                "admitted": False,
                "reasons": reasons,
                "direct_roles": direct_roles,
                "contextual_roles": contextual_roles,
                "roles": all_roles,
                "tags": list(tags),
            }

        # ========== Admission evidence ==========

        qualification.append("对象位于 backward 强相关集合中")
        root_evidence.append("backward 依赖集合成员，属于污染源上游对象")

        if dist is not None:
            qualification.append(f"backward 距离约为 {dist}")
            root_evidence.append(f"到 seed 的最短 backward 距离约为 {dist}")

        if self.m.is_backward_leaf(obj_id):
            qualification.append("backward 叶子节点，上游根候选")
            root_evidence.append("backward 叶子节点")

        qualification.append("有稳定的用户代码变异锚点")

        if {"comparison_related", "comparison_operand"} & role_set:
            qualification.append("参与比较/条件判断")
            root_evidence.append("直接参与比较")
        if {"address_related"} & role_set or {"address_base", "address_index"} & tags:
            qualification.append("参与地址形成")
            root_evidence.append("参与地址形成")
        if {"memory_related"} & role_set:
            qualification.append("参与内存读写")
            root_evidence.append("参与内存操作")
        if {"arithmetic_related"} & role_set:
            qualification.append("参与算术运算")
            root_evidence.append("参与算术运算")
        if "near_seed_path" in role_set:
            qualification.append("在污染源附近路径上")

        role_class = "generic_mutable_object"
        if {"comparison_operand", "comparison_related"} & role_set:
            role_class = "comparison_participant"
        elif is_var_object(obj_id):
            role_class = "variable"
        elif is_stack_object(obj_id):
            role_class = "stack_variable"
        elif "arithmetic_related" in role_set:
            role_class = "arithmetic_participant"
        elif is_register_object(obj_id):
            role_class = "register_carrier"

        if {"comparison_constant", "timing_threshold", "cache_threshold"} & tags:
            role_class = "key_constant"
        if {"loop_bound_constant"} & tags:
            role_class = "loop_bound_constant"
        if "generic_arithmetic_constant" in tags:
            role_class = "arithmetic_constant"

        direct_mutation_preferred = True
        deletion_candidate_only = False

        if is_register_object(obj_id):
            direct_mutation_preferred = False
            deletion_candidate_only = True
            actions.append("containing_instruction_deletion")
            actions.append("containing_instruction_operand_mutation")
        elif is_imm_object(obj_id):
            parsed = parse_imm_occurrence(obj_id)
            if parsed:
                if parsed["component"] == "operand_imm":
                    direct_mutation_preferred = True
                    actions.append("immediate_value_mutation")
                elif parsed["component"] == "mem_disp":
                    if parsed["value"] > 0x1000:
                        direct_mutation_preferred = True
                        actions.append("displacement_mutation")
                    else:
                        direct_mutation_preferred = False
                        deletion_candidate_only = True
                        actions.append("containing_instruction_deletion")
                else:
                    direct_mutation_preferred = True
                    actions.append("immediate_value_mutation")
            else:
                actions.append("immediate_value_mutation")
        elif is_var_object(obj_id) or is_stack_object(obj_id):
            direct_mutation_preferred = True
            actions.append("operand_mutation")
            actions.append("instruction_deletion")
        else:
            actions.append("operand_mutation")

        return {
            "admitted": True,
            "reasons": [],
            "role_class": role_class,
            "direct_mutation_preferred": direct_mutation_preferred,
            "deletion_candidate_only": deletion_candidate_only,
            "actions": actions,
            "qualification_reasons": qualification,
            "root_evidence": root_evidence,
            "roles": all_roles,
            "direct_roles": direct_roles,
            "contextual_roles": contextual_roles,
            "tags": list(tags),
            "anchor_pcs": sorted(anchor_pcs),
            "backward_distance": dist,
        }

    # ================================================================
    # Build strong causal objects
    # ================================================================

    def build_strong_causal_objects(self) -> Tuple[List[dict], List[dict]]:
        candidates = []
        excluded = []

        for obj_id in sorted(self.m.object_details.keys()):
            ev = self._evaluate_strong_admission(obj_id)

            if not ev["admitted"]:
                excluded.append({
                    "object_id": obj_id,
                    "object_type": object_type(obj_id),
                    "exclusion_reasons": ev["reasons"],
                })
                continue

            context_pcs = sorted(
                set(self.m.obj_direct_pcs.get(obj_id, set())) - set(ev["anchor_pcs"])
            )

            candidates.append(asdict(StrongCausalObject(
                object_id=obj_id,
                object_type=object_type(obj_id),
                causal_role_class=ev["role_class"],
                direct_mutation_preferred=ev["direct_mutation_preferred"],
                deletion_candidate_only=ev.get("deletion_candidate_only", False),
                recommended_actions=ev["actions"],
                semantic_tags=ev.get("tags", []),
                direct_semantic_roles=ev["direct_roles"],
                contextual_semantic_roles=ev["contextual_roles"],
                qualification_reasons=uniq_keep_order(ev["qualification_reasons"]),
                root_evidence=uniq_keep_order(ev["root_evidence"]),
                rationale=uniq_keep_order(ev["qualification_reasons"]),
                representative_pcs=self.m.get_representative_pcs(obj_id),
                representative_disasm=self.m.get_representative_disasm(obj_id),
                related_anchor_pcs=ev["anchor_pcs"],
                contextual_related_pcs=context_pcs,
                source_refs=[],
                backward_distance=ev.get("backward_distance"),
            )))

        candidates = self._demote_addr_components(candidates, excluded)
        return candidates, excluded

    def _demote_addr_components(self, candidates: List[dict],
                                excluded: List[dict]) -> List[dict]:
        pc_has_semantic = defaultdict(bool)
        pc_imm_addr_indices = defaultdict(list)

        for i, c in enumerate(candidates):
            oid = c["object_id"]
            for pc in c.get("related_anchor_pcs", []):
                if is_var_object(oid) or is_stack_object(oid):
                    pc_has_semantic[pc] = True
                elif is_imm_object(oid):
                    parsed = parse_imm_occurrence(oid)
                    if parsed and parsed["component"] in ("mem_disp", "mem_scale"):
                        pc_imm_addr_indices[pc].append(i)

        demote_indices = set()
        for pc, has_sem in pc_has_semantic.items():
            if has_sem and pc in pc_imm_addr_indices:
                for idx in pc_imm_addr_indices[pc]:
                    demote_indices.add(idx)

        remaining = []
        for i, c in enumerate(candidates):
            if i in demote_indices:
                excluded.append({
                    "object_id": c["object_id"],
                    "object_type": c["object_type"],
                    "exclusion_reasons": [
                        "同锚点已有高语义层对象 (var/stack)，地址分量 imm 降级为 excluded"
                    ],
                })
            else:
                remaining.append(c)
        return remaining

    # ================================================================
    # Build assembly anchors — v2.4: refined tier + prologue/epilogue
    # ================================================================

    def build_assembly_anchors(self, strong_objects: List[dict]) -> List[dict]:
        strong_ids = {o["object_id"] for o in strong_objects}
        full_mutation_ids = {
            o["object_id"] for o in strong_objects
            if o.get("direct_mutation_preferred", False)
            and not o.get("deletion_candidate_only", False)
        }
        deletion_only_ids = strong_ids - full_mutation_ids

        # 为 tier 分级提供对象类型快查
        var_ids = {oid for oid in full_mutation_ids if is_var_object(oid)}
        imm_operand_ids = set()
        for oid in full_mutation_ids:
            if is_imm_object(oid):
                parsed = parse_imm_occurrence(oid)
                if parsed and parsed["component"] == "operand_imm":
                    imm_operand_ids.add(oid)
        stack_ids = {oid for oid in full_mutation_ids if is_stack_object(oid)}

        anchors = []

        for pc_hex in sorted(self.m.instruction_details.keys()):
            if self.m.is_crt_pc(pc_hex):
                continue

            idet = self.m.instruction_details[pc_hex]
            mnemonic = self.m.get_mnemonic_at(pc_hex)
            disasm = self.m.get_disasm_at(pc_hex)

            if not disasm:
                continue

            if self._is_pure_structural_instruction(mnemonic, disasm):
                continue

            is_type_conv, _ = is_type_conversion_instruction(disasm)

            # v2.4: detect prologue/epilogue
            is_pe = self.m.is_prologue_epilogue_pc(pc_hex)
            pe_desc = self.m.get_prologue_epilogue_desc(pc_hex)

            direct_here = self.m.pc_direct_objects.get(pc_hex, set())
            causal_full = sorted(direct_here & full_mutation_ids)
            causal_del = sorted(direct_here & deletion_only_ids)
            explanatory_objects_here = sorted(
                direct_here - strong_ids - {o for o in direct_here if is_noise_object(o)}
            )

            # 判断当前 PC 是否是 seed 指令
            # DependencyModel 已经在初始化时从 taint_source.seed_instruction_pcs 读取并存储
            is_seed_pc = pc_hex in self.m.seed_pcs

            # anchor 必须有 full-mutation 对象
            if not causal_full and not is_seed_pc:
                continue

            if is_type_conv:
                has_non_reg_full = any(not is_register_object(o) for o in causal_full)
                if not has_non_reg_full and not is_seed_pc:
                    continue

            all_causal = sorted(set(causal_full) | set(causal_del))

            knds = self._classify_anchor_kinds(mnemonic, disasm, all_causal)
            if not knds:
                continue

            # v2.4: 计算此 anchor 上各类对象的存在情况
            has_var = bool(set(causal_full) & var_ids)
            has_imm_operand = bool(set(causal_full) & imm_operand_ids)
            has_stack_only = (
                bool(set(causal_full) & stack_ids)
                and not has_var
                and not has_imm_operand
                and not any(is_register_object(o) and o in full_mutation_ids for o in causal_full)
            )

            tier = self._determine_anchor_tier_v24(
                knds, mnemonic, disasm, causal_full,
                has_var=has_var,
                has_imm_operand=has_imm_operand,
                has_stack_only=has_stack_only,
                is_prologue_epilogue=is_pe,
            )

            mutations = self._recommend_mutations(knds, mnemonic)

            rationale = []
            if is_pe:
                rationale.append(f"函数序言/尾声指令：{pe_desc}")
            else:
                rationale.append("该指令涉及强相关可变异对象")

            if "comparison_anchor" in knds:
                rationale.append("参与比较，变异后可能改变路径")
            if "branch_anchor" in knds:
                rationale.append("条件转移锚点")
            if "address_calc_anchor" in knds:
                rationale.append("参与地址计算")
            if "memory_value_anchor" in knds:
                rationale.append("涉及内存值读写")
            if "immediate_anchor" in knds:
                rationale.append("含关键立即数")
            if "call_anchor" in knds:
                rationale.append("调用锚点")
            if "arithmetic_anchor" in knds:
                rationale.append("算术运算锚点")

            func_name = idet.get("function") or idet.get("func")
            src_file = idet.get("source_file") or idet.get("src_file")
            src_line = idet.get("source_line") or idet.get("src_line")

            anchors.append(asdict(AnchorCandidate(
                pc=pc_hex,
                mnemonic=mnemonic,
                disasm=disasm,
                function=func_name,
                source_file=src_file,
                source_line=src_line,
                anchor_tier=tier,
                anchor_kinds=sorted(knds),
                recommended_mutations=sorted(mutations),
                causal_objects=all_causal,
                explanatory_objects=explanatory_objects_here,
                related_strong_objects=[],
                rationale=rationale,
                is_prologue_epilogue=is_pe,
                prologue_epilogue_desc=pe_desc,
            )))

        return anchors

    def _is_pure_structural_instruction(self, mnemonic: str, disasm: str) -> bool:
        dl = disasm.lower()
        if mnemonic == "push" and "rbp" in dl:
            return True
        if mnemonic == "pop" and "rbp" in dl:
            return True
        if mnemonic == "mov" and (
            "rbp, rsp" in dl or "rsp, rbp" in dl or
            "ebp, esp" in dl or "esp, ebp" in dl):
            return True
        if mnemonic in ("ret", "retn", "leave"):
            return True
        if mnemonic in ("nop", "endbr64", "endbr32", "int3", "ud2"):
            return True
        return False

    def _classify_anchor_kinds(self, mnemonic: str, disasm: str,
                                causal_objects: List[str]) -> Set[str]:
        kinds = set()
        dl = disasm.lower()
        has_mem_bracket = "[" in dl

        if mnemonic in ("cmp", "test"):
            kinds.add("comparison_anchor")
        if mnemonic.startswith("j"):
            kinds.add("branch_anchor")
        if mnemonic == "call":
            kinds.add("call_anchor")
        if has_mem_bracket:
            kinds.add("address_calc_anchor")
            if mnemonic in ("mov", "movzx", "movsx", "lea", "add", "sub",
                            "and", "or", "xor", "shl", "shr", "sar",
                            "imul", "mul", "div", "idiv", "inc", "dec",
                            "cmp", "test", "push", "pop", "movaps",
                            "movdqa", "movdqu", "movss", "movsd",
                            "movsxd"):
                kinds.add("memory_value_anchor")

        for oid in causal_objects:
            if is_imm_object(oid):
                parsed = parse_imm_occurrence(oid)
                if parsed and parsed["component"] == "operand_imm":
                    kinds.add("immediate_anchor")
                    break

        if mnemonic in ("add", "sub", "imul", "mul", "shl", "shr", "sar",
                        "and", "or", "xor", "inc", "dec", "neg", "not"):
            kinds.add("arithmetic_anchor")

        if not kinds and causal_objects:
            kinds.add("generic_anchor")

        return kinds

    def _determine_anchor_tier_v24(self, kinds: Set[str], mnemonic: str,
                                    disasm: str, full_mutation_objects: List[str],
                                    *, has_var: bool, has_imm_operand: bool,
                                    has_stack_only: bool,
                                    is_prologue_epilogue: bool) -> str:
        """
        v2.4 精细化 tier 分级：

        primary:
          - 比较指令 (cmp/test) 且含 full-mutation 对象
          - 条件分支指令
          - call 指令
          - 含 operand_imm 类型的关键立即数
          - 涉及 var 对象的内存操作（如 movzx eax, [rax] 涉及 var:array1）
          - 核心算术 (shl/shr/and/or/xor) 且含 operand_imm 或 var

        secondary:
          - 仅涉及 stack 对象的普通 mov 读写
          - 地址计算 (lea) 无 var/imm_operand
          - 一般算术仅涉及 stack

        contextual:
          - 函数序言/尾声指令（参数保存、callee-saved、栈帧分配等）
          - generic_anchor
          - 仅剩余情况
        """

        # 函数序言/尾声 → 最低优先级 contextual
        if is_prologue_epilogue:
            return "contextual"

        # --- primary 条件 ---
        # 比较指令
        if "comparison_anchor" in kinds:
            return "primary"
        # 条件分支
        if "branch_anchor" in kinds:
            return "primary"
        # call
        if "call_anchor" in kinds:
            return "primary"
        # 含关键 operand_imm 立即数
        if "immediate_anchor" in kinds and has_imm_operand:
            return "primary"
        # 涉及 var 对象的内存操作
        if "memory_value_anchor" in kinds and has_var:
            return "primary"
        # 核心算术且含 operand_imm 或 var
        if "arithmetic_anchor" in kinds and (has_imm_operand or has_var):
            return "primary"

        # --- secondary 条件 ---
        # 算术指令涉及 stack
        if "arithmetic_anchor" in kinds:
            return "secondary"
        # 内存操作涉及 stack（普通 mov 读写）
        if "memory_value_anchor" in kinds:
            return "secondary"
        # 地址计算
        if "address_calc_anchor" in kinds:
            return "secondary"

        # --- contextual（其余） ---
        return "contextual"

    def _recommend_mutations(self, kinds: Set[str], mnemonic: str) -> Set[str]:
        mutations = set()
        if "comparison_anchor" in kinds:
            mutations.add("operand_mutation")
            mutations.add("opcode_replacement")
            mutations.add("instruction_deletion")
        if "branch_anchor" in kinds:
            mutations.add("branch_flip_or_replace")
            mutations.add("instruction_deletion")
        if "call_anchor" in kinds:
            mutations.add("call_skip_or_replace")
        if "memory_value_anchor" in kinds:
            mutations.add("operand_mutation")
            mutations.add("instruction_deletion")
        if "immediate_anchor" in kinds:
            mutations.add("immediate_value_mutation")
        if "arithmetic_anchor" in kinds:
            mutations.add("operand_mutation")
            mutations.add("opcode_replacement")
        if "address_calc_anchor" in kinds and "memory_value_anchor" not in kinds:
            mutations.add("operand_mutation")
            mutations.add("instruction_deletion")
        if "generic_anchor" in kinds:
            mutations.add("instruction_deletion")
        return mutations

    # ================================================================
    # Build explanatory objects
    # ================================================================

    def build_explanatory_objects(self, strong_ids: Set[str],
                                  excluded: List[dict]) -> List[dict]:
        explanatory = []

        for obj_id in sorted(self.m.object_details.keys()):
            if obj_id in strong_ids:
                continue
            if not self._is_explanatory_candidate(obj_id):
                continue

            odet = self.m.object_details.get(obj_id, {})
            tags = list(odet.get("semantic_tags") or [])
            direct_roles, contextual_roles = self._infer_semantic_roles(obj_id)
            all_roles = uniq_keep_order(direct_roles + contextual_roles)

            explanation_value = self._get_explanation_value(obj_id, all_roles, direct_roles)
            if not explanation_value:
                continue

            rep_pcs = self.m.get_representative_pcs(obj_id)
            rep_disasm = self.m.get_representative_disasm(obj_id)

            related_strong = set()
            for pc in self.m.obj_direct_pcs.get(obj_id, set()):
                for s in self.m.pc_direct_objects.get(pc, set()):
                    if s in strong_ids:
                        related_strong.add(s)

            explanatory.append({
                "object_id": obj_id,
                "object_type": object_type(obj_id),
                "explanation_value": explanation_value,
                "semantic_tags": tags,
                "semantic_roles": all_roles,
                "direct_semantic_roles": direct_roles,
                "contextual_semantic_roles": contextual_roles,
                "representative_pcs": rep_pcs,
                "representative_disasm": rep_disasm,
                "related_strong_objects": sorted(related_strong)[:10],
            })

        return explanatory

    def _is_explanatory_candidate(self, obj_id: str) -> bool:
        if is_noise_object(obj_id):
            return False
        if obj_id == self.m.seed_object:
            return True
        if is_flag_object(obj_id):
            return True
        if is_structural_register(obj_id):
            return True
        if is_mem_object(obj_id) and obj_id in self.m.backward_objects:
            return True
        if is_stack_object(obj_id) and obj_id in self.m.backward_objects:
            return True
        return False

    def _get_explanation_value(self, obj_id: str, roles: List[str],
                                direct_roles: List[str]) -> Optional[str]:
        if obj_id == self.m.seed_object:
            return "污染源 seed 对象"
        if is_flag_object(obj_id):
            return "flags 寄存器，分支条件语义"
        if is_structural_register(obj_id):
            return "栈/帧指针"
        if is_mem_object(obj_id):
            return "backward 相关内存地址，辅助理解污染传播路径"
        if is_stack_object(obj_id):
            return "backward 相关栈变量（去重后的非代表成员）"
        return None


# ---------------------------------------------------------------------------
# Diagnostics
# ---------------------------------------------------------------------------

def build_diagnostics(model: DependencyModel,
                      strong_objects: List[dict],
                      anchors: List[dict],
                      excluded_objects: List[dict]) -> dict:
    failure_counter: Counter = Counter()
    for exc in excluded_objects:
        for reason in exc.get("exclusion_reasons", []):
            failure_counter[reason] += 1

    notes = []
    if not strong_objects:
        notes.append("未发现满足准入条件的强相关可变异对象。")
    if strong_objects and not anchors:
        notes.append("已找到强相关对象但无可落地的汇编锚点。")

    deletion_only_count = sum(1 for o in strong_objects if o.get("deletion_candidate_only", False))
    full_mutation_count = len(strong_objects) - deletion_only_count
    if deletion_only_count > 0:
        notes.append(
            f"strong set: {deletion_only_count} deletion-only + {full_mutation_count} full mutation"
        )

    type_dist = Counter()
    for o in strong_objects:
        type_dist[o["object_type"]] += 1

    anchor_tier_dist = Counter()
    for a in anchors:
        anchor_tier_dist[a["anchor_tier"]] += 1

    # v2.4: prologue/epilogue stats
    pe_count = sum(1 for a in anchors if a.get("is_prologue_epilogue", False))

    return {
        "failure_reasons": dict(sorted(failure_counter.items(), key=lambda kv: (-kv[1], kv[0]))),
        "notes": notes,
        "strong_type_distribution": dict(type_dist.most_common()),
        "anchor_tier_distribution": dict(anchor_tier_dist.most_common()),
        "anchor_prologue_epilogue_count": pe_count,
        "model_overview": {
            "seed_object": model.seed_object,
            "seed_symbol": model.seed_symbol,
            "backward_objects": len(model.backward_objects),
            "backward_leaf_objects": len(model.backward_leaf_objects),
            "forward_objects": len(model.forward_objects),
            "instruction_details": len(model.instruction_details),
            "object_details": len(model.object_details),
            "crt_pcs": len(model.crt_pcs),
            "prologue_epilogue_pcs": len(model.prologue_epilogue_pcs),
            "strong_causal_objects": len(strong_objects),
            "strong_full_mutation": full_mutation_count,
            "strong_deletion_only": deletion_only_count,
            "assembly_anchors": len(anchors),
            "stack_dedup_groups": len(model.stack_dedup_groups),
        },
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="筛选与污染源相关的强相关可变异对象和汇编层锚点。"
    )
    parser.add_argument("--dependency-summary", required=True,
                        help="dependency_summary.json 路径")
    parser.add_argument("--terminal-mapping", default=None,
                        help="terminal_node_mapping.json 路径（可选）")
    parser.add_argument("--path-report", default=None,
                        help="path_report.json 路径（可选）")
    parser.add_argument("--outdir", default="filter_out",
                        help="输出目录")
    args = parser.parse_args()

    with open(args.dependency_summary, "r", encoding="utf-8") as f:
        dep = json.load(f)

    mapping = None
    if args.terminal_mapping:
        try:
            with open(args.terminal_mapping, "r", encoding="utf-8") as f:
                mapping = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"[WARN] cannot load terminal mapping: {args.terminal_mapping}", file=sys.stderr)

    path_report = None
    if args.path_report:
        try:
            with open(args.path_report, "r", encoding="utf-8") as f:
                path_report = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"[WARN] cannot load path report: {args.path_report}", file=sys.stderr)

    model = DependencyModel(dep, mapping, path_report)
    filt = CausalCandidateFilter(model)

    strong_objects, excluded_objects = filt.build_strong_causal_objects()
    anchors = filt.build_assembly_anchors(strong_objects)
    strong_ids = {o["object_id"] for o in strong_objects}
    explanatory_objects = filt.build_explanatory_objects(strong_ids, excluded_objects)
    diagnostics = build_diagnostics(model, strong_objects, anchors, excluded_objects)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    dump_json(outdir / "strong_causal_objects.json", strong_objects)
    dump_json(outdir / "assembly_anchor_candidates.json", anchors)
    dump_json(outdir / "explanatory_objects.json", explanatory_objects)
    dump_json(outdir / "excluded_objects.json", excluded_objects)

    summary = {
        "status": "ok" if strong_objects else "no_mutable_strong_candidates",
        "seed_object": model.seed_object,
        "seed_symbol": model.seed_symbol,
        "counts": {
            "strong_causal_objects": len(strong_objects),
            "strong_full_mutation": sum(1 for o in strong_objects
                                        if not o.get("deletion_candidate_only", False)),
            "strong_deletion_only": sum(1 for o in strong_objects
                                        if o.get("deletion_candidate_only", False)),
            "assembly_anchor_candidates": len(anchors),
            "explanatory_objects": len(explanatory_objects),
            "excluded_objects": len(excluded_objects),
        },
        "notes": [
            "v2.4: tier 精细化 — primary 仅限比较/分支/call/含 var 或 operand_imm 的操作",
            "v2.4: 函数序言/尾声指令降级为 contextual 并标记 is_prologue_epilogue",
            "v2.4: anchor 增加 is_prologue_epilogue / prologue_epilogue_desc 字段",
        ],
        "diagnostics": diagnostics,
    }
    dump_json(outdir / "selection_summary.json", summary)

    print(f"[OK] outputs → {outdir}/")

    so_count = len(strong_objects)
    full_count = sum(1 for o in strong_objects if not o.get("deletion_candidate_only", False))
    del_count = so_count - full_count
    a_tiers = Counter(a["anchor_tier"] for a in anchors)
    pe_count = sum(1 for a in anchors if a.get("is_prologue_epilogue", False))
    print(f"\nSummary: {so_count} strong ({full_count} full + {del_count} del-only), "
          f"{len(anchors)} anchors (primary={a_tiers.get('primary',0)}, "
          f"secondary={a_tiers.get('secondary',0)}, "
          f"contextual={a_tiers.get('contextual',0)}, "
          f"prologue/epilogue={pe_count}), "
          f"{len(explanatory_objects)} explanatory, "
          f"{len(excluded_objects)} excluded")

    return 0


if __name__ == "__main__":
    sys.exit(main())