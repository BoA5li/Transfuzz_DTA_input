#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from collections import defaultdict, deque, Counter
from dataclasses import dataclass
from enum import Enum, auto

from triton import (
    TritonContext,
    ARCH,
    Instruction,
    MemoryAccess,
    CPUSIZE,
    OPCODE,
    MODE,
)

# ============================================================
# Configuration
# ============================================================

PROGRAM = "./spectre_v1"
SECRET_SYMBOL_CANDIDATES = ("array2", "secret", "temp", "probe")
MAX_TRACE_INSTRUCTIONS = 2_000_000

# ============================================================
# Helpers
# ============================================================

def esc(s):
    return str(s).replace("\\", "\\\\").replace('"', '\\"')


def safe_decode(bs, default=""):
    try:
        return bs.decode("utf-8", errors="ignore")
    except Exception:
        return default


def run_cmd(args):
    try:
        return subprocess.check_output(args, stderr=subprocess.DEVNULL).decode("utf-8", errors="ignore")
    except Exception:
        return ""


def normalize_reg_name(name: str) -> str:
    if not name:
        return name
    return name.lower()


def pc_node_name(pc: int) -> str:
    return f"pc:0x{pc:x}"


def reg_object_name(reg_name: str) -> str:
    return f"reg:{normalize_reg_name(reg_name)}"


def imm_object_name(v: int) -> str:
    return f"imm:{int(v)}"


def format_src(pc, addr2line_map=None):
    if not addr2line_map:
        return ""
    src = addr2line_map.get(pc)
    if not src:
        return ""
    return f"{src[0]}:{src[1]}"


def is_hex(s):
    try:
        int(s, 16)
        return True
    except Exception:
        return False


# ============================================================
# ELF / Symbol / Debug helpers
# ============================================================

def parse_nm_symbols(binary_path):
    syms = {}
    text = run_cmd(["nm", "-n", binary_path])
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 3:
            continue
        addr_s, typ, name = parts[0], parts[1], parts[2]
        if not is_hex(addr_s):
            continue
        syms[name] = int(addr_s, 16)
    return syms


def parse_objdump_sections(binary_path):
    sections = []
    text = run_cmd(["objdump", "-h", binary_path])
    for line in text.splitlines():
        line = line.strip()
        parts = line.split()
        if len(parts) < 7:
            continue
        # idx name size vma lma fileoff align
        if not parts[0].isdigit():
            continue
        try:
            name = parts[1]
            size = int(parts[2], 16)
            vma = int(parts[3], 16)
            lma = int(parts[4], 16)
            off = int(parts[5], 16)
            sections.append({
                "name": name,
                "size": size,
                "vma": vma,
                "lma": lma,
                "offset": off,
            })
        except Exception:
            pass
    return sections


def parse_plt_ranges(binary_path):
    ranges = []
    for sec in parse_objdump_sections(binary_path):
        n = sec["name"]
        if n.startswith(".plt"):
            start = sec["vma"]
            end = start + sec["size"]
            ranges.append((start, end, n))
    return ranges


def parse_dynamic_symbols(binary_path):
    syms = {}
    text = run_cmd(["objdump", "-T", binary_path])
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 6:
            continue
        if not is_hex(parts[0]):
            continue
        try:
            addr = int(parts[0], 16)
            name = parts[-1]
            syms[name] = addr
        except Exception:
            pass
    return syms


def parse_plt_symbol_map(binary_path):
    """
    尝试建立 plt 地址 -> 外部符号名 的映射
    兼容 x86_64 常见 objdump -d 输出格式:
      0000000000401030 <puts@plt>:
    """
    mp = {}
    text = run_cmd(["objdump", "-d", binary_path])
    for line in text.splitlines():
        line = line.rstrip()
        if "<" in line and ">:" in line:
            left = line.split("<", 1)[0].strip()
            mid = line.split("<", 1)[1].split(">:", 1)[0].strip()
            if left and is_hex(left):
                addr = int(left, 16)
                if "@plt" in mid:
                    mp[addr] = mid
    return mp


def build_addr2line_map(binary_path, pcs):
    mp = {}
    for pc in sorted(set(pcs)):
        out = run_cmd(["addr2line", "-e", binary_path, "-f", "-C", hex(pc)])
        lines = [x.strip() for x in out.splitlines() if x.strip()]
        if len(lines) >= 2:
            fileline = lines[1]
            if fileline != "??:0":
                if ":" in fileline:
                    fn, ln = fileline.rsplit(":", 1)
                    try:
                        mp[pc] = (fn, int(ln))
                    except Exception:
                        mp[pc] = (fileline, 0)
    return mp


# ============================================================
# Memory map / loader
# ============================================================

class SimpleMemoryImage:
    def __init__(self):
        self.mem = {}
        self.mapped_ranges = []  # (start, end, desc)

    def map_bytes(self, base, data: bytes, desc=""):
        for i, b in enumerate(data):
            self.mem[base + i] = b
        if data:
            self.mapped_ranges.append((base, base + len(data), desc))

    def read_byte(self, addr):
        return self.mem.get(addr, 0)

    def read_bytes(self, addr, size):
        return bytes(self.read_byte(addr + i) for i in range(size))

    def write_byte(self, addr, v):
        self.mem[addr] = v & 0xff

    def write_bytes(self, addr, data: bytes):
        for i, b in enumerate(data):
            self.mem[addr + i] = b & 0xff

    def is_mapped(self, addr):
        return addr in self.mem


def load_elf_segments(binary_path, memimg: SimpleMemoryImage):
    text = run_cmd(["readelf", "-W", "-l", binary_path])
    if not text:
        with open(binary_path, "rb") as f:
            data = f.read()
        # fallback flat map at 0x400000
        memimg.map_bytes(0x400000, data, "flat")
        return 0x400000

    entry = 0x400000
    with open(binary_path, "rb") as f:
        raw = f.read()

    for line in text.splitlines():
        s = line.strip()
        if s.startswith("Entry point"):
            try:
                entry = int(s.split("0x", 1)[1], 16)
            except Exception:
                pass

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if "LOAD" in line:
            full = line
            if i + 1 < len(lines):
                full += " " + lines[i + 1].strip()
            parts = full.replace("LOAD", " LOAD ").split()
            hexes = [p for p in parts if p.startswith("0x")]
            if len(hexes) >= 5:
                try:
                    off = int(hexes[0], 16)
                    vaddr = int(hexes[1], 16)
                    filesz = int(hexes[3], 16)
                    memsz = int(hexes[4], 16)

                    seg = raw[off:off + filesz]
                    memimg.map_bytes(vaddr, seg, "LOAD")
                    if memsz > filesz:
                        memimg.map_bytes(vaddr + filesz, b"\x00" * (memsz - filesz), "BSS")
                except Exception:
                    pass
            i += 2
            continue
        i += 1
    return entry


# ============================================================
# Classification helpers
# ============================================================

class ObjectClassifier:
    def __init__(self, global_ranges=None):
        self.global_ranges = global_ranges or []  # list of (name, start, end)

    def classify_mem_object(self, addr):
        for name, start, end in self.global_ranges:
            if start <= addr < end:
                off = addr - start
                if off == 0:
                    return f"glob:{name}"
                return f"glob:{name}+0x{off:x}"
        return f"mem:0x{addr:x}"


# ============================================================
# Graph helpers
# ============================================================

def backward_slice_from_pcs(seed_pcs, reverse_map):
    visited = set()
    worklist = list(seed_pcs)
    while worklist:
        cur = worklist.pop()
        if cur in visited:
            continue
        visited.add(cur)
        for pred in reverse_map.get(cur, set()):
            if pred not in visited:
                worklist.append(pred)
    return visited


def find_leaf_pcs_in_slice(slice_pcs, reverse_map):
    leaves = set()
    for pc in slice_pcs:
        preds = [p for p in reverse_map.get(pc, set()) if p in slice_pcs]
        if not preds:
            leaves.add(pc)
    return leaves


def backward_slice_from_objects(seed_objs, reverse_map):
    visited = set()
    worklist = list(seed_objs)
    while worklist:
        cur = worklist.pop()
        if cur in visited:
            continue
        visited.add(cur)
        for pred in reverse_map.get(cur, set()):
            if pred not in visited:
                worklist.append(pred)
    return visited


def find_leaf_objects_in_slice(slice_objs, reverse_map):
    leaves = set()
    for obj in slice_objs:
        preds = [p for p in reverse_map.get(obj, set()) if p in slice_objs]
        if not preds:
            leaves.add(obj)
    return leaves


# ============================================================
# Control dependency analyzer
# ============================================================

class DynamicControlDependencyAnalyzer:
    def __init__(self):
        self.forward_ctrl = defaultdict(set)
        self.reverse_ctrl = defaultdict(set)
        self.control_edges = set()
        self.branch_condition_objects = defaultdict(set)

    def record_branch_condition_objects(self, pc, objs):
        self.branch_condition_objects[pc] |= set(objs)

    def build_from_cfg(self, cfg_edges, inst_info):
        """
        恢复原始稳定机制：
        - 仅基于动态 CFG 做轻量近似控制依赖
        - 对条件跳转分支点，将其后续“分叉后可达”节点标记为受控
        兼容扩展分析：
        - 跳过 PLT/外部桩等不稳定点
        """
        succs = defaultdict(set)
        preds = defaultdict(set)
        pcs = set()

        for a, b in cfg_edges:
            succs[a].add(b)
            preds[b].add(a)
            pcs.add(a)
            pcs.add(b)

        cond_branches = set()
        for pc in pcs:
            info = inst_info.get(pc, {})
            d = info.get("disasm", "").lower()
            if d.startswith("j") and d not in ("jmp", "jmpq"):
                cond_branches.add(pc)

        for br in cond_branches:
            sset = list(succs.get(br, set()))
            if len(sset) < 2:
                continue

            visited = set()
            q = deque(sset)
            limit = 20000
            while q and limit > 0:
                limit -= 1
                cur = q.popleft()
                if cur == br or cur in visited:
                    continue
                visited.add(cur)
                self.forward_ctrl[br].add(cur)
                self.reverse_ctrl[cur].add(br)
                self.control_edges.add((br, cur))
                for nx in succs.get(cur, set()):
                    if nx not in visited:
                        q.append(nx)


# ============================================================
# External call / PLT / GOT / special-instruction compatibility
# ============================================================

class ExternalFlowCompat:
    """
    目标：
      1) 保持原有分析逻辑不变
      2) 为动态链接 / PLT / GOT / 外部函数 / 特殊指令 / 返回地址管理提供稳定补丁
    """

    def __init__(self, memimg: SimpleMemoryImage, binary_path: str):
        self.memimg = memimg
        self.binary_path = binary_path

        self.plt_ranges = parse_plt_ranges(binary_path)
        self.plt_symbol_map = parse_plt_symbol_map(binary_path)
        self.dynamic_symbols = parse_dynamic_symbols(binary_path)

        self.stub_base = 0x700000000000
        self.stub_next = self.stub_base
        self.stub_map = {}         # name -> addr
        self.stub_rev = {}         # addr -> name

        self.got_slots = {}        # got_addr -> target_stub_or_known
        self.synthetic_return_stack = []

    def alloc_stub(self, name):
        if name in self.stub_map:
            return self.stub_map[name]
        addr = self.stub_next
        self.stub_next += 0x100
        # ret
        self.memimg.map_bytes(addr, b"\xc3", f"stub:{name}")
        self.stub_map[name] = addr
        self.stub_rev[addr] = name
        return addr

    def is_in_plt(self, pc):
        for a, b, _ in self.plt_ranges:
            if a <= pc < b:
                return True
        return False

    def get_plt_symbol(self, pc):
        if pc in self.plt_symbol_map:
            return self.plt_symbol_map[pc]
        # 尝试向下对齐到 PLT entry
        for base, name in self.plt_symbol_map.items():
            if base <= pc < base + 0x20:
                return name
        return None

    def is_external_stub(self, pc):
        return pc in self.stub_rev

    def get_stub_name(self, pc):
        return self.stub_rev.get(pc)

    def patch_got_slot(self, got_addr, sym_name):
        target = self.alloc_stub(sym_name)
        self.got_slots[got_addr] = target
        data = int(target).to_bytes(8, byteorder="little", signed=False)
        self.memimg.write_bytes(got_addr, data)
        return target

    def try_patch_indirect_target(self, addr):
        """
        如果某个内存地址看起来像 GOT slot，但尚未初始化，则补丁为 ext stub。
        """
        if addr in self.got_slots:
            return self.got_slots[addr]
        sym_name = f"extern_at_0x{addr:x}"
        return self.patch_got_slot(addr, sym_name)

    def push_return_address(self, ra):
        self.synthetic_return_stack.append(ra)

    def pop_return_address(self):
        if self.synthetic_return_stack:
            return self.synthetic_return_stack.pop()
        return None

    def handle_special_before(self, ctx: TritonContext, inst: Instruction):
        """
        兼容某些特殊/系统指令，避免仿真崩溃。
        返回 True 表示已完全处理并可继续。
        """
        d = inst.getDisassembly().lower()

        # 对 cpuid / rdtsc / lfence / mfence / sfence / pause / endbr64 做兼容
        if d.startswith("cpuid"):
            try:
                for rn in ("rax", "rbx", "rcx", "rdx"):
                    reg = getattr(ctx.registers, rn)
                    ctx.setConcreteRegisterValue(reg, 0)
            except Exception:
                pass
            return True

        if d.startswith("rdtsc"):
            try:
                ctx.setConcreteRegisterValue(ctx.registers.rax, 0)
                ctx.setConcreteRegisterValue(ctx.registers.rdx, 0)
            except Exception:
                pass
            return True

        if d.startswith(("lfence", "mfence", "sfence", "pause", "endbr64", "nop")):
            return True

        return False

    def resolve_call_target(self, ctx: TritonContext, inst: Instruction):
        """
        返回 (kind, target, name)
        kind: direct / indirect / plt / stub / unknown
        """
        pc = inst.getAddress()
        dis = inst.getDisassembly().lower()

        if self.is_in_plt(pc):
            name = self.get_plt_symbol(pc) or f"plt_0x{pc:x}"
            stub = self.alloc_stub(name)
            return ("plt", stub, name)

        # 尝试从 Triton 读取 next address 相关信息并结合操作数判定
        # 保守做法：优先从 disasm 解析 direct call
        if dis.startswith("call"):
            toks = dis.split(None, 1)
            if len(toks) > 1:
                op = toks[1].strip()
                # direct relative usually shown as absolute by Triton disasm
                if op.startswith("0x"):
                    try:
                        return ("direct", int(op, 16), None)
                    except Exception:
                        pass
                # qword ptr [...]
                if "[" in op and "]" in op:
                    inside = op[op.find("[") + 1:op.find("]")]
                    inside = inside.replace(" ", "")
                    # [rip+0x....] / [0x....]
                    if inside.startswith("0x"):
                        try:
                            mem_addr = int(inside, 16)
                            tgt = self.try_patch_indirect_target(mem_addr)
                            return ("indirect", tgt, f"extern_at_0x{mem_addr:x}")
                        except Exception:
                            pass
                    if inside.startswith("rip+"):
                        try:
                            off = int(inside[4:], 16)
                            next_pc = pc + inst.getSize()
                            mem_addr = next_pc + off
                            tgt = self.try_patch_indirect_target(mem_addr)
                            return ("indirect", tgt, f"extern_at_0x{mem_addr:x}")
                        except Exception:
                            pass

        return ("unknown", None, None)

    def emulate_call_transfer(self, ctx: TritonContext, inst: Instruction):
        """
        返回实际应跳转到的 target pc。
        这里不改变原分析逻辑，只在调用不稳定目标时做补丁稳定。
        """
        kind, tgt, name = self.resolve_call_target(ctx, inst)
        ra = inst.getAddress() + inst.getSize()
        self.push_return_address(ra)

        # 更新栈上的返回地址，保证 ret 可回收
        try:
            rsp = ctx.getConcreteRegisterValue(ctx.registers.rsp)
            new_rsp = (rsp - 8) & 0xffffffffffffffff
            ctx.setConcreteRegisterValue(ctx.registers.rsp, new_rsp)
            self.memimg.write_bytes(new_rsp, ra.to_bytes(8, byteorder="little", signed=False))
            ctx.setConcreteMemoryAreaValue(new_rsp, ra.to_bytes(8, byteorder="little", signed=False))
        except Exception:
            pass

        if kind in ("plt", "indirect"):
            return tgt
        if kind == "direct" and tgt is not None:
            return tgt

        # unknown call => synthetic stub
        stub = self.alloc_stub(name or f"unknown_call_0x{inst.getAddress():x}")
        return stub

    def emulate_ret_transfer(self, ctx: TritonContext, inst: Instruction):
        """
        稳定返回地址管理：
        优先从 concrete stack 取；失败则回退 synthetic stack。
        """
        try:
            rsp = ctx.getConcreteRegisterValue(ctx.registers.rsp)
            raw = self.memimg.read_bytes(rsp, 8)
            target = int.from_bytes(raw, byteorder="little", signed=False)
            ctx.setConcreteRegisterValue(ctx.registers.rsp, (rsp + 8) & 0xffffffffffffffff)
            if target != 0:
                self.pop_return_address()
                return target
        except Exception:
            pass

        alt = self.pop_return_address()
        if alt is not None:
            try:
                rsp = ctx.getConcreteRegisterValue(ctx.registers.rsp)
                ctx.setConcreteRegisterValue(ctx.registers.rsp, (rsp + 8) & 0xffffffffffffffff)
            except Exception:
                pass
            return alt
        return None


# ============================================================
# Main
# ============================================================

def main():
    binary_path = PROGRAM
    if len(sys.argv) >= 2:
        binary_path = sys.argv[1]

    ctx = TritonContext(ARCH.X86_64)
    try:
        ctx.setMode(MODE.ALIGNED_MEMORY, True)
    except Exception:
        pass
    try:
        ctx.setMode(MODE.CONSTANT_FOLDING, True)
    except Exception:
        pass
    try:
        ctx.setMode(MODE.AST_OPTIMIZATIONS, True)
    except Exception:
        pass

    memimg = SimpleMemoryImage()
    entry = load_elf_segments(binary_path, memimg)

    nm_symbols = parse_nm_symbols(binary_path)
    dyn_symbols = parse_dynamic_symbols(binary_path)
    all_symbols = dict(nm_symbols)
    all_symbols.update(dyn_symbols)

    sections = parse_objdump_sections(binary_path)
    global_ranges = []
    for sec in sections:
        name = sec["name"]
        if name in (".data", ".bss", ".rodata", ".data.rel.ro") or name.startswith(".got"):
            start = sec["vma"]
            end = start + sec["size"]
            global_ranges.append((name, start, end))

    for name, addr in nm_symbols.items():
        for cand in SECRET_SYMBOL_CANDIDATES:
            if cand in name:
                # 尝试给已知全局符号更细粒度范围
                global_ranges.append((name, addr, addr + 0x4000))

    classifier = ObjectClassifier(global_ranges=global_ranges)
    classify_mem_object = classifier.classify_mem_object

    compat = ExternalFlowCompat(memimg, binary_path)

    # initialize Triton memory from memimg
    if memimg.mem:
        min_addr = min(memimg.mem.keys())
        max_addr = max(memimg.mem.keys())
        cur = min_addr
        chunk = []
        chunk_base = cur
        while cur <= max_addr:
            if cur in memimg.mem:
                if not chunk:
                    chunk_base = cur
                chunk.append(memimg.mem[cur])
            else:
                if chunk:
                    ctx.setConcreteMemoryAreaValue(chunk_base, bytes(chunk))
                    chunk = []
            cur += 1
        if chunk:
            ctx.setConcreteMemoryAreaValue(chunk_base, bytes(chunk))

    # basic register init
    STACK_BASE = 0x7ffffff00000
    STACK_SIZE = 0x200000
    memimg.map_bytes(STACK_BASE - STACK_SIZE, b"\x00" * STACK_SIZE, "stack")
    ctx.setConcreteMemoryAreaValue(STACK_BASE - STACK_SIZE, b"\x00" * STACK_SIZE)

    try:
        ctx.setConcreteRegisterValue(ctx.registers.rsp, STACK_BASE - 0x1000)
        ctx.setConcreteRegisterValue(ctx.registers.rbp, STACK_BASE - 0x1000)
        ctx.setConcreteRegisterValue(ctx.registers.rip, entry)
    except Exception:
        pass

    # ============================================================
    # Analysis state
    # ============================================================
    inst_count = 0
    cfg_edges = set()
    dfg_edges = set()

    reverse_dfg = defaultdict(set)
    forward_dfg = defaultdict(set)

    object_deps = defaultdict(set)
    object_rev_deps = defaultdict(set)

    value_node_edges = defaultdict(set)
    value_node_rev_edges = defaultdict(set)
    inst_value_node_edges = set()

    inst_info = {}
    inst_rw = defaultdict(lambda: {
        "read_regs": set(),
        "write_regs": set(),
        "read_mems": set(),
        "write_mems": set(),
    })
    inst_immediates = defaultdict(set)
    inst_taint_io = defaultdict(lambda: {
        "use_regs": set(),
        "use_mems": set(),
        "def_regs": set(),
        "def_mems": set(),
    })
    inst_uses_taint = defaultdict(bool)

    conditional_branch_pcs = set()
    secret_use_pcs = set()
    secret_def_pcs = set()
    secret_use_details = defaultdict(set)
    secret_def_details = defaultdict(set)

    ctrl_analyzer = DynamicControlDependencyAnalyzer()

    last_reg_def = {}
    last_mem_def = {}

    prev_pc = None

    # ============================================================
    # Debug options / helpers
    # ============================================================

    DEBUG_TRACE_HEAD = True
    DEBUG_TRACE_TAIL = True
    DEBUG_CALLS = True
    DEBUG_FUNC_HIT = True
    DEBUG_HOT_PC = True
    DEBUG_STOP_CAUSE = True
    DEBUG_LOOP_DETECT = True

    TRACE_HEAD_LIMIT = 200
    TRACE_TAIL_LIMIT = 200
    HOT_PC_LIMIT = 20
    HOT_EDGE_LIMIT = 20
    RECENT_PC_WINDOW = 5000


    class StopReason(Enum):
        NONE = auto()
        MAX_INSTRUCTIONS = auto()
        FETCH_FAIL = auto()
        DISASSEMBLY_FAIL = auto()
        PROCESSING_FAIL = auto()
        RIP_READ_FAIL = auto()
        RIP_ZERO = auto()
        UNKNOWN = auto()


    def stop_reason_str(reason):
        return reason.name if isinstance(reason, StopReason) else str(reason)


    @dataclass
    class TraceEntry:
        pc: int
        disasm: str
        func: str = ""
        is_plt: bool = False
        is_ext_stub: bool = False


    def lookup_func_name(pc):
        """
        根据 all_symbols 做“最近且不超过 pc”的近似命名。
        用于第一轮调试定位是否进入 main / spectre_function / PLT。
        """
        best_name = ""
        best_addr = -1
        for name, addr in all_symbols.items():
            try:
                if addr <= pc and addr > best_addr:
                    best_addr = addr
                    best_name = name
            except Exception:
                pass
        return best_name


    def make_trace_entry(pc, disasm):
        func_name = lookup_func_name(pc)
        is_plt = False
        is_ext_stub = False

        try:
            is_plt = compat.is_in_plt(pc)
        except Exception:
            pass

        try:
            is_ext_stub = compat.is_external_stub(pc)
        except Exception:
            pass

        return TraceEntry(
            pc=pc,
            disasm=disasm,
            func=func_name,
            is_plt=is_plt,
            is_ext_stub=is_ext_stub,
        )


    watched_func_names = [
        "_start",
        "main",
        "readMemoryByte",
        "spectre_function",
        "strlen",
        "strlen@plt",
        "printf",
        "printf@plt",
        "__libc_start_main",
        "__libc_start_main@plt",
    ]

    watched_func_hits = Counter()
    watched_func_first_seen = set()


    def update_watched_func_hit(pc, disasm):
        cur_name = lookup_func_name(pc)
        if not cur_name:
            return

        for target in watched_func_names:
            if cur_name == target:
                watched_func_hits[target] += 1
                if DEBUG_FUNC_HIT and target not in watched_func_first_seen:
                    watched_func_first_seen.add(target)
                    print(f"[DEBUG] First hit function: {target} at PC=0x{pc:x} disasm={disasm}")


    stop_reason = StopReason.NONE
    stop_pc = 0
    stop_detail = ""

    trace_head = []
    trace_tail = deque(maxlen=TRACE_TAIL_LIMIT)

    pc_exec_count = Counter()
    cfg_edge_exec_count = Counter()
    recent_pcs = deque(maxlen=RECENT_PC_WINDOW)

    function_unique_pcs = defaultdict(set)

    # secret region heuristic
    secret_addr_ranges = []
    for name, addr in all_symbols.items():
        if any(c in name for c in SECRET_SYMBOL_CANDIDATES):
            secret_addr_ranges.append((name, addr, addr + 0x4000))

    def is_secret_addr(addr):
        for _, a, b in secret_addr_ranges:
            if a <= addr < b:
                return True
        return False

    def add_object_dep(src, dst):
        if src == dst:
            return
        object_deps[src].add(dst)
        object_rev_deps[dst].add(src)

    def add_value_node_edge(src, dst):
        if src == dst:
            return
        value_node_edges[src].add(dst)
        value_node_rev_edges[dst].add(src)
        inst_value_node_edges.add((src, dst))

    def record_object_level_dependencies(pc):
        rw = inst_rw.get(pc, {})
        src_objs = set()
        dst_objs = set()

        for r in rw.get("read_regs", set()):
            src_objs.add(reg_object_name(r))
        for a in rw.get("read_mems", set()):
            src_objs.add(classify_mem_object(a))
        for iv in inst_immediates.get(pc, set()):
            src_objs.add(imm_object_name(iv))

        for r in rw.get("write_regs", set()):
            dst_objs.add(reg_object_name(r))
        for a in rw.get("write_mems", set()):
            dst_objs.add(classify_mem_object(a))            stop_reason = StopReason.UNKNOWN
            stop_pc = pc
            stop_detail = "hlt reached"
            break

        pcn = pc_node_name(pc)

        for src in src_objs:
            for dst in dst_objs:
                add_object_dep(src, dst)

        for src in src_objs:
            add_value_node_edge(src, pcn)
        for dst in dst_objs:
            add_value_node_edge(pcn, dst)

    # ============================================================
    # Trace loop
    # ============================================================
    while inst_count < MAX_TRACE_INSTRUCTIONS:
        try:
            pc = ctx.getConcreteRegisterValue(ctx.registers.rip)
        except Exception as e:
            stop_reason = StopReason.RIP_READ_FAIL
            stop_pc = 0
            stop_detail = f"failed to read RIP: {type(e).__name__}: {e}"
            break

        if pc == 0:
            stop_reason = StopReason.RIP_ZERO
            stop_pc = pc
            stop_detail = "RIP became zero"
            break

        opcode = memimg.read_bytes(pc, 16)
        if not opcode or opcode == b"\x00" * len(opcode):
            # unmapped or zero area => stop unless external stub
            if not compat.is_external_stub(pc):
                stop_reason = StopReason.FETCH_FAIL
                stop_pc = pc
                stop_detail = "unmapped or zero-filled instruction bytes"
                break

        inst = Instruction(pc, opcode)
        try:
            ctx.disassembly(inst)
        except Exception as e:
            if compat.is_external_stub(pc):
                inst = Instruction(pc, memimg.read_bytes(pc, 1))
                try:
                    ctx.disassembly(inst)
                except Exception as e2:
                    stop_reason = StopReason.DISASSEMBLY_FAIL
                    stop_pc = pc
                    stop_detail = f"external stub disassembly failed: {type(e2).__name__}: {e2}"
                    break
            else:
                stop_reason = StopReason.DISASSEMBLY_FAIL
                stop_pc = pc
                stop_detail = f"disassembly failed: {type(e).__name__}: {e}"
                break

        disasm = inst.getDisassembly()

        # ---------------- debug trace record ----------------
        if disasm.lower().startswith("hlt"):
            stop_reason = StopReason.UNKNOWN
            stop_pc = pc
            stop_detail = "hlt reached"
            break

        te = make_trace_entry(pc, disasm)
        if DEBUG_TRACE_HEAD and len(trace_head) < TRACE_HEAD_LIMIT:
            trace_head.append(te)
        if DEBUG_TRACE_TAIL:
            trace_tail.append(te)

        pc_exec_count[pc] += 1
        recent_pcs.append(pc)

        cur_func = lookup_func_name(pc)
        if cur_func:
            function_unique_pcs[cur_func].add(pc)

        update_watched_func_hit(pc, disasm)

        # record instruction metadata
        info = inst_info.setdefault(pc, {})
        info["disasm"] = disasm
        info["plt"] = False
        info["external_stub"] = False

        try:
            if compat.is_in_plt(pc):
                info["plt"] = True
                info["plt_name"] = compat.get_plt_symbol(pc)
        except Exception:
            pass

        try:
            if compat.is_external_stub(pc):
                info["external_stub"] = True
                info["external_name"] = compat.get_stub_name(pc)
        except Exception:
            pass

        # cfg edge
        if prev_pc is not None:
            cfg_edges.add((prev_pc, pc))
            cfg_edge_exec_count[(prev_pc, pc)] += 1
        prev_pc = pc

        # RW summary for this instruction
        rw = {
            "read_regs": set(),
            "write_regs": set(),
            "read_mems": set(),
            "write_mems": set(),
        }

        # Triton operands
        for op in inst.getOperands():
            try:
                if op.getType() == OPERAND.REG:
                    reg_name = op.getName()
                    if op.isRead():
                        rw["read_regs"].add(reg_name)
                    if op.isWrite():
                        rw["write_regs"].add(reg_name)
                elif op.getType() == OPERAND.MEM:
                    base = op.getBaseRegister()
                    index = op.getIndexRegister()
                    disp = op.getDisplacement()
                    addr = 0

                    if base is not None and base.getId() != 0:
                        addr += ctx.getConcreteRegisterValue(base)
                    if index is not None and index.getId() != 0:
                        scale = op.getScale() if hasattr(op, "getScale") else 1
                        addr += ctx.getConcreteRegisterValue(index) * scale
                    if disp is not None:
                        try:
                            addr += disp.getValue()
                        except Exception:
                            pass

                    size = op.getSize()
                    for a in range(addr, addr + max(size, 1)):
                        if op.isRead():
                            rw["read_mems"].add(a)
                        if op.isWrite():
                            rw["write_mems"].add(a)
            except Exception:
                pass

        inst_rw[pc] = rw

        # immediate collection
        for op in inst.getOperands():
            try:
                if op.getType() == OPERAND.IMM:
                    inst_immediates[pc].add(op.getValue())
            except Exception:
                pass

        # external/plt/control-flow compatibility handling
        dlow = disasm.lower()
        next_pc_override = None
        handled_cf = False

        if dlow.startswith("call"):
            try:
                next_pc_override = compat.emulate_call_transfer(ctx, inst)
                handled_cf = True

                if DEBUG_CALLS:
                    extra = ""
                    try:
                        if compat.is_in_plt(pc):
                            extra += f" [CALLSITE_IN_PLT:{compat.get_plt_symbol(pc)}]"
                    except Exception:
                        pass
                    try:
                        if next_pc_override is not None:
                            tgt_name = lookup_func_name(next_pc_override)
                            if tgt_name:
                                extra += f" -> <{tgt_name}>"
                            if compat.is_external_stub(next_pc_override):
                                extra += f" [EXT_STUB:{compat.get_stub_name(next_pc_override)}]"
                    except Exception:
                        pass
                    print(f"[DEBUG][CALL] PC=0x{pc:x} {disasm} next_pc_override=0x{(next_pc_override if next_pc_override is not None else 0):x}{extra}")

            except Exception as e:
                if DEBUG_CALLS:
                    print(f"[WARN][CALL] emulate_call_transfer failed at PC=0x{pc:x}: {type(e).__name__}: {e}")
                handled_cf = False

        elif dlow.startswith("ret"):
            try:
                try:
                    rsp_before = ctx.getConcreteRegisterValue(ctx.registers.rsp)
                except Exception:
                    rsp_before = 0

                next_pc_override = compat.emulate_ret_transfer(ctx, inst)
                handled_cf = True

                if DEBUG_CALLS:
                    extra = ""
                    try:
                        tgt_name = lookup_func_name(next_pc_override) if next_pc_override is not None else ""
                        if tgt_name:
                            extra += f" -> <{tgt_name}>"
                    except Exception:
                        pass
                    print(f"[DEBUG][RET] PC=0x{pc:x} {disasm} RSP=0x{rsp_before:x} next_pc_override=0x{(next_pc_override if next_pc_override is not None else 0):x}{extra}")

            except Exception as e:
                if DEBUG_CALLS:
                    print(f"[WARN][RET] emulate_ret_transfer failed at PC=0x{pc:x}: {type(e).__name__}: {e}")
                handled_cf = False

        # conditional branch marker
        if dlow.startswith("j") and not dlow.startswith("jmp"):
            conditional_branch_pcs.add(pc)

        # process semantics if not already handled
        if not handled_cf:
            try:
                ctx.processing(inst)
            except Exception as e:
                if DEBUG_CALLS:
                    print(f"[WARN][PROC] ctx.processing failed at PC=0x{pc:x} {disasm}: {type(e).__name__}: {e}")

                # final fallback path
                if dlow.startswith("call"):
                    try:
                        next_pc_override = compat.emulate_call_transfer(ctx, inst)
                        handled_cf = True
                        if DEBUG_CALLS:
                            print(f"[DEBUG][CALL-FALLBACK] PC=0x{pc:x} next_pc_override=0x{(next_pc_override if next_pc_override is not None else 0):x}")
                    except Exception as e2:
                        stop_reason = StopReason.PROCESSING_FAIL
                        stop_pc = pc
                        stop_detail = f"ctx.processing failed and call fallback failed: {type(e2).__name__}: {e2}"
                        break

                elif dlow.startswith("ret"):
                    try:
                        next_pc_override = compat.emulate_ret_transfer(ctx, inst)
                        handled_cf = True
                        if DEBUG_CALLS:
                            print(f"[DEBUG][RET-FALLBACK] PC=0x{pc:x} next_pc_override=0x{(next_pc_override if next_pc_override is not None else 0):x}")
                    except Exception as e2:
                        stop_reason = StopReason.PROCESSING_FAIL
                        stop_pc = pc
                        stop_detail = f"ctx.processing failed and ret fallback failed: {type(e2).__name__}: {e2}"
                        break

                else:
                    next_pc_override = pc + max(inst.getSize(), 1)
                    handled_cf = True
                    if DEBUG_CALLS:
                        print(f"[DEBUG][SKIP] PC=0x{pc:x} {disasm} -> next_pc_override=0x{next_pc_override:x}")

        # apply RIP override if needed
        if next_pc_override is not None:
            try:
                ctx.setConcreteRegisterValue(ctx.registers.rip, next_pc_override)
                if DEBUG_CALLS and (dlow.startswith("call") or dlow.startswith("ret")):
                    print(f"[DEBUG][RIP-FIXUP] set RIP = 0x{next_pc_override:x} from PC=0x{pc:x}")
            except Exception as e:
                if DEBUG_CALLS:
                    print(f"[WARN][RIP-FIXUP] failed to set RIP at PC=0x{pc:x}: {type(e).__name__}: {e}")

        inst_count += 1

    if stop_reason == StopReason.NONE and inst_count >= MAX_TRACE_INSTRUCTIONS:
        stop_reason = StopReason.MAX_INSTRUCTIONS
        try:
            stop_pc = ctx.getConcreteRegisterValue(ctx.registers.rip)
        except Exception:
            stop_pc = 0
        stop_detail = "instruction budget exhausted"

    # ============================================================
    # addr2line map
    # ============================================================
    addr2line_map = build_addr2line_map(binary_path, inst_info.keys())

    # ============================================================
    # Build control dependencies after dynamic CFG is known
    # ============================================================
    ctrl_analyzer.build_from_cfg(cfg_edges, inst_info)

    # 分支条件的数据依赖补齐到 object graph / inst graph
    for br_pc in sorted(conditional_branch_pcs):
        pcn = pc_node_name(br_pc)
        cond_objs = ctrl_analyzer.branch_condition_objects.get(br_pc, set())

        for obj in cond_objs:
            # 条件值 -> branch 指令节点
            add_value_node_edge(obj, pcn)

        # 同时把“条件对象 -> 被控制对象”也加入 object graph
        for controlled_pc in ctrl_analyzer.forward_ctrl.get(br_pc, set()):
            rw = inst_rw.get(controlled_pc, {})
            dst_objs = set()
            for r in rw.get("write_regs", set()):
                dst_objs.add(reg_object_name(r))
            for a in rw.get("write_mems", set()):
                dst_objs.add(classify_mem_object(a))
            # 如果该受控指令本身是secret use/def，也将其读对象视为受branch控制
            for a in rw.get("read_mems", set()):
                if classify_mem_object(a).startswith("glob:array2") or a in secret_use_details.get(controlled_pc, set()) or a in secret_def_details.get(controlled_pc, set()):
                    dst_objs.add(classify_mem_object(a))

            for cobj in cond_objs:
                for dobj in dst_objs:
                    add_object_dep(cobj, dobj)

            # branch_pc -> controlled_pc 进入值图
            add_value_node_edge(pcn, pc_node_name(controlled_pc))

    # 控制依赖映射到指令级 reverse deps：controlled_pc <- branch_pc
    reverse_ctrl = ctrl_analyzer.reverse_ctrl
    forward_ctrl = ctrl_analyzer.forward_ctrl
    control_edges = ctrl_analyzer.control_edges

    # 联合 reverse 依赖图：数据 + 控制
    combined_reverse_deps = defaultdict(set)
    combined_forward_deps = defaultdict(set)

    all_pcs = set(inst_info.keys())
    for pc in all_pcs:
        for pred in reverse_dfg.get(pc, set()):
            combined_reverse_deps[pc].add(pred)
            combined_forward_deps[pred].add(pc)
        for pred in reverse_ctrl.get(pc, set()):
            combined_reverse_deps[pc].add(pred)
            combined_forward_deps[pred].add(pc)

    # ============================================================
    # Backward dependency analysis
    # ============================================================
    secret_seed_pcs = set(secret_use_pcs) | set(secret_def_pcs)

    secret_backward_slice_data = backward_slice_from_pcs(secret_seed_pcs, reverse_dfg)
    secret_leaf_pcs_data = find_leaf_pcs_in_slice(secret_backward_slice_data, reverse_dfg)

    # 数据+控制联合切片
    secret_backward_slice_combined = backward_slice_from_pcs(secret_seed_pcs, combined_reverse_deps)
    secret_leaf_pcs_combined = find_leaf_pcs_in_slice(secret_backward_slice_combined, combined_reverse_deps)

    secret_seed_objects = set()
    for pc, addrs in secret_use_details.items():
        for a in addrs:
            secret_seed_objects.add(classify_mem_object(a))
    for pc, addrs in secret_def_details.items():
        for a in addrs:
            secret_seed_objects.add(classify_mem_object(a))

    object_backward_slice = backward_slice_from_objects(secret_seed_objects, object_rev_deps)
    object_leaf_slice = find_leaf_objects_in_slice(object_backward_slice, object_rev_deps)

    backward_related_regs = set()
    backward_related_mems = set()
    backward_related_imms = set()

    for pc in secret_backward_slice_combined:
        rw = inst_rw.get(pc, {})
        backward_related_regs |= set(rw.get("read_regs", set()))
        backward_related_regs |= set(rw.get("write_regs", set()))
        backward_related_mems |= set(rw.get("read_mems", set()))
        backward_related_mems |= set(rw.get("write_mems", set()))
        backward_related_imms |= set(inst_immediates.get(pc, set()))

    # 值节点图中的 backward object/value tracing
    secret_seed_value_nodes = set(secret_seed_objects)
    for pc in secret_seed_pcs:
        secret_seed_value_nodes.add(pc_node_name(pc))

    def backward_slice_from_value_nodes(seed_nodes, reverse_map):
        visited = set()
        worklist = list(seed_nodes)
        while worklist:
            cur = worklist.pop()
            if cur in visited:
                continue
            visited.add(cur)
            for pred in reverse_map.get(cur, set()):
                if pred not in visited:
                    worklist.append(pred)
        return visited

    def find_leaf_value_nodes_in_slice(slice_nodes, reverse_map):
        leaves = set()
        for n in slice_nodes:
            preds = [p for p in reverse_map.get(n, set()) if p in slice_nodes]
            if len(preds) == 0:
                leaves.add(n)
        return leaves

    value_backward_slice = backward_slice_from_value_nodes(secret_seed_value_nodes, value_node_rev_edges)
    value_leaf_slice = find_leaf_value_nodes_in_slice(value_backward_slice, value_node_rev_edges)


    # ============================================================
    # Debug summary
    # ============================================================

    if DEBUG_STOP_CAUSE:
        print(f"[DEBUG] Stop reason: {stop_reason_str(stop_reason)} at PC=0x{stop_pc:x} ({stop_detail})")
        print(f"[DEBUG] Total executed instructions: {inst_count}")
        print(f"[DEBUG] Unique CFG edges: {len(cfg_edges)}")
        print(f"[DEBUG] Unique instruction PCs: {len(inst_info)}")

    if DEBUG_TRACE_HEAD:
        print(f"\n[DEBUG] Trace head (first {len(trace_head)} instructions)")
        for i, e in enumerate(trace_head):
            extra = ""
            if e.func:
                extra += f" <{e.func}>"
            if e.is_plt:
                extra += " [PLT]"
            if e.is_ext_stub:
                extra += " [EXT_STUB]"
            print(f"  [{i}] PC=0x{e.pc:x}  {e.disasm}{extra}")

    if DEBUG_TRACE_TAIL:
        print(f"\n[DEBUG] Trace tail (last {len(trace_tail)} instructions)")
        for i, e in enumerate(trace_tail):
            extra = ""
            if e.func:
                extra += f" <{e.func}>"
            if e.is_plt:
                extra += " [PLT]"
            if e.is_ext_stub:
                extra += " [EXT_STUB]"
            print(f"  [{i}] PC=0x{e.pc:x}  {e.disasm}{extra}")

    if DEBUG_HOT_PC:
        print(f"\n[DEBUG] Hot PCs (top {min(HOT_PC_LIMIT, len(pc_exec_count))})")
        for i, (hot_pc, cnt) in enumerate(pc_exec_count.most_common(HOT_PC_LIMIT)):
            extra = ""
            fn = lookup_func_name(hot_pc)
            if fn:
                extra += f" <{fn}>"
            try:
                if compat.is_in_plt(hot_pc):
                    extra += f" [PLT:{compat.get_plt_symbol(hot_pc)}]"
            except Exception:
                pass
            try:
                if compat.is_external_stub(hot_pc):
                    extra += f" [EXT_STUB:{compat.get_stub_name(hot_pc)}]"
            except Exception:
                pass
            dis = inst_info.get(hot_pc, {}).get("disasm", "")
            if dis:
                extra += f" :: {dis}"
            print(f"  #{i} PC=0x{hot_pc:x} count={cnt}{extra}")

        print(f"\n[DEBUG] Hot CFG edges (top {min(HOT_EDGE_LIMIT, len(cfg_edge_exec_count))})")
        for i, ((src, dst), cnt) in enumerate(cfg_edge_exec_count.most_common(HOT_EDGE_LIMIT)):
            sfn = lookup_func_name(src)
            dfn = lookup_func_name(dst)
            sextra = f" <{sfn}>" if sfn else ""
            dextra = f" <{dfn}>" if dfn else ""
            print(f"  #{i} 0x{src:x}{sextra} -> 0x{dst:x}{dextra} count={cnt}")

    if DEBUG_FUNC_HIT:
        print("\n[DEBUG] Watched function hit counts")
        for name in watched_func_names:
            print(f"  {name}: {watched_func_hits.get(name, 0)}")

    print("\n[DEBUG] Function coverage summary")
    for fn, pcs in sorted(function_unique_pcs.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        print(f"  {fn}: unique PCs = {len(pcs)}")

    if DEBUG_LOOP_DETECT and len(recent_pcs) == RECENT_PC_WINDOW:
        uniq = set(recent_pcs)
        if len(uniq) < 16:
            print(f"[WARN] Possible tight loop/stuck state: last {RECENT_PC_WINDOW} instructions touched only {len(uniq)} unique PCs")
    
    print("\n[DEBUG] Key reachability check")
    for key_fn in ["_start", "main", "readMemoryByte", "spectre_function"]:
        print(f"  reached {key_fn}: {'YES' if watched_func_hits.get(key_fn, 0) > 0 else 'NO'}")


    # ============================================================
    # Print summary
    # ============================================================
    print("\n[+] Execution finished")
    print(f"[+] Instructions executed: {inst_count}")
    print(f"[+] CFG edges: {len(cfg_edges)}")
    print(f"[+] DFG edges: {len(dfg_edges)}")
    print(f"[+] Control edges: {len(control_edges)}")
    print(f"[+] Value-node edges: {len(inst_value_node_edges)}")

    print("\n[+] Secret-region direct uses (reads/accesses):", len(secret_use_pcs))
    for pc in sorted(secret_use_pcs):
        info = inst_info.get(pc, {})
        src = format_src(pc, addr2line_map)
        addrs = ", ".join(f"0x{x:x}" for x in sorted(secret_use_details.get(pc, set()))[:8])
        if src:
            print(f"    USE_SECRET 0x{pc:x}  {info.get('disasm', '')}  [addr={addrs}] ; {src}")
        else:
            print(f"    USE_SECRET 0x{pc:x}  {info.get('disasm', '')}  [addr={addrs}]")

    print("\n[+] Secret-region direct defs (writes):", len(secret_def_pcs))
    for pc in sorted(secret_def_pcs):
        info = inst_info.get(pc, {})
        src = format_src(pc, addr2line_map)
        addrs = ", ".join(f"0x{x:x}" for x in sorted(secret_def_details.get(pc, set()))[:8])
        if src:
            print(f"    DEF_SECRET 0x{pc:x}  {info.get('disasm', '')}  [addr={addrs}] ; {src}")
        else:
            print(f"    DEF_SECRET 0x{pc:x}  {info.get('disasm', '')}  [addr={addrs}]")

    print("\n[+] Backward instruction slice from secret-related accesses/defs")
    print(f"    seed pcs                 : {len(secret_seed_pcs)}")
    print(f"    data-only slice pcs      : {len(secret_backward_slice_data)}")
    print(f"    data-only leaf pcs       : {len(secret_leaf_pcs_data)}")
    print(f"    data+control slice pcs   : {len(secret_backward_slice_combined)}")
    print(f"    data+control leaf pcs    : {len(secret_leaf_pcs_combined)}")

    print("\n[+] Leaf instruction PCs (data+control):")
    for pc in sorted(secret_leaf_pcs_combined):
        info = inst_info.get(pc, {})
        src = format_src(pc, addr2line_map)
        tag = []
        if pc in conditional_branch_pcs:
            tag.append("COND_BR")
        if src:
            print(f"    0x{pc:x}  {info.get('disasm', '')} {'[' + ','.join(tag) + ']' if tag else ''} ; {src}")
        else:
            print(f"    0x{pc:x}  {info.get('disasm', '')} {'[' + ','.join(tag) + ']' if tag else ''}")

    print("\n[+] Backward-related register objects:")
    for r in sorted(backward_related_regs):
        print(f"    reg:{r}")

    print("\n[+] Backward-related memory/global objects:")
    mem_objs = sorted(set(classify_mem_object(a) for a in backward_related_mems))
    for m in mem_objs:
        print(f"    {m}")

    print("\n[+] Backward-related immediates seen in data+control slice:")
    for iv in sorted(backward_related_imms):
        print(f"    imm:{iv}")

    print("\n[+] Object-level backward slice from array2-related objects")
    print(f"    seed objects : {len(secret_seed_objects)}")
    print(f"    slice objects: {len(object_backward_slice)}")
    print(f"    leaf objects : {len(object_leaf_slice)}")
    for obj in sorted(object_leaf_slice):
        print(f"    LEAF_OBJ {obj}")

    print("\n[+] Value-node backward slice from secret-related seeds")
    print(f"    seed value nodes : {len(secret_seed_value_nodes)}")
    print(f"    slice value nodes: {len(value_backward_slice)}")
    print(f"    leaf value nodes : {len(value_leaf_slice)}")
    for n in sorted(value_leaf_slice):
        print(f"    LEAF_VALUE {n}")

    # ============================================================
    # Export cfg.dot
    # ============================================================
    with open("cfg.dot", "w") as f:
        f.write("digraph CFG {\n")
        pcs = sorted(set([a for a, _ in cfg_edges] + [b for _, b in cfg_edges]))
        for pc in pcs:
            info = inst_info.get(pc, {})
            src = addr2line_map.get(pc)
            label = [f"0x{pc:x}"]
            if src:
                label.append(f"{src[0]}:{src[1]}")
            if info:
                label.append(info.get("disasm", ""))
                if info.get("plt"):
                    label.append("[PLT]")
                if info.get("external_stub"):
                    label.append(f"[EXT_STUB:{info.get('external_name','?')}]")

            tio = inst_taint_io.get(pc, {})
            if tio:
                if tio["use_regs"] or tio["use_mems"]:
                    label.append("TUSE: " +
                                 ",".join(sorted(map(str, tio["use_regs"]))) +
                                 ("," if tio["use_regs"] and tio["use_mems"] else "") +
                                 ",".join(f"0x{x:x}" for x in sorted(tio["use_mems"])))
                if tio["def_regs"] or tio["def_mems"]:
                    label.append("TDEF: " +
                                 ",".join(sorted(map(str, tio["def_regs"]))) +
                                 ("," if tio["def_regs"] and tio["def_mems"] else "") +
                                 ",".join(f"0x{x:x}" for x in sorted(tio["def_mems"])))

            if pc in conditional_branch_pcs:
                cond_objs = sorted(ctrl_analyzer.branch_condition_objects.get(pc, set()))
                if cond_objs:
                    label.append("COND: " + ",".join(cond_objs[:8]))

            color = "red" if inst_uses_taint.get(pc, False) else "black"
            if pc in secret_use_pcs:
                color = "orange"
            if pc in secret_def_pcs:
                color = "red"
            if pc in conditional_branch_pcs:
                color = "purple"
            if info.get("external_stub"):
                color = "brown"

            label_text = esc("\\n".join(label))
            f.write(f'  "0x{pc:x}" [label="{label_text}", color="{color}"];\n')

        for a, b in sorted(cfg_edges):
            f.write(f'  "0x{a:x}" -> "0x{b:x}";\n')
        f.write("}\n")

    # ============================================================
    # Build BB CFG
    # ============================================================
    succs = defaultdict(set)
    preds = defaultdict(set)
    pcs_all = set()
    for a, b in cfg_edges:
        succs[a].add(b)
        preds[b].add(a)
        pcs_all.add(a)
        pcs_all.add(b)

    def is_terminator(pc):
        info = inst_info.get(pc, {})
        d = info.get("disasm", "").lower()
        return d.startswith("j") or d.startswith("call") or d.startswith("ret") or d.startswith("hlt")

    sorted_pcs = sorted(pcs_all)
    visited = set()
    blocks = []
    pc_to_block = {}

    for pc in sorted_pcs:
        if pc in visited:
            continue

        head = pc
        while True:
            pp = list(preds.get(head, []))
            if len(pp) != 1:
                break
            pred = pp[0]
            if len(succs.get(pred, [])) != 1:
                break
            if is_terminator(pred):
                break
            if pred in visited:
                break
            head = pred

        block = []
        cur = head
        while True:
            if cur in visited:
                break
            block.append(cur)
            visited.add(cur)
            pc_to_block[cur] = len(blocks)

            if is_terminator(cur):
                break

            ss = list(succs.get(cur, []))
            if len(ss) != 1:
                break
            nxt = ss[0]
            if len(preds.get(nxt, [])) != 1:
                break
            cur = nxt

        if block:
            blocks.append(block)

    bb_edges = set()
    for a, b in cfg_edges:
        if a in pc_to_block and b in pc_to_block:
            ba = pc_to_block[a]
            bb = pc_to_block[b]
            if ba != bb:
                bb_edges.add((ba, bb))

    with open("cfg_bb.dot", "w") as f:
        f.write("digraph CFG_BB {\n")
        for idx, block in enumerate(blocks):
            lines = [f"BB{idx}"]
            for pc in block:
                info = inst_info.get(pc, {})
                src = addr2line_map.get(pc)
                line = f"0x{pc:x}: {info.get('disasm', '')}"
                if src:
                    line += f" ; {src[0]}:{src[1]}"
                if info.get("plt"):
                    line += " [PLT]"
                if info.get("external_stub"):
                    line += f" [EXT_STUB:{info.get('external_name','?')}]"
                lines.append(line)

                if pc in conditional_branch_pcs:
                    cond_objs = sorted(ctrl_analyzer.branch_condition_objects.get(pc, set()))
                    if cond_objs:
                        lines.append("  [COND: " + ",".join(cond_objs[:6]) + "]")

                tio = inst_taint_io.get(pc, {})
                if tio:
                    tparts = []
                    if tio["use_regs"] or tio["use_mems"]:
                        tparts.append("TUSE")
                    if tio["def_regs"] or tio["def_mems"]:
                        tparts.append("TDEF")
                    if tparts:
                        lines.append("  [" + ",".join(tparts) + "]")

            color = "black"
            if any(inst_uses_taint.get(pc, False) for pc in block):
                color = "red"
            if any(pc in secret_use_pcs for pc in block):
                color = "orange"
            if any(pc in secret_def_pcs for pc in block):
                color = "red"
            if any(pc in conditional_branch_pcs for pc in block):
                color = "purple"
            if any(inst_info.get(pc, {}).get("external_stub") for pc in block):
                color = "brown"

            label_text = esc("\\n".join(lines))
            f.write(f'  "BB{idx}" [shape=box, label="{label_text}", color="{color}"];\n')

        for a, b in sorted(bb_edges):
            f.write(f'  "BB{a}" -> "BB{b}";\n')
        f.write("}\n")

    # ============================================================
    # Export dfg.dot
    # ============================================================
    with open("dfg.dot", "w") as f:
        f.write("digraph DFG {\n")
        pcs = sorted(set([a for a, _ in dfg_edges] + [b for _, b in dfg_edges]))
        for pc in pcs:
            info = inst_info.get(pc, {})
            src = addr2line_map.get(pc)
            label = [f"0x{pc:x}"]
            if src:
                label.append(f"{src[0]}:{src[1]}")
            if info:
                label.append(info.get("disasm", ""))
                if info.get("plt"):
                    label.append("[PLT]")
                if info.get("external_stub"):
                    label.append(f"[EXT_STUB:{info.get('external_name','?')}]")

            rw = inst_rw.get(pc, {})
            if rw:
                if rw["read_regs"]:
                    label.append("RReg: " + ",".join(sorted(rw["read_regs"])))
                if rw["write_regs"]:
                    label.append("WReg: " + ",".join(sorted(rw["write_regs"])))
                if inst_immediates.get(pc):
                    label.append("Imm: " + ",".join(str(x) for x in sorted(inst_immediates[pc])))

            color = "black"
            if inst_uses_taint.get(pc, False):
                color = "red"
            if pc in secret_use_pcs:
                color = "orange"
            if pc in secret_def_pcs:
                color = "red"
            if pc in conditional_branch_pcs:
                color = "purple"
            if info.get("external_stub"):
                color = "brown"

            label_text = esc("\\n".join(label))
            f.write(f'  "0x{pc:x}" [label="{label_text}", color="{color}"];\n')

        for a, b in sorted(dfg_edges):
            color = "red" if (inst_uses_taint.get(a, False) or inst_uses_taint.get(b, False)) else "blue"
            if a in secret_backward_slice_combined and b in secret_backward_slice_combined:
                color = "darkgreen"
            f.write(f'  "0x{a:x}" -> "0x{b:x}" [color="{color}"];\n')
        f.write("}\n")

    # ============================================================
    # Export control.dot
    # ============================================================
    with open("control.dot", "w") as f:
        f.write("digraph CONTROL {\n")
        pcs = sorted(set(list(conditional_branch_pcs) + [x for _, x in control_edges]))
        for pc in pcs:
            info = inst_info.get(pc, {})
            src = addr2line_map.get(pc)
            label = [f"0x{pc:x}"]
            if src:
                label.append(f"{src[0]}:{src[1]}")
            if info:
                label.append(info.get("disasm", ""))
                if info.get("plt"):
                    label.append("[PLT]")
                if info.get("external_stub"):
                    label.append(f"[EXT_STUB:{info.get('external_name','?')}]")

            if pc in conditional_branch_pcs:
                conds = sorted(ctrl_analyzer.branch_condition_objects.get(pc, set()))
                if conds:
                    label.append("COND: " + ",".join(conds[:10]))

            color = "black"
            if pc in conditional_branch_pcs:
                color = "purple"
            if pc in secret_use_pcs:
                color = "orange"
            if pc in secret_def_pcs:
                color = "red"
            if info.get("external_stub"):
                color = "brown"

            label_text = esc("\\n".join(label))
            f.write(f'  "0x{pc:x}" [label="{label_text}", color="{color}"];\n')

        for a, b in sorted(control_edges):
            f.write(f'  "0x{a:x}" -> "0x{b:x}" [color="purple", style="dashed"];\n')
        f.write("}\n")

    # ============================================================
    # Export cdfg.dot
    # ============================================================
    with open("cdfg.dot", "w") as f:
        f.write("digraph CDFG {\n")
        pcs = sorted(set(list(inst_info.keys())))
        for pc in pcs:
            info = inst_info.get(pc, {})
            src = addr2line_map.get(pc)
            label = [f"0x{pc:x}"]
            if src:
                label.append(f"{src[0]}:{src[1]}")
            if info:
                label.append(info.get("disasm", ""))
                if info.get("plt"):
                    label.append("[PLT]")
                if info.get("external_stub"):
                    label.append(f"[EXT_STUB:{info.get('external_name','?')}]")

            if pc in secret_use_pcs:
                label.append("[SECRET_USE]")
            if pc in secret_def_pcs:
                label.append("[SECRET_DEF]")
            if pc in secret_leaf_pcs_combined:
                label.append("[BWD_LEAF]")
            if pc in conditional_branch_pcs:
                label.append("[COND_BR]")

            color = "black"
            if inst_uses_taint.get(pc, False):
                color = "red"
            if pc in secret_use_pcs:
                color = "orange"
            if pc in secret_def_pcs:
                color = "red"
            if pc in secret_leaf_pcs_combined:
                color = "blue"
            if pc in conditional_branch_pcs:
                color = "purple"
            if info.get("external_stub"):
                color = "brown"

            label_text = esc("\\n".join(label))
            f.write(f'  "0x{pc:x}" [label="{label_text}", color="{color}"];\n')

        for a, b in sorted(cfg_edges):
            f.write(f'  "0x{a:x}" -> "0x{b:x}" [color="black"];\n')
        for a, b in sorted(dfg_edges):
            col = "blue"
            style = "dashed"
            if a in secret_backward_slice_combined and b in secret_backward_slice_combined:
                col = "darkgreen"
                style = "bold"
            f.write(f'  "0x{a:x}" -> "0x{b:x}" [color="{col}", style="{style}"];\n')
        for a, b in sorted(control_edges):
            f.write(f'  "0x{a:x}" -> "0x{b:x}" [color="purple", style="dotted"];\n')
        f.write("}\n")

    # ============================================================
    # Export backward_secret.dot
    # ============================================================
    with open("backward_secret.dot", "w") as f:
        f.write("digraph BACKWARD_SECRET {\n")
        for pc in sorted(secret_backward_slice_combined):
            info = inst_info.get(pc, {})
            src = addr2line_map.get(pc)
            label = [f"0x{pc:x}"]
            if src:
                label.append(f"{src[0]}:{src[1]}")
            label.append(info.get("disasm", ""))
            if info.get("plt"):
                label.append("[PLT]")
            if info.get("external_stub"):
                label.append(f"[EXT_STUB:{info.get('external_name','?')}]")

            rw = inst_rw.get(pc, {})
            if rw.get("read_regs"):
                label.append("RReg: " + ",".join(sorted(rw["read_regs"])))
            if rw.get("write_regs"):
                label.append("WReg: " + ",".join(sorted(rw["write_regs"])))

            mem_reads = rw.get("read_mems", set())
            mem_writes = rw.get("write_mems", set())
            if mem_reads:
                label.append("RMem: " + ",".join(sorted(classify_mem_object(a) for a in mem_reads)[:6]))
            if mem_writes:
                label.append("WMem: " + ",".join(sorted(classify_mem_object(a) for a in mem_writes)[:6]))

            if inst_immediates.get(pc):
                label.append("Imm: " + ",".join(str(x) for x in sorted(inst_immediates[pc])))

            if pc in conditional_branch_pcs:
                conds = sorted(ctrl_analyzer.branch_condition_objects.get(pc, set()))
                if conds:
                    label.append("COND: " + ",".join(conds[:8]))

            color = "black"
            if pc in secret_use_pcs:
                color = "orange"
            if pc in secret_def_pcs:
                color = "red"
            if pc in secret_leaf_pcs_combined:
                color = "blue"
            if pc in conditional_branch_pcs:
                color = "purple"
            if info.get("external_stub"):
                color = "brown"

            label_text = esc("\\n".join(label))
            f.write(f'  "0x{pc:x}" [label="{label_text}", color="{color}"];\n')

        for use_pc in sorted(secret_backward_slice_combined):
            for def_pc in combined_reverse_deps.get(use_pc, set()):
                if def_pc in secret_backward_slice_combined:
                    edge_color = "darkgreen"
                    edge_style = "solid" if def_pc in reverse_dfg.get(use_pc, set()) else "dotted"
                    f.write(f'  "0x{def_pc:x}" -> "0x{use_pc:x}" [color="{edge_color}", style="{edge_style}"];\n')
        f.write("}\n")

    # ============================================================
    # Export object_backward.dot
    # ============================================================
    with open("object_backward.dot", "w") as f:
        f.write("digraph OBJECT_BACKWARD {\n")

        for obj in sorted(object_backward_slice):
            color = "black"
            if obj in secret_seed_objects:
                color = "red"
            elif obj in object_leaf_slice:
                color = "blue"
            elif obj.startswith("imm:"):
                color = "purple"
            f.write(f'  "{esc(obj)}" [label="{esc(obj)}", color="{color}"];\n')

        for dst in sorted(object_backward_slice):
            for src in object_rev_deps.get(dst, set()):
                if src in object_backward_slice:
                    f.write(f'  "{esc(src)}" -> "{esc(dst)}";\n')

        f.write("}\n")

    # ============================================================
    # Export value_backward.dot
    # ============================================================
    with open("value_backward.dot", "w") as f:
        f.write("digraph VALUE_BACKWARD {\n")

        for n in sorted(value_backward_slice):
            color = "black"
            if n in secret_seed_value_nodes:
                color = "red"
            elif n in value_leaf_slice:
                color = "blue"
            elif n.startswith("imm:"):
                color = "purple"
            elif n.startswith("pc:"):
                try:
                    pc = int(n.split(":0x", 1)[1], 16)
                    if pc in conditional_branch_pcs:
                        color = "purple"
                    if inst_info.get(pc, {}).get("external_stub"):
                        color = "brown"
                except Exception:
                    pass
            f.write(f'  "{esc(n)}" [label="{esc(n)}", color="{color}"];\n')

        for dst in sorted(value_backward_slice):
            for src in value_node_rev_edges.get(dst, set()):
                if src in value_backward_slice:
                    f.write(f'  "{esc(src)}" -> "{esc(dst)}";\n')

        f.write("}\n")

    print("\n[+] DOT files generated:")
    print("    cfg.dot")
    print("    cfg_bb.dot")
    print("    dfg.dot")
    print("    control.dot")
    print("    cdfg.dot")
    print("    backward_secret.dot")
    print("    object_backward.dot")
    print("    value_backward.dot")


if __name__ == '__main__':
    main()