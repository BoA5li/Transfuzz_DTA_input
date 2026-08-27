#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Triton 动态污点 + 双向依赖分析（增强版，方向1 + 方向2 + 方向3 + 方向4 + 方向5 + 方向6）

方向 1：静态后支配 + 动态轨迹混合控制依赖
方向 2：seed-driven / slice-driven 重建
方向 3：对象去重 / 规范化
方向 4：循环稳态摘要 / 重复依赖事实聚合
方向 5：路径报告优先 + 仅导出 seed slice / 局部视图 DOT
方向 6：可配置后处理 / 可配置导出（fast / balanced / full）

本修订版在保持原有主流程与导出逻辑不变的基础上，补充了以下建模优化：
  A. immediate 从“值级对象”改为“出现点 / 语义站点级对象”
     - 不再把全程序同值同宽的立即数合并为 imm:0x0:i32 这一类全局节点
     - 统一改为 imm_occurrence:<pc>:<source_kind>:<operand_index>:<value>:<width>
     - 直接减少多个语义不同的 0 / 1 / 位移常量互相污染的问题

  B. immediate 语义标签
     - 在分析器阶段直接给 immediate 节点打标签，区分：
       comparison_constant / store_constant / loop_bound_constant
       stack_alignment_constant / rip_relative_displacement / plt_got_offset
       frame_offset_constant / address_scale_constant 等

  C. 寄存器对象语义角色标签
     - 在保持 reg:<parent> 节点 ID 不变的前提下，为其补充语义标签：
       carrier / controlling_operand / address_base / address_index
       transient_move_only_carrier / address_segment 等

  D. ABI / 序言尾声 / 脚手架指令标签
     - 在指令级别补充：
       prologue / epilogue / stack_alignment / argument_shuffle
       callee_save_spill / callee_save_restore
     - 后续筛选器可以直接利用这些标签降权或排除，而不需要重复猜测
"""

import argparse
import json
import sys
import time
from collections import defaultdict, deque
from elftools.elf.elffile import ELFFile
from triton import TritonContext, ARCH, Instruction, MemoryAccess, OPERAND
# === 方案2修订：导入辅助模块 ===
from revision_helpers import (
    is_self_zero_idiom,
    is_partial_write_rmw,
    MemoryAliasTracker,
    get_caller_saved_canonical_oids,
    recover_weakly_connected_nodes,
)


# ------------------------------------------------------------------------
# 配置项
# ------------------------------------------------------------------------
TAINT_SYMBOL_NAME = 'array2'
DEFAULT_SECRET_LEN = 256 * 512

# 混合控制依赖展开模式：
#   none      -> 不建立控制依赖边
#   def-only  -> 仅对受分支控制的“定义对象”加 control 边
#   all       -> 对受分支控制的指令全部建立 inst 控制边，并把条件对象连到该指令定义对象
CONTROL_EXPANSION_MODE = 'all'

# 为避免异常程序无限执行，增加一个保底阈值
MAX_INSTRUCTIONS = 10_000_000

# ------------------------------------------------------------------------
# 方向5：路径报告优先 / 局部 DOT 视图
# ------------------------------------------------------------------------
OBJECT_DOT_VIEW = 'combined'    # combined | backward | forward | neighborhood
INST_DOT_VIEW = 'slice'         # slice | backward | forward | neighborhood
DOT_NEIGHBORHOOD_HOPS = 2

PATH_REPORT_ENABLED = True
PATH_REPORT_MAX_DEPTH = 48
PATH_REPORT_PER_TARGET = 3
PATH_REPORT_TOP_TARGETS = 32
PATH_REPORT_EDGE_PCS_LIMIT = 8

# ------------------------------------------------------------------------
# 方向6：后处理 / 输出模式
# ------------------------------------------------------------------------
POSTPROCESS_MODE = 'full'   # fast | balanced | full
OUTPUT_PREFIX = ''          # 例如 'run1_'；为空则保持当前文件名
SUMMARY_SCOPE = 'full'      # minimal | slice | full，可被模式覆盖

# 默认沿用当前 full 语义；不同模式仅裁剪导出/摘要，不改变主分析目标
MODE_PROFILES = {
    'fast': {
        'control_expansion_mode': 'def-only',
        'export_cfg': False,
        'export_cfg_bb': False,
        'export_inst_dep': False,
        'export_object_dep': False,
        'export_cdfg': False,
        'export_summary_json': True,
        'export_path_report': True,
        'summary_scope': 'minimal',
        'path_report_max_depth': 32,
        'path_report_per_target': 2,
        'path_report_top_targets': 16,
        'object_dot_view': 'combined',
        'inst_dot_view': 'slice',
        'dot_neighborhood_hops': 2,
    },
    'balanced': {
        'control_expansion_mode': 'def-only',
        'export_cfg': False,
        'export_cfg_bb': False,
        'export_inst_dep': True,
        'export_object_dep': True,
        'export_cdfg': True,
        'export_summary_json': True,
        'export_path_report': True,
        'summary_scope': 'slice',
        'path_report_max_depth': 48,
        'path_report_per_target': 3,
        'path_report_top_targets': 24,
        'object_dot_view': 'combined',
        'inst_dot_view': 'slice',
        'dot_neighborhood_hops': 2,
    },
    'full': {
        'control_expansion_mode': 'all',
        'export_cfg': True,
        'export_cfg_bb': True,
        'export_inst_dep': True,
        'export_object_dep': True,
        'export_cdfg': True,
        'export_summary_json': True,
        'export_path_report': True,
        'summary_scope': 'full',
        'path_report_max_depth': 64,
        'path_report_per_target': 4,
        'path_report_top_targets': 32,
        'object_dot_view': 'combined',
        'inst_dot_view': 'slice',
        'dot_neighborhood_hops': 2,
    },
}

# ------------------------------------------------------------------------
# 调试观测配置（最小侵入，不改变分析语义）
# ------------------------------------------------------------------------
DEBUG_PROGRESS = True
DEBUG_PROGRESS_EVERY = 20000

DEBUG_HOTSPOT = True
DEBUG_HOTSPOT_EVERY = 100000
DEBUG_HOTSPOT_TOPN = 6

DEBUG_CTRL_VERBOSE = False
DEBUG_CTRL_WARN_THRESHOLD = 32

DEBUG_PC_STALL_WARN = True
DEBUG_PC_STALL_THRESHOLD = 50000

# ------------------------------------------------------------------------
# 方向4：循环稳态摘要 / 重复依赖事实聚合
# ------------------------------------------------------------------------
LOOP_SUMMARIZATION_ENABLED = True

# 首次看到某个“动态依赖事实签名”时正常记录；后续重复直接聚合计数，不再重复写入事实结构。
LOOP_SUMMARIZATION_SUPPRESS_AFTER = 1

# 为避免 pattern 表自身无界增长，可设置一个保底上限；达到后对“新签名”不再做摘要，仅继续正常记录。
LOOP_SUMMARIZATION_MAX_PATTERNS = 200000

# 调试输出中打印 top-N 高频重复模式
LOOP_SUMMARIZATION_TOPN = 10

# 签名中是否纳入当前在线控制上下文
LOOP_SUMMARIZATION_INCLUDE_CONTROL = True

# ------------------------------------------------------------------------
# 语义标签常量
# ------------------------------------------------------------------------
ARG_REGS = {
    'rdi', 'rsi', 'rdx', 'rcx', 'r8', 'r9',
    'edi', 'esi', 'edx', 'ecx', 'r8d', 'r9d',
    'di', 'si', 'dx', 'cx', 'r8w', 'r9w',
    'dil', 'sil', 'dl', 'cl', 'r8b', 'r9b',
}

CALLEE_SAVED_REGS = {
    'rbx', 'rbp', 'r12', 'r13', 'r14', 'r15',
    'ebx', 'ebp', 'r12d', 'r13d', 'r14d', 'r15d',
    'bx', 'bp', 'r12w', 'r13w', 'r14w', 'r15w',
    'bl', 'bpl', 'r12b', 'r13b', 'r14b', 'r15b',
}

MOVE_LIKE_OPCODES = {
    'mov', 'movabs', 'movzx', 'movsx', 'movsxd', 'lea',
}

COMPARE_LIKE_OPCODES = {
    'cmp', 'test', 'ucomiss', 'ucomisd', 'comiss', 'comisd',
}

# ------------------------------------------------------------------------
# 命令行 / 模式辅助
# ------------------------------------------------------------------------
def parse_args(argv):
    parser = argparse.ArgumentParser(
        description='Triton dynamic taint + bidirectional dependency analyzer'
    )
    parser.add_argument('binary', help='ELF path to analyze')
    parser.add_argument(
        '--mode',
        choices=sorted(MODE_PROFILES.keys()),
        default=POSTPROCESS_MODE,
        help=f'postprocess/export mode (default: {POSTPROCESS_MODE})'
    )
    parser.add_argument(
        '--control-mode',
        choices=('none', 'def-only', 'all'),
        default=None,
        help='override control expansion mode'
    )
    parser.add_argument(
        '--max-insts',
        type=int,
        default=MAX_INSTRUCTIONS,
        help=f'max executed instructions (default: {MAX_INSTRUCTIONS})'
    )
    parser.add_argument(
        '--secret-symbol',
        default=TAINT_SYMBOL_NAME,
        help=f'taint source global symbol (default: {TAINT_SYMBOL_NAME})'
    )
    parser.add_argument(
        '--secret-len',
        type=int,
        default=DEFAULT_SECRET_LEN,
        help=f'default taint source size when ELF symbol size is zero (default: {DEFAULT_SECRET_LEN})'
    )
    parser.add_argument(
        '--output-prefix',
        default=OUTPUT_PREFIX,
        help='prefix for exported files, e.g. run1_'
    )
    parser.add_argument(
        '--path-report',
        dest='path_report',
        action='store_true',
        default=None,
        help='force enable path report export'
    )
    parser.add_argument(
        '--no-path-report',
        dest='path_report',
        action='store_false',
        help='force disable path report export'
    )
    parser.add_argument(
        '--path-depth',
        type=int,
        default=None,
        help='override path report max BFS depth'
    )
    parser.add_argument(
        '--path-per-target',
        type=int,
        default=None,
        help='override number of representative paths per target'
    )
    parser.add_argument(
        '--object-dot-view',
        choices=('combined', 'backward', 'forward', 'neighborhood'),
        default=None,
        help='override object DOT view (seed slice / local neighborhood only)'
    )
    parser.add_argument(
        '--inst-dot-view',
        choices=('slice', 'backward', 'forward', 'neighborhood'),
        default=None,
        help='override instruction DOT view (seed slice / local neighborhood only)'
    )
    parser.add_argument(
        '--neighborhood-hops',
        type=int,
        default=None,
        help='override neighborhood DOT hop budget'
    )
    return parser.parse_args(argv)


def resolve_mode_options(args):
    profile = dict(MODE_PROFILES[args.mode])

    if args.control_mode is not None:
        profile['control_expansion_mode'] = args.control_mode

    if args.path_report is not None:
        profile['export_path_report'] = bool(args.path_report)

    if args.path_depth is not None and args.path_depth > 0:
        profile['path_report_max_depth'] = int(args.path_depth)

    if args.path_per_target is not None and args.path_per_target > 0:
        profile['path_report_per_target'] = int(args.path_per_target)

    if args.object_dot_view is not None:
        profile['object_dot_view'] = args.object_dot_view

    if args.inst_dot_view is not None:
        profile['inst_dot_view'] = args.inst_dot_view

    if args.neighborhood_hops is not None and args.neighborhood_hops > 0:
        profile['dot_neighborhood_hops'] = int(args.neighborhood_hops)

    profile['max_insts'] = int(args.max_insts)
    profile['secret_symbol'] = args.secret_symbol
    profile['secret_len'] = int(args.secret_len)
    profile['output_prefix'] = args.output_prefix or ''
    profile['mode'] = args.mode
    return profile


def prefixed_name(prefix, filename):
    return f'{prefix}{filename}' if prefix else filename


def build_minimal_sysv_process_vector(stack_addr, stack_size, argv=('prog',)):
    """
    构造 Linux/SysV AMD64 进程入口所需的最小初始栈布局。

    ELF ``e_entry`` 指向的 ``_start`` 并不按 ``main`` 的函数调用约定接收
    ``rdi``/``rsi``；它从初始 ``rsp`` 读取如下数据：

      [rsp]            argc
      [rsp + 8]        argv[0] -> NUL 结尾字符串
      ...
      argv[argc]       NULL
      envp[0]          NULL
      auxv[0]          AT_NULL, 0

    返回纯数据描述，便于在不依赖 Triton 的单元测试中验证 ABI 布局。
    """
    if not isinstance(stack_addr, int) or not isinstance(stack_size, int):
        raise TypeError('stack_addr and stack_size must be integers')
    if stack_size <= 0:
        raise ValueError('stack_size must be positive')

    encoded_args = []
    for arg in argv:
        if isinstance(arg, str):
            raw = arg.encode('utf-8')
        elif isinstance(arg, (bytes, bytearray)):
            raw = bytes(arg)
        else:
            raise TypeError('argv entries must be str or bytes')
        if b'\0' in raw:
            raise ValueError('argv entries must not contain embedded NUL bytes')
        encoded_args.append(raw + b'\0')

    pointer_size = 8
    stack_end = stack_addr + stack_size
    # 在栈顶下方保留空间，且保持 Linux x86-64 入口要求的 16 字节对齐。
    initial_rsp = (stack_end - 0x1000) & ~0xF
    if initial_rsp < stack_addr:
        raise ValueError('stack region is too small for the initial process stack')

    argc = len(encoded_args)
    argv_addr = initial_rsp + pointer_size
    envp_addr = argv_addr + (argc + 1) * pointer_size
    auxv_addr = envp_addr + pointer_size

    # argc + argv 指针与 NULL + envp NULL + AT_NULL/value 两个字。
    entry_word_count = 1 + argc + 1 + 1 + 2
    string_cursor = (initial_rsp + entry_word_count * pointer_size + 0xF) & ~0xF

    arg_addresses = []
    string_writes = []
    for raw in encoded_args:
        arg_addresses.append(string_cursor)
        string_writes.append((string_cursor, raw))
        string_cursor += len(raw)

    if string_cursor > stack_end:
        raise ValueError('argv layout does not fit in the configured stack region')

    entry_stack_values = [argc] + arg_addresses + [0, 0, 0, 0]
    entry_stack_image = b''.join(
        value.to_bytes(pointer_size, byteorder='little', signed=False)
        for value in entry_stack_values
    )

    return {
        'initial_rsp': initial_rsp,
        'argc': argc,
        'argv_addr': argv_addr,
        'envp_addr': envp_addr,
        'auxv_addr': auxv_addr,
        'entry_stack_image': entry_stack_image,
        'arg_addresses': tuple(arg_addresses),
        'string_writes': tuple(string_writes),
    }


def derive_main_process_args(argc, argv_addr, stack_addr, stack_size):
    """校验 libc 启动参数并推导 ``main(argc, argv, envp)`` 的三个参数。"""
    if not all(isinstance(value, int) for value in (
        argc, argv_addr, stack_addr, stack_size
    )):
        raise TypeError('process argument values must be integers')
    if argc < 0 or argc > 4096:
        raise ValueError(f'invalid argc: {argc}')
    if stack_size <= 0:
        raise ValueError('stack_size must be positive')

    argv_table_end = argv_addr + (argc + 1) * 8
    if not (
        stack_addr <= argv_addr
        and argv_table_end + 8 <= stack_addr + stack_size
    ):
        raise ValueError('argv is outside the configured stack region')

    return argc, argv_addr, argv_table_end


def taint_memory_region(ctx, start_addr, size):
    """
    仅使用 Triton 污点引擎标记内存区域，不创建逐字节符号变量。

    当前分析器通过 ``isRegisterTainted`` / ``isMemoryTainted`` 提取动态
    依赖关系，并未消费符号 AST 或路径约束。避免调用 ``symbolizeMemory``
    可防止大型污点源产生与分析结果无关的符号化时间和内存开销。
    """
    if not isinstance(start_addr, int) or isinstance(start_addr, bool):
        raise TypeError('start_addr must be an integer')
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError('size must be an integer')
    if start_addr < 0:
        raise ValueError('start_addr must be non-negative')
    if size < 0:
        raise ValueError('size must be non-negative')

    for offset in range(size):
        ctx.taintMemory(MemoryAccess(start_addr + offset, 1))


# ------------------------------------------------------------------------
# ELF / 符号 / 调试信息辅助
# ------------------------------------------------------------------------
def load_all_code_segments(path):
    """加载所有 PT_LOAD 以及关键代码段，返回 [(vaddr, bytes)], entry。"""
    segs = []
    e_entry = None
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        e_entry = elf.header['e_entry']

        for seg in elf.iter_segments():
            if seg['p_type'] == 'PT_LOAD':
                segs.append((seg['p_vaddr'], seg.data()))

        for secname in ('.text', '.plt', '.plt.sec'):
            sec = elf.get_section_by_name(secname)
            if sec:
                segs.append((sec['sh_addr'], sec.data()))

    return segs, e_entry


def build_addr2line_map(path):
    """地址 -> (文件名, 行号)"""
    mapping = {}
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        if not elf.has_dwarf_info():
            return mapping
        dwarfinfo = elf.get_dwarf_info()
        for cu in dwarfinfo.iter_CUs():
            lp = dwarfinfo.line_program_for_CU(cu)
            if lp is None:
                continue
            for entry in lp.get_entries():
                if entry.state is None:
                    continue
                state = entry.state
                if state.end_sequence:
                    continue
                file_index = state.file
                line = state.line
                try:
                    filename = lp['file_entry'][file_index - 1].name.decode(errors='ignore')
                except Exception:
                    filename = f'<file#{file_index}>'
                mapping[state.address] = (filename, line)
    return mapping


def build_symbol_addr_map(path):
    """地址 -> 符号名（函数/对象都可能出现）"""
    symmap = {}
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        symtab = elf.get_section_by_name('.symtab')
        if not symtab:
            return symmap
        for sym in symtab.iter_symbols():
            addr = sym.entry['st_value']
            if addr != 0:
                symmap[addr] = sym.name
    return symmap


def build_global_objects(path):
    """
    收集全局对象符号。
    返回：
      - objects: [{name, addr, size, type}, ...] 按 addr 排序
      - by_addr: {addr: name}
    """
    objects = []
    by_addr = {}
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        symtab = elf.get_section_by_name('.symtab')
        if not symtab:
            return objects, by_addr

        for sym in symtab.iter_symbols():
            addr = sym.entry['st_value']
            name = sym.name
            if addr == 0 or not name:
                continue
            st_info = sym.entry.get('st_info', None)
            st_type = None
            if st_info is not None:
                try:
                    st_type = st_info['type']
                except Exception:
                    st_type = None

            if st_type in ('STT_OBJECT', 'STT_COMMON', 'STT_NOTYPE', None):
                size = int(sym.entry.get('st_size', 0) or 0)
                objects.append({
                    'name': name,
                    'addr': int(addr),
                    'size': size,
                    'type': st_type,
                })
                by_addr[int(addr)] = name

    objects.sort(key=lambda x: x['addr'])
    return objects, by_addr


def build_got_plt_map(path):
    """解析 .got/.got.plt relocation，返回 {got_entry_addr: symbol_name}。"""
    got_map = {}
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        relsecs = []
        for name in ('.rela.plt', '.rel.plt', '.rela.dyn', '.rel.dyn'):
            sec = elf.get_section_by_name(name)
            if sec:
                relsecs.append(sec)
        dynsym = elf.get_section_by_name('.dynsym')
        if not dynsym:
            return got_map

        for sec in relsecs:
            for rel in sec.iter_relocations():
                sym = dynsym.get_symbol(rel.entry['r_info_sym'])
                got_map[int(rel.entry['r_offset'])] = sym.name
    return got_map


def get_main_and_plt_ranges(path):
    main_addr = None
    plt_ranges = []
    text_end = None
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        symtab = elf.get_section_by_name('.symtab')
        if symtab:
            for sym in symtab.iter_symbols():
                if sym.name == 'main':
                    main_addr = int(sym.entry['st_value'])
                    break

        for secname in ('.plt', '.plt.sec'):
            sec = elf.get_section_by_name(secname)
            if sec:
                start = int(sec['sh_addr'])
                end = start + int(sec['sh_size'])
                plt_ranges.append((start, end))

        text_sec = elf.get_section_by_name('.text')
        if text_sec:
            text_end = int(text_sec['sh_addr']) + int(text_sec['sh_size'])

    return main_addr, plt_ranges, text_end


def build_function_ranges(path):
    """从 ELF 函数符号恢复 ``[(start, end, name)]``，供函数内 CFG 使用。"""
    ranges = []
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        for table_name in ('.symtab', '.dynsym'):
            symtab = elf.get_section_by_name(table_name)
            if not symtab:
                continue
            for sym in symtab.iter_symbols():
                try:
                    info = sym.entry['st_info']
                    if info['type'] != 'STT_FUNC':
                        continue
                    start = int(sym.entry['st_value'])
                    size = int(sym.entry['st_size'])
                    shndx = sym.entry['st_shndx']
                except Exception:
                    continue
                if start <= 0 or size <= 0 or shndx == 'SHN_UNDEF':
                    continue
                ranges.append((start, start + size, sym.name or f'sub_{start:x}'))

    # 同一函数可能同时出现在 symtab/dynsym；按范围去重。
    unique = {}
    for start, end, name in ranges:
        unique.setdefault((start, end), name)
    return [
        (start, end, unique[(start, end)])
        for start, end in sorted(unique)
    ]


def compute_postdominators(nodes, successors):
    """
    在虚拟统一出口下计算后支配集合和直接后支配节点。

    只返回能够到达某个真实出口的节点；无法到达出口的无限区域被列入
    ``unresolved_nodes``，调用方不得将其当作严格控制依赖证据。
    """
    nodes = {node for node in nodes if _is_pc(node)}
    succ = {
        node: {dst for dst in successors.get(node, set()) if dst in nodes}
        for node in nodes
    }
    exits = {node for node in nodes if not succ[node]}
    if not nodes or not exits:
        return {
            'postdominators': {},
            'immediate_postdominators': {},
            'exits': exits,
            'unresolved_nodes': set(nodes),
        }

    predecessors = defaultdict(set)
    for src, dsts in succ.items():
        for dst in dsts:
            predecessors[dst].add(src)

    can_reach_exit = set(exits)
    queue = deque(exits)
    while queue:
        node = queue.popleft()
        for pred in predecessors.get(node, set()):
            if pred not in can_reach_exit:
                can_reach_exit.add(pred)
                queue.append(pred)

    unresolved = nodes - can_reach_exit
    virtual_exit = object()
    universe = set(can_reach_exit) | {virtual_exit}
    postdom = {virtual_exit: {virtual_exit}}
    for node in can_reach_exit:
        postdom[node] = set(universe)

    changed = True
    while changed:
        changed = False
        for node in can_reach_exit:
            node_succ = succ[node] & can_reach_exit
            if not node_succ:
                node_succ = {virtual_exit}
            intersection = set(universe)
            for dst in node_succ:
                intersection.intersection_update(postdom[dst])
            updated = {node} | intersection
            if updated != postdom[node]:
                postdom[node] = updated
                changed = True

    clean_postdom = {
        node: {item for item in values if item is not virtual_exit}
        for node, values in postdom.items()
        if node is not virtual_exit
    }
    immediate = {}
    for node, values in clean_postdom.items():
        strict = values - {node}
        candidates = [
            candidate for candidate in strict
            if not any(
                candidate in clean_postdom.get(other, set())
                for other in strict if other != candidate
            )
        ]
        immediate[node] = candidates[0] if len(candidates) == 1 else None

    return {
        'postdominators': clean_postdom,
        'immediate_postdominators': immediate,
        'exits': exits,
        'unresolved_nodes': unresolved,
    }


def build_control_regions(nodes, successors):
    """为每条条件 CFG 边计算由后支配定义的控制区域。"""
    result = compute_postdominators(nodes, successors)
    if result['unresolved_nodes']:
        return {}, result

    postdom = result['postdominators']
    immediate = result['immediate_postdominators']
    branch_regions = {}
    for branch_pc in nodes:
        branch_succ = {
            dst for dst in successors.get(branch_pc, set()) if dst in nodes
        }
        if len(branch_succ) < 2 or branch_pc not in postdom:
            continue
        successor_regions = {}
        for successor in branch_succ:
            region = set(postdom.get(successor, set())) - set(postdom[branch_pc])
            region.discard(branch_pc)
            successor_regions[successor] = region
        branch_regions[branch_pc] = {
            'successor_regions': successor_regions,
            'merge_pc': immediate.get(branch_pc),
        }
    return branch_regions, result


def recover_function_cfg(ctx, start, end, max_nodes=200000):
    """利用 Triton 解码器恢复单个函数的保守函数内 CFG。"""
    nodes = set()
    successors = defaultdict(set)
    worklist = [start]
    decode_failed = False
    unresolved_indirect = False
    unresolved_branch_successor = False

    while worklist:
        pc = worklist.pop()
        if pc in nodes or not (start <= pc < end):
            continue
        if len(nodes) >= max_nodes:
            decode_failed = True
            break

        try:
            opcode = ctx.getConcreteMemoryAreaValue(pc, 16)
            inst = Instruction()
            inst.setOpcode(opcode)
            inst.setAddress(pc)
            ctx.disassembly(inst)
            size = int(inst.getSize())
            disasm = inst.getDisassembly() or ''
        except Exception:
            decode_failed = True
            break
        if size <= 0:
            decode_failed = True
            break

        nodes.add(pc)
        opc = disasm.split()[0].lower() if disasm else 'unknown'
        fallthrough = pc + size
        nexts = set()

        if opc.startswith('ret') or opc in ('hlt', 'ud2'):
            pass
        elif opc == 'jmp' or (opc.startswith('j') and opc != 'jmp'):
            target = None
            try:
                operands = list(inst.getOperands())
                if operands and operands[0].getType() == OPERAND.IMM:
                    target = int(operands[0].getValue())
            except Exception:
                target = None
            if target is None:
                unresolved_indirect = True
            elif start <= target < end:
                nexts.add(target)
            # 条件跳转始终还有 fall-through；直接 jmp 没有。
            if opc != 'jmp':
                if target is not None and not (start <= target < end):
                    unresolved_branch_successor = True
                if start <= fallthrough < end:
                    nexts.add(fallthrough)
                else:
                    unresolved_branch_successor = True
        elif opc == 'call':
            if start <= fallthrough < end:
                nexts.add(fallthrough)
        elif start <= fallthrough < end:
            nexts.add(fallthrough)

        successors[pc].update(nexts)
        worklist.extend(nexts - nodes)

    return {
        'nodes': nodes,
        'successors': successors,
        'complete': (
            bool(nodes)
            and not decode_failed
            and not unresolved_indirect
            and not unresolved_branch_successor
        ),
        'decode_failed': decode_failed,
        'unresolved_indirect': unresolved_indirect,
        'unresolved_branch_successor': unresolved_branch_successor,
    }


def build_static_control_model(ctx, path):
    """恢复函数内 CFG，并为完整函数建立静态后支配控制区域。"""
    branches = {}
    functions = {}
    stats = defaultdict(int)

    for start, end, name in build_function_ranges(path):
        stats['functions_seen'] += 1
        cfg = recover_function_cfg(ctx, start, end)
        complete = cfg['complete']
        regions = {}
        postdom_result = {'unresolved_nodes': set()}
        if complete:
            regions, postdom_result = build_control_regions(
                cfg['nodes'], cfg['successors']
            )
            if postdom_result['unresolved_nodes']:
                complete = False

        if complete:
            stats['functions_modeled'] += 1
            stats['branches_modeled'] += len(regions)
            for branch_pc, info in regions.items():
                branches[branch_pc] = {
                    'function_start': start,
                    'function_name': name,
                    'successor_regions': info['successor_regions'],
                    'merge_pc': info['merge_pc'],
                }
        else:
            stats['functions_fallback'] += 1
            if cfg['unresolved_indirect']:
                stats['functions_with_indirect_jump'] += 1
            if cfg['decode_failed']:
                stats['functions_with_decode_failure'] += 1
            if cfg['unresolved_branch_successor']:
                stats['functions_with_external_conditional_edge'] += 1
            if postdom_result.get('unresolved_nodes'):
                stats['functions_without_exit_path'] += 1

        functions[start] = {
            'name': name,
            'end': end,
            'complete': complete,
            'node_count': len(cfg['nodes']),
            'branch_count': len(regions) if complete else 0,
        }

    return {
        'branches': branches,
        'functions': functions,
        'stats': dict(stats),
    }


# ------------------------------------------------------------------------
# 基础工具
# ------------------------------------------------------------------------
def read_mem_int(ctx, addr, size):
    raw = ctx.getConcreteMemoryAreaValue(addr, size)
    return int.from_bytes(bytes(raw), 'little')


def get_parent_reg_name(ctx, reg):
    try:
        return ctx.getParentRegister(reg).getName()
    except Exception:
        return reg.getName()


def safe_dot(s):
    return str(s).replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')


def hex_pc(x):
    try:
        return f'0x{x:x}'
    except Exception:
        return str(x)


def stable_tuple(items):
    return tuple(sorted(items))


def sorted_hex_list(items):
    return [hex_pc(x) for x in sorted(items)]


def merge_meta_field(dst, key, value):
    if value is None:
        return

    if isinstance(value, set):
        dst.setdefault(key, set()).update(value)
        return

    if isinstance(value, dict):
        cur = dst.setdefault(key, {})
        cur.update(value)
        return

    if isinstance(value, list):
        cur = dst.setdefault(key, [])
        for item in value:
            if item not in cur:
                cur.append(item)
        return

    if key not in dst:
        dst[key] = value
        return

    old = dst[key]
    if old == value:
        return

    if isinstance(old, set):
        old.add(value)
        return

    if isinstance(old, list):
        if value not in old:
            old.append(value)
        return

    if isinstance(old, dict):
        return

    # 标量冲突时改为集合并保留全部值
    dst[key] = {old, value}


def ensure_node(node_meta, node_id, node_type, label, **extra):
    if node_id not in node_meta:
        node_meta[node_id] = {
            'type': node_type,
            'label': label,
        }
    else:
        if label and not node_meta[node_id].get('label'):
            node_meta[node_id]['label'] = label
        if node_type and not node_meta[node_id].get('type'):
            node_meta[node_id]['type'] = node_type

    for k, v in extra.items():
        merge_meta_field(node_meta[node_id], k, v)


def add_node_tags(node_meta, node_id, *tags):
    if node_id not in node_meta:
        return
    valid = {t for t in tags if t}
    if valid:
        node_meta[node_id].setdefault('semantic_tags', set()).update(valid)


def add_inst_tags(inst_semantic_tags, pc, *tags):
    valid = {t for t in tags if t}
    if valid:
        inst_semantic_tags[pc].update(valid)


def reg_name_from_operand(ctx, op):
    try:
        if op is not None and op.getType() == OPERAND.REG:
            return get_parent_reg_name(ctx, op)
    except Exception:
        pass
    return None


def mem_base_name(ctx, mop):
    try:
        reg = mop.getBaseRegister()
        if reg and reg.getName():
            return get_parent_reg_name(ctx, reg)
    except Exception:
        pass
    return None


def mem_index_name(ctx, mop):
    try:
        reg = mop.getIndexRegister()
        if reg and reg.getName():
            return get_parent_reg_name(ctx, reg)
    except Exception:
        pass
    return None


def mem_segment_name(ctx, mop):
    try:
        reg = mop.getSegmentRegister()
        if reg and reg.getName():
            return get_parent_reg_name(ctx, reg)
    except Exception:
        pass
    return None


def is_power_of_two(v):
    try:
        n = int(v)
        return n > 0 and (n & (n - 1)) == 0
    except Exception:
        return False


def normalize_imm_value(value, bit_size=None):
    try:
        iv = int(value)
    except Exception:
        iv = 0

    if bit_size and bit_size > 0:
        mask = (1 << bit_size) - 1
        iv &= mask
        sign_bit = 1 << (bit_size - 1)
        if iv & sign_bit:
            signed = iv - (1 << bit_size)
            return iv, signed
    return iv, iv


def classify_instruction_semantics(ctx, inst, opc, read_regs_info, written_regs_info,
                                   read_mems_info, written_mems_info):
    tags = set()
    operands = list(inst.getOperands())

    op0 = operands[0] if len(operands) >= 1 else None
    op1 = operands[1] if len(operands) >= 2 else None

    op0_reg = reg_name_from_operand(ctx, op0)
    op1_reg = reg_name_from_operand(ctx, op1)

    # 常见序言
    if opc == 'push' and op0_reg == 'rbp':
        tags.add('prologue')
    if opc in MOVE_LIKE_OPCODES and op0_reg == 'rbp' and op1_reg == 'rsp':
        tags.add('prologue')
    if opc == 'sub' and op0_reg == 'rsp' and op1 is not None and op1.getType() == OPERAND.IMM:
        tags.add('prologue')

    # 常见尾声
    if opc in ('leave',):
        tags.add('epilogue')
    if opc == 'pop' and op0_reg == 'rbp':
        tags.add('epilogue')
    if opc == 'add' and op0_reg == 'rsp' and op1 is not None and op1.getType() == OPERAND.IMM:
        tags.add('epilogue')

    # 栈对齐
    if opc == 'and' and op0_reg in ('rsp', 'esp') and op1 is not None and op1.getType() == OPERAND.IMM:
        tags.add('stack_alignment')

    # 参数搬运
    if opc in MOVE_LIKE_OPCODES:
        if op0_reg in ARG_REGS and op1_reg in ARG_REGS:
            tags.add('argument_shuffle')

        if op0 is not None and op1 is not None:
            try:
                if op0.getType() == OPERAND.MEM and op1.getType() == OPERAND.REG:
                    if mem_base_name(ctx, op0) in ('rsp', 'rbp') and get_parent_reg_name(ctx, op1) in ARG_REGS:
                        tags.add('argument_shuffle')
                if op0.getType() == OPERAND.REG and op1.getType() == OPERAND.MEM:
                    if get_parent_reg_name(ctx, op0) in ARG_REGS and mem_base_name(ctx, op1) in ('rsp', 'rbp'):
                        tags.add('argument_shuffle')
            except Exception:
                pass

    # callee-save spill/restore
    if opc == 'push' and op0_reg in CALLEE_SAVED_REGS:
        tags.add('callee_save_spill')
    if opc == 'pop' and op0_reg in CALLEE_SAVED_REGS:
        tags.add('callee_save_restore')

    if opc in MOVE_LIKE_OPCODES and op0 is not None and op1 is not None:
        try:
            if op0.getType() == OPERAND.MEM and op1.getType() == OPERAND.REG:
                if mem_base_name(ctx, op0) in ('rsp', 'rbp') and get_parent_reg_name(ctx, op1) in CALLEE_SAVED_REGS:
                    tags.add('callee_save_spill')
            if op0.getType() == OPERAND.REG and op1.getType() == OPERAND.MEM:
                if get_parent_reg_name(ctx, op0) in CALLEE_SAVED_REGS and mem_base_name(ctx, op1) in ('rsp', 'rbp'):
                    tags.add('callee_save_restore')
        except Exception:
            pass

    return tags


def is_pure_register_move(ctx, inst, opc, read_regs_info, written_regs_info, read_mems_info,
                          written_mems_info, has_immediates):
    if opc not in MOVE_LIKE_OPCODES:
        return False
    if has_immediates:
        return False
    if read_mems_info or written_mems_info:
        return False
    if len(read_regs_info) != 1 or len(written_regs_info) != 1:
        return False
    src_reg = get_parent_reg_name(ctx, read_regs_info[0][0])
    dst_reg = get_parent_reg_name(ctx, written_regs_info[0][0])
    if src_reg == dst_reg:
        return False
    return True


def classify_immediate_semantics(ctx, inst, pc, opc, operand_index, imm_obj, value, bit_size,
                                 source_kind, in_plt_site=False, pc_hit_count_for_site=1):
    """
    为 immediate occurrence 打语义标签。
    这些标签不改变依赖语义，只为后续筛选器提供结构化先验。
    """
    tags = set()
    semantic_family = set()
    structural_family = set()

    normalized_unsigned, normalized_signed = normalize_imm_value(value, bit_size)

    operands = list(inst.getOperands())
    op0 = operands[0] if len(operands) >= 1 else None
    op1 = operands[1] if len(operands) >= 2 else None
    op0_reg = reg_name_from_operand(ctx, op0)
    op1_reg = reg_name_from_operand(ctx, op1)

    if source_kind == 'operand_imm':
        if opc in COMPARE_LIKE_OPCODES:
            tags.add('comparison_constant')
            semantic_family.add('program_semantic_constant')
            if pc_hit_count_for_site > 1:
                tags.add('loop_bound_constant')
                semantic_family.add('program_semantic_constant')

        if written_mems_like(inst):
            tags.add('store_constant')
            semantic_family.add('program_semantic_constant')

        if opc == 'and' and op0_reg in ('rsp', 'esp'):
            tags.add('stack_alignment_constant')
            structural_family.add('structural_abi_constant')

        if opc in ('add', 'sub') and op0_reg in ('rsp', 'esp'):
            tags.add('stack_alignment_constant')
            structural_family.add('structural_abi_constant')

        if opc == 'call':
            tags.add('call_target_constant')

    elif source_kind == 'mem_disp':
        structural_family.add('structural_abi_constant')

        try:
            mop = operands[operand_index]
        except Exception:
            mop = None

        base_name = mem_base_name(ctx, mop) if mop is not None else None
        if base_name in ('rip', 'eip'):
            tags.add('rip_relative_displacement')
        if base_name in ('rbp', 'rsp', 'ebp', 'esp'):
            tags.add('frame_offset_constant')

        if in_plt_site:
            tags.add('plt_got_offset')

    elif source_kind == 'mem_scale':
        tags.add('address_scale_constant')
        structural_family.add('structural_abi_constant')

    # 常见 stack alignment 常量
    if normalized_signed in (-16, -32, -64) or normalized_unsigned in (
        0xfffffffffffffff0,
        0xffffffffffffffe0,
        0xffffffffffffffc0,
        0xfffffff0,
        0xffffffe0,
        0xffffffc0,
    ):
        if opc == 'and' and (op0_reg in ('rsp', 'esp') or op1_reg in ('rsp', 'esp')):
            tags.add('stack_alignment_constant')
            structural_family.add('structural_abi_constant')

    # 常见小整数比较/界限
    if source_kind == 'operand_imm' and opc in COMPARE_LIKE_OPCODES and normalized_signed in (-1, 0, 1):
        tags.add('comparison_constant')
        semantic_family.add('program_semantic_constant')

    if semantic_family:
        tags.update(semantic_family)
    if structural_family:
        tags.update(structural_family)

    return tags


def written_mems_like(inst):
    try:
        return bool(list(inst.getStoreAccess()))
    except Exception:
        return False


def debug_print_progress(inst_count, pc, disasm, call_depth, call_stack,
                         active_control_context, pc_hit_count, start_ts):
    elapsed = time.time() - start_ts
    cur_hit = pc_hit_count.get(pc, 0)

    print(
        f'[dbg] inst={inst_count} '
        f'pc={hex_pc(pc)} '
        f'hit={cur_hit} '
        f'call_depth={call_depth} '
        f'call_stack={len(call_stack)} '
        f'active_ctrl={len(active_control_context)} '
        f'elapsed={elapsed:.2f}s '
        f'disasm={disasm}'
    )

    if active_control_context:
        top = active_control_context[-1]
        try:
            cond_preview = sorted(list(top.get('cond_objs', set())))[:4]
        except Exception:
            cond_preview = ['<unavailable>']
        print(
            f'[dbg] top_ctrl='
            f'branch_pc={hex_pc(top.get("branch_pc"))} '
            f'alt_pc={hex_pc(top.get("alt_pc")) if top.get("alt_pc") is not None else None} '
            f'depth={top.get("call_depth")} '
            f'cond_objs={cond_preview}'
        )


def debug_print_hotspots(pc_hit_count, inst_info, topn=8):
    items = sorted(pc_hit_count.items(), key=lambda kv: kv[1], reverse=True)[:topn]
    print('[dbg] hotspot pcs:')
    for pc, cnt in items:
        disasm = inst_info.get(pc, {}).get('disasm', '<unknown>')
        print(f'       {hex_pc(pc):>12}  hit={cnt:<10}  {disasm}')


def debug_print_loop_patterns(loop_pattern_stats, topn=8):
    items = sorted(loop_pattern_stats.values(), key=lambda x: x['count'], reverse=True)[:topn]
    print('[dbg] loop / repeated dynamic fact patterns:')
    for item in items:
        print(
            f'       pc={hex_pc(item["pc"]):>12} '
            f'depth={item["call_depth"]:<4} '
            f'count={item["count"]:<8} '
            f'suppressed={item["suppressed_records"]:<8} '
            f'disasm={item["disasm"]}'
        )


# ------------------------------------------------------------------------
# Hooks
# ------------------------------------------------------------------------
def hook_printf(ctx):
    ctx.setConcreteRegisterValue(ctx.registers.rax, 0)


def hook_strlen(ctx):
    ctx.setConcreteRegisterValue(ctx.registers.rax, 10)


def hook_rdtscp(ctx, inst_count, inst):
    ctx.setConcreteRegisterValue(ctx.registers.rax, inst_count & 0xffffffff)
    ctx.setConcreteRegisterValue(ctx.registers.rdx, 0)
    ctx.setConcreteRegisterValue(ctx.registers.rcx, 0)
    rip = ctx.getConcreteRegisterValue(ctx.registers.rip)
    ctx.setConcreteRegisterValue(ctx.registers.rip, rip + inst.getSize())


def hook_clflush(ctx, inst):
    rip = ctx.getConcreteRegisterValue(ctx.registers.rip)
    ctx.setConcreteRegisterValue(ctx.registers.rip, rip + inst.getSize())


# ------------------------------------------------------------------------
# 对象命名与归一化（方向3）
# ------------------------------------------------------------------------
def find_global_object(addr, size, global_objects):
    """根据地址区间查找落入的全局对象。"""
    for obj in global_objects:
        base = obj['addr']
        sz = obj['size']
        if sz > 0:
            if base <= addr and (addr + max(size, 1)) <= (base + sz):
                return obj, addr - base
        else:
            if addr == base:
                return obj, 0
    return None, None


class ObjectCanonicalizer:
    """
    方向3的核心：统一对象 ID 生成逻辑。
    设计目标：
      - 不改变方向1/2的分析接口；
      - 所有对象都经过同一个 canonical 入口；
      - last_def_obj / inst_use/def/addr/immediates 使用统一对象键；
      - 尽量兼容当前的输出约定（特别是全局 seed 仍然用 var:<name>）。

    本修订版额外优化：
      - immediate 不再按“值(+位宽)”做全局 intern；
      - 改为 occurrence-based / semantic-site-based，避免不同语义位置的 0/1/offset 被错误合并。
    """

    STACK_FRAME_WINDOW = 0x8000

    def __init__(self, ctx, global_objects, stack_addr, stack_size,
                 taint_symbol_name, taint_source_addr=None, taint_source_size=None):
        self.ctx = ctx
        self.global_objects = global_objects
        self.stack_addr = stack_addr
        self.stack_size = stack_size
        self.taint_symbol_name = taint_symbol_name
        self.taint_source_addr = taint_source_addr
        self.taint_source_size = taint_source_size

    @staticmethod
    def _fmt_hex(v):
        if v < 0:
            return f'-0x{-v:x}'
        return f'0x{v:x}'

    @staticmethod
    def _fmt_off(v):
        if v < 0:
            return f'-0x{-v:x}'
        return f'+0x{v:x}'

    def canon_named_seed(self, name):
        return f'var:{name}', 'var', name, {
            'semantic_tags': {'taint_seed'},
        }

    def canon_reg(self, reg):
        pname = get_parent_reg_name(self.ctx, reg)
        return f'reg:{pname}', 'reg', pname, {}

    def _extract_imm_value_width(self, imm, bit_size=None):
        value = None
        if hasattr(imm, 'getValue'):
            try:
                value = int(imm.getValue())
            except Exception:
                value = None
        if value is None:
            try:
                value = int(imm)
            except Exception:
                value = 0

        resolved_bit_size = bit_size
        if resolved_bit_size is None:
            for attr in ('getBitSize', 'getBitvectorSize', 'getSize'):
                if hasattr(imm, attr):
                    try:
                        maybe = int(getattr(imm, attr)())
                        if attr == 'getSize' and maybe <= 32:
                            maybe *= 8
                        if maybe > 0:
                            resolved_bit_size = maybe
                            break
                    except Exception:
                        pass
        return value, resolved_bit_size

    def canon_imm_occurrence(self, imm, pc, operand_index=None, source_kind='operand_imm',
                             bit_size=None, semantic_tags=None):
        value, resolved_bit_size = self._extract_imm_value_width(imm, bit_size=bit_size)
        vlabel = self._fmt_hex(value)
        idx_label = operand_index if operand_index is not None else 'na'
        width_label = f'i{resolved_bit_size}' if resolved_bit_size and resolved_bit_size > 0 else 'i?'

        oid = f'imm_occurrence:{hex_pc(pc)}:{source_kind}:{idx_label}:{vlabel}:{width_label}'
        short_src = source_kind
        label = f'imm@{hex_pc(pc)}:{short_src}:{idx_label}:{vlabel}/{width_label}'

        if semantic_tags:
            tag_preview = '|'.join(sorted(semantic_tags))
            label = f'{label} [{tag_preview}]'

        meta = {
            'occurrence_pc': pc,
            'occurrence_pc_hex': hex_pc(pc),
            'operand_index': operand_index,
            'source_kind': source_kind,
            'value': value,
            'value_hex': vlabel,
            'bit_size': resolved_bit_size,
            'semantic_tags': set(semantic_tags or []),
            'occurrence_based': True,
        }
        return oid, 'imm', label, meta

    def _in_stack(self, addr):
        return self.stack_addr <= addr < (self.stack_addr + self.stack_size)

    def _get_reg_value(self, reg_name):
        try:
            reg = getattr(self.ctx.registers, reg_name)
            return int(self.ctx.getConcreteRegisterValue(reg))
        except Exception:
            return None

    def _canon_stack_object(self, addr):
        rbp = self._get_reg_value('rbp')
        rsp = self._get_reg_value('rsp')

        if rbp is not None and self._in_stack(rbp):
            off = addr - rbp
            if -self.STACK_FRAME_WINDOW <= off <= self.STACK_FRAME_WINDOW:
                oid = f'stack:[rbp{self._fmt_off(off)}]'
                label = f'stack[rbp{self._fmt_off(off)}]'
                return oid, 'stack', label, {
                    'stack_base': 'rbp',
                    'stack_offset': off,
                }

        if rsp is not None and self._in_stack(rsp):
            off = addr - rsp
            if -self.STACK_FRAME_WINDOW <= off <= self.STACK_FRAME_WINDOW:
                oid = f'stack:[rsp{self._fmt_off(off)}]'
                label = f'stack[rsp{self._fmt_off(off)}]'
                return oid, 'stack', label, {
                    'stack_base': 'rsp',
                    'stack_offset': off,
                }

        oid = f'stack_abs:0x{addr:x}'
        label = f'stack[0x{addr:x}]'
        return oid, 'stack', label, {}

    def canon_memory_access(self, addr, size, mem=None):
        """
        内存访问 -> 规范对象节点：
          1) 污点源对象 -> var:<TAINT_SYMBOL_NAME>
          2) 全局对象     -> var:<name>
          3) 栈对象       -> stack:[rbp/rsp+off] / stack_abs:0x...
          4) 兜底内存     -> mem:0x...
        """
        if self.taint_source_addr is not None and self.taint_source_size is not None:
            if self.taint_source_addr <= addr < (self.taint_source_addr + self.taint_source_size):
                off = addr - self.taint_source_addr
                oid = f'var:{self.taint_symbol_name}'
                label = self.taint_symbol_name if off == 0 else f'{self.taint_symbol_name}+0x{off:x}'
                return oid, 'var', label, {
                    'semantic_tags': {'taint_seed'},
                }

        obj, off = find_global_object(addr, size, self.global_objects)
        if obj is not None:
            oid = f"var:{obj['name']}"
            label = obj['name'] if off == 0 else f"{obj['name']}+0x{off:x}"
            return oid, 'var', label, {
                'global_addr': obj['addr'],
                'global_size': obj['size'],
            }

        if self._in_stack(addr):
            return self._canon_stack_object(addr)

        oid = f'mem:0x{addr:x}'
        label = f'mem[0x{addr:x}]'
        return oid, 'mem', label, {
            'address': addr,
            'access_size': size,
        }


# ------------------------------------------------------------------------
# 图与依赖辅助
# ------------------------------------------------------------------------
def _add_typed_edge_meta(edge_meta, src, dst, kind, pc=None, count=1):
    info = edge_meta.setdefault((src, dst), {'kinds': set(), 'pcs': set(), 'count': 0, 'kind_counts': {}})
    info['kinds'].add(kind)
    info['count'] += count
    info['kind_counts'][kind] = info['kind_counts'].get(kind, 0) + count
    if pc is not None:
        info['pcs'].add(pc)


def _is_pc(value):
    """PC 节点必须是整数；显式排除 bool（bool 是 int 的子类）。"""
    return isinstance(value, int) and not isinstance(value, bool)


def add_inst_edge_meta(inst_edge_meta, src_pc, dst_pc, kind, pc=None, count=1):
    """只向指令依赖图写入 PC -> PC 边。"""
    if not _is_pc(src_pc) or not _is_pc(dst_pc):
        raise TypeError(
            'instruction edge endpoints must both be integer PCs: '
            f'src={src_pc!r} ({type(src_pc).__name__}), '
            f'dst={dst_pc!r} ({type(dst_pc).__name__})'
        )
    if pc is not None and not _is_pc(pc):
        raise TypeError(f'instruction edge evidence pc must be an integer PC: {pc!r}')
    _add_typed_edge_meta(inst_edge_meta, src_pc, dst_pc, kind, pc=pc, count=count)


def add_object_edge_meta(object_edge_meta, src_oid, dst_oid, kind, pc=None, count=1):
    """只向对象因果依赖图写入 object-id -> object-id 边。"""
    if not isinstance(src_oid, str) or not isinstance(dst_oid, str):
        raise TypeError(
            'object edge endpoints must both be string object IDs: '
            f'src={src_oid!r} ({type(src_oid).__name__}), '
            f'dst={dst_oid!r} ({type(dst_oid).__name__})'
        )
    if pc is not None and not _is_pc(pc):
        raise TypeError(f'object edge evidence pc must be an integer PC: {pc!r}')
    _add_typed_edge_meta(object_edge_meta, src_oid, dst_oid, kind, pc=pc, count=count)


def add_object_relation_meta(object_relation_meta, src_oid, dst_oid, relation, pc=None, count=1):
    """
    记录对象身份/结构关系（alias、member-of、canonical-equivalent 等）。

    这些关系不是 data/address/control 因果边，禁止写入 inst_edge_meta 或
    object_edge_meta，避免对象等价关系改变依赖可达性。
    """
    if not isinstance(src_oid, str) or not isinstance(dst_oid, str):
        raise TypeError(
            'object relation endpoints must both be string object IDs: '
            f'src={src_oid!r} ({type(src_oid).__name__}), '
            f'dst={dst_oid!r} ({type(dst_oid).__name__})'
        )
    if pc is not None and not _is_pc(pc):
        raise TypeError(f'object relation evidence pc must be an integer PC: {pc!r}')
    _add_typed_edge_meta(object_relation_meta, src_oid, dst_oid, relation, pc=pc, count=count)


def validate_edge_table_types(inst_edge_meta, object_edge_meta, object_relation_meta):
    """在切片/导出前 fail closed，禁止通过过滤静默丢弃类型污染边。"""
    for src, dst in inst_edge_meta:
        if not _is_pc(src) or not _is_pc(dst):
            raise TypeError(f'invalid instruction edge key: {(src, dst)!r}')
    for table_name, table in (
        ('object dependency', object_edge_meta),
        ('object relation', object_relation_meta),
    ):
        for src, dst in table:
            if not isinstance(src, str) or not isinstance(dst, str):
                raise TypeError(f'invalid {table_name} edge key: {(src, dst)!r}')


def build_adj_from_edge_meta(edge_meta):
    succ = defaultdict(set)
    pred = defaultdict(set)
    for (src, dst), _ in edge_meta.items():
        succ[src].add(dst)
        pred[dst].add(src)
    return succ, pred


def traverse_graph(start_nodes, succ=None, pred=None, reverse=False, allowed_kinds=None, edge_meta=None):
    """图遍历，返回可达节点集合。"""
    visited = set()
    q = deque(start_nodes)
    while q:
        cur = q.popleft()
        if cur in visited:
            continue
        visited.add(cur)
        nexts = pred.get(cur, set()) if reverse else succ.get(cur, set())
        for nxt in nexts:
            if edge_meta is not None and allowed_kinds is not None:
                meta = edge_meta.get((nxt, cur) if reverse else (cur, nxt), None)
                if meta is None:
                    continue
                if not (meta['kinds'] & set(allowed_kinds)):
                    continue
            if nxt not in visited:
                q.append(nxt)
    return visited


def compute_leaf_nodes(nodes, pred):
    leaves = set()
    for n in nodes:
        if len(pred.get(n, set()) & nodes) == 0:
            leaves.add(n)
    return leaves


def compute_sink_nodes(nodes, succ):
    sinks = set()
    for n in nodes:
        if len(succ.get(n, set()) & nodes) == 0:
            sinks.add(n)
    return sinks


def is_memory_like_object(node_id):
    return (
        node_id.startswith('var:') or
        node_id.startswith('stack:') or
        node_id.startswith('stack_abs:') or
        node_id.startswith('mem:')
    )


def collect_control_source_objects_for_pc(pc, inst_controlled_by, inst_ctrl_objects):
    objs = set()
    for bpc in inst_controlled_by.get(pc, set()):
        objs.update(inst_ctrl_objects.get(bpc, set()))
    return objs


def make_active_control_signature(active_control_context, pc):
    if not LOOP_SUMMARIZATION_INCLUDE_CONTROL:
        return (), ()

    branch_pcs = set()
    cond_objs = set()
    for cctx in active_control_context:
        bpc = cctx.get('branch_pc')
        if bpc is not None and bpc != pc:
            branch_pcs.add(bpc)
        cond_objs.update(cctx.get('cond_objs', set()))

    return stable_tuple(branch_pcs), stable_tuple(cond_objs)


def make_loop_fact_signature(
    pc,
    call_depth,
    use_objs,
    def_objs,
    addr_objs,
    imm_objs,
    mem_objs,
    raw_inst_data_edges,
    canonical_inst_data_edges,
    inst_addr_edges,
    object_relations,
    active_ctrl_branch_sig,
    active_ctrl_obj_sig,
    use_tainted_regs,
    use_tainted_mems,
    def_tainted_regs,
    def_tainted_mems,
    regs_t,
    mems_t,
    touches_seed=False,  # ★ 修订点9：新增参数
):
    """
    生成循环事实签名。
    
    修订点9：加入 touches_seed 标记，使得涉及 seed 的指令
    与不涉及 seed 的相同模式指令产生不同签名，从而独立计数。
    这确保了 seed-touching 的指令不会被错误地与非 seed 指令聚合后被熔断。
    """
    return (
        pc,
        call_depth,
        stable_tuple(use_objs),
        stable_tuple(def_objs),
        stable_tuple(addr_objs),
        stable_tuple(imm_objs),
        stable_tuple(mem_objs),
        tuple(sorted(raw_inst_data_edges)),
        tuple(sorted(canonical_inst_data_edges)),
        tuple(sorted(inst_addr_edges)),
        tuple(sorted(object_relations)),
        active_ctrl_branch_sig,
        active_ctrl_obj_sig,
        stable_tuple(use_tainted_regs),
        stable_tuple(use_tainted_mems),
        stable_tuple(def_tainted_regs),
        stable_tuple(def_tainted_mems),
        stable_tuple(regs_t),
        stable_tuple(mems_t),
        touches_seed,  # ★ 修订点9：seed 标记纳入签名
    )


def update_loop_pattern_stats(loop_pattern_stats, signature, pc, call_depth, disasm,
                              use_objs, def_objs, addr_objs, imm_objs,
                              active_ctrl_branch_sig, active_ctrl_obj_sig,
                              inst_uses_taint_flag, allow_new_pattern=True):
    if signature in loop_pattern_stats:
        entry = loop_pattern_stats[signature]
        entry['count'] += 1
        entry['suppressed_records'] = max(0, entry['count'] - LOOP_SUMMARIZATION_SUPPRESS_AFTER)
        return entry, False

    if not allow_new_pattern:
        return None, False

    entry = {
        'pc': pc,
        'call_depth': call_depth,
        'disasm': disasm,
        'count': 1,
        'suppressed_records': 0,
        'use_objects': stable_tuple(use_objs),
        'def_objects': stable_tuple(def_objs),
        'addr_objects': stable_tuple(addr_objs),
        'immediates': stable_tuple(imm_objs),
        'active_control_branch_pcs': active_ctrl_branch_sig,
        'active_control_objects': active_ctrl_obj_sig,
        'uses_taint': bool(inst_uses_taint_flag),
    }
    loop_pattern_stats[signature] = entry
    return entry, True


def build_seed_object_slice(
    obj_seed_nodes,
    executed_pcs,
    node_meta,
    inst_use_objects,
    inst_def_objects,
    inst_addr_objects,
    inst_mem_objects,
    inst_controlled_by,
    inst_ctrl_objects,
    control_expansion_mode,
):
    """
    方向 2：
    不从 whole-program object_edge_meta 上做遍历，
    而是从每条指令记录下来的最小事实出发，只围绕 seed 构造对象 slice。
    """

    all_obj_use_pcs = defaultdict(set)
    all_obj_def_pcs = defaultdict(set)
    all_obj_addr_use_pcs = defaultdict(set)
    all_obj_ctrl_use_pcs = defaultdict(set)
    mem_obj_touch_pcs = defaultdict(set)
    control_src_objects_by_pc = {}

    for pc in executed_pcs:
        use_objs = inst_use_objects.get(pc, set())
        def_objs = inst_def_objects.get(pc, set())
        addr_objs = inst_addr_objects.get(pc, set())
        mem_objs = inst_mem_objects.get(pc, set())

        for oid in use_objs:
            all_obj_use_pcs[oid].add(pc)

        for oid in def_objs:
            all_obj_def_pcs[oid].add(pc)

        for oid in addr_objs:
            all_obj_addr_use_pcs[oid].add(pc)

        for oid in mem_objs:
            mem_obj_touch_pcs[oid].add(pc)

        ctrl_srcs = collect_control_source_objects_for_pc(pc, inst_controlled_by, inst_ctrl_objects)
        control_src_objects_by_pc[pc] = ctrl_srcs
        for oid in ctrl_srcs:
            all_obj_ctrl_use_pcs[oid].add(pc)

    object_edge_meta = {}

    # -------------------- forward slice --------------------
    forward_obj_reachable = set(obj_seed_nodes)
    q = deque(obj_seed_nodes)

    while q:
        oid = q.popleft()

        for pc in all_obj_use_pcs.get(oid, set()):
            for dst in inst_def_objects.get(pc, set()):
                if oid == dst:
                    continue
                add_object_edge_meta(object_edge_meta, oid, dst, 'data', pc)
                if dst not in forward_obj_reachable:
                    forward_obj_reachable.add(dst)
                    q.append(dst)

        for pc in all_obj_addr_use_pcs.get(oid, set()):
            for dst in inst_mem_objects.get(pc, set()):
                if oid == dst:
                    continue
                add_object_edge_meta(object_edge_meta, oid, dst, 'addr', pc)
                if dst not in forward_obj_reachable:
                    forward_obj_reachable.add(dst)
                    q.append(dst)

        if control_expansion_mode in ('def-only', 'all'):
            for pc in all_obj_ctrl_use_pcs.get(oid, set()):
                for dst in inst_def_objects.get(pc, set()):
                    if oid == dst:
                        continue
                    add_object_edge_meta(object_edge_meta, oid, dst, 'control', pc)
                    if dst not in forward_obj_reachable:
                        forward_obj_reachable.add(dst)
                        q.append(dst)

    # -------------------- backward slice --------------------
    backward_obj_reachable = set(obj_seed_nodes)
    q = deque(obj_seed_nodes)

    while q:
        oid = q.popleft()

        for pc in all_obj_def_pcs.get(oid, set()):
            for src in inst_use_objects.get(pc, set()):
                if src == oid:
                    continue
                add_object_edge_meta(object_edge_meta, src, oid, 'data', pc)
                if src not in backward_obj_reachable:
                    backward_obj_reachable.add(src)
                    q.append(src)

            if control_expansion_mode in ('def-only', 'all'):
                for src in control_src_objects_by_pc.get(pc, set()):
                    if src == oid:
                        continue
                    add_object_edge_meta(object_edge_meta, src, oid, 'control', pc)
                    if src not in backward_obj_reachable:
                        backward_obj_reachable.add(src)
                        q.append(src)

        if is_memory_like_object(oid):
            for pc in mem_obj_touch_pcs.get(oid, set()):
                for src in inst_addr_objects.get(pc, set()):
                    if src == oid:
                        continue
                    add_object_edge_meta(object_edge_meta, src, oid, 'addr', pc)
                    if src not in backward_obj_reachable:
                        backward_obj_reachable.add(src)
                        q.append(src)

    slice_nodes = set(obj_seed_nodes) | forward_obj_reachable | backward_obj_reachable
    for (src, dst) in object_edge_meta.keys():
        slice_nodes.add(src)
        slice_nodes.add(dst)

    sliced_node_meta = {
        oid: node_meta[oid]
        for oid in slice_nodes
        if oid in node_meta
    }

    # 只为 slice 节点恢复对象事实，避免 whole-program 对象事实常驻
    obj_def_pcs = defaultdict(set)
    obj_use_pcs = defaultdict(set)
    obj_addr_use_pcs = defaultdict(set)
    obj_ctrl_use_pcs = defaultdict(set)

    for pc in executed_pcs:
        for oid in inst_use_objects.get(pc, set()):
            if oid in slice_nodes:
                obj_use_pcs[oid].add(pc)

        for oid in inst_def_objects.get(pc, set()):
            if oid in slice_nodes:
                obj_def_pcs[oid].add(pc)

        for oid in inst_addr_objects.get(pc, set()):
            if oid in slice_nodes:
                obj_addr_use_pcs[oid].add(pc)

        for oid in control_src_objects_by_pc.get(pc, set()):
            if oid in slice_nodes:
                obj_ctrl_use_pcs[oid].add(pc)

    return {
        'object_edge_meta': object_edge_meta,
        'sliced_node_meta': sliced_node_meta,
        'forward_obj_reachable': forward_obj_reachable,
        'backward_obj_reachable': backward_obj_reachable,
        'obj_def_pcs': obj_def_pcs,
        'obj_use_pcs': obj_use_pcs,
        'obj_addr_use_pcs': obj_addr_use_pcs,
        'obj_ctrl_use_pcs': obj_ctrl_use_pcs,
    }


# ------------------------------------------------------------------------
# 在线控制依赖辅助（方向1）
# ------------------------------------------------------------------------
def make_hybrid_control_context(
    static_control_model,
    branch_pc,
    cond_objs,
    call_depth,
    taken_next,
    fallthrough,
    alt_pc,
):
    """优先创建静态后支配上下文；不可证明时显式退回动态近似。"""
    branch_model = static_control_model.get('branches', {}).get(branch_pc)
    controlled_pcs = None
    merge_pc = None
    evidence = 'dynamic_alt_fallback'

    if branch_model is not None:
        region = branch_model.get('successor_regions', {}).get(taken_next)
        if region is not None:
            controlled_pcs = frozenset(region)
            merge_pc = branch_model.get('merge_pc')
            evidence = 'static_postdom_dynamic_edge'

    key = (branch_pc, call_depth, taken_next, evidence)
    return {
        'key': key,
        'branch_pc': branch_pc,
        'cond_objs': set(cond_objs),
        'call_depth': call_depth,
        'taken_next': taken_next,
        'fallthrough': fallthrough,
        'alt_pc': alt_pc,
        'controlled_pcs': controlled_pcs,
        'merge_pc': merge_pc,
        'evidence': evidence,
    }


def pop_inactive_control_context(active_control_context, active_control_keys, current_pc, call_depth):
    """
    在线清理已失活的混合控制上下文。

    静态后支配上下文在同一调用深度离开其严格控制区域时失活；进入被
    控制的 callee 时继续有效。回退上下文沿用原来的 alt_pc 动态近似。
    """
    retained = []
    for cctx in active_control_context:
        should_pop = call_depth < cctx['call_depth']
        if not should_pop and call_depth == cctx['call_depth']:
            if cctx.get('evidence') == 'static_postdom_dynamic_edge':
                controlled_pcs = cctx.get('controlled_pcs') or frozenset()
                should_pop = (
                    current_pc != cctx.get('branch_pc')
                    and current_pc not in controlled_pcs
                )
            else:
                alt = cctx.get('alt_pc')
                should_pop = alt is not None and current_pc == alt

        if should_pop:
            key = cctx.get('key')
            if key is not None:
                active_control_keys.discard(key)
        else:
            retained.append(cctx)

    active_control_context[:] = retained


def apply_online_control_to_inst(
    pc,
    def_objs,
    active_control_context,
    call_depth,
    inst_controlled_by,
    inst_ctrl_objects,
    inst_edge_meta,
    obj_ctrl_use_pcs,
    inst_control_evidence=None,
):
    """
    将当前活动控制上下文在线施加到当前指令。

    方向 2 下，这里只记录“最小事实”，不在线构造 whole-program object control graph：
      - 记录 branch_pc -> pc 的指令级 control 边
      - 记录当前指令受哪些 cond_objs 控制（inst_ctrl_objects[pc]）
      - 记录 cond_obj 在哪些 pc 上被控制使用（obj_ctrl_use_pcs）
    后续若需要 object-level control 边（cond_obj -> def_obj），应在 seed-driven slice 阶段重建。
    """
    if CONTROL_EXPANSION_MODE == 'none':
        return

    if not active_control_context:
        return

    seen_branch_pcs = set()
    merged_cond_objs = set()

    for cctx in active_control_context:
        bpc = cctx['branch_pc']

        # 静态上下文只作用于后支配算法确认的 taken-edge 控制区域。
        if (
            cctx.get('evidence') == 'static_postdom_dynamic_edge'
            and call_depth == cctx.get('call_depth')
            and pc not in (cctx.get('controlled_pcs') or frozenset())
        ):
            continue

        if bpc != pc and bpc not in seen_branch_pcs:
            seen_branch_pcs.add(bpc)
            inst_controlled_by[pc].add(bpc)
            add_inst_edge_meta(inst_edge_meta, bpc, pc, 'control', pc)
            if inst_control_evidence is not None:
                inst_control_evidence[(bpc, pc)].add(
                    cctx.get('evidence', 'dynamic_alt_fallback')
                )

        merged_cond_objs.update(cctx.get('cond_objs', set()))

    if not merged_cond_objs:
        return

    inst_ctrl_objects[pc].update(merged_cond_objs)

    if CONTROL_EXPANSION_MODE in ('def-only', 'all'):
        for cobj in merged_cond_objs:
            obj_ctrl_use_pcs[cobj].add(pc)


# ------------------------------------------------------------------------
# 方向5：局部视图 / 路径报告辅助
# ------------------------------------------------------------------------
def filter_edge_meta_by_nodes(edge_meta, allowed_nodes):
    allowed = set(allowed_nodes)
    return {
        (src, dst): meta
        for (src, dst), meta in edge_meta.items()
        if src in allowed and dst in allowed
    }


def filter_plain_edges_by_nodes(edges, allowed_nodes):
    allowed = set(allowed_nodes)
    return {
        (src, dst)
        for (src, dst) in edges
        if src in allowed and dst in allowed
    }


def build_edge_details(edge_meta):
    details = {}
    for (src, dst), meta in edge_meta.items():
        details[(src, dst)] = {
            'kinds': sorted(meta['kinds']),
            'pcs': sorted_hex_list(meta['pcs']),
            'count': meta['count'],
            'kind_counts': dict(sorted(meta['kind_counts'].items())),
        }
    return details


def build_object_relation_details(object_relation_meta):
    """将独立的对象关系表转换为可 JSON 序列化的稳定列表。"""
    details = []
    for (src_oid, dst_oid), meta in sorted(object_relation_meta.items()):
        details.append({
            'source_object': src_oid,
            'target_object': dst_oid,
            'relations': sorted(meta['kinds']),
            'pcs': sorted_hex_list(meta['pcs']),
            'count': meta['count'],
            'relation_counts': dict(sorted(meta['kind_counts'].items())),
        })
    return details


def collect_k_hop_neighborhood(start_nodes, succ, pred, hops=2):
    visited = set(start_nodes)
    frontier = set(start_nodes)

    for _ in range(max(0, hops)):
        if not frontier:
            break
        nxt_frontier = set()
        for cur in frontier:
            nxt_frontier.update(succ.get(cur, set()))
            nxt_frontier.update(pred.get(cur, set()))
        nxt_frontier -= visited
        if not nxt_frontier:
            break
        visited.update(nxt_frontier)
        frontier = nxt_frontier

    return visited


def select_object_view_nodes(view_mode, obj_seed_nodes,
                             backward_obj_reachable, forward_obj_reachable,
                             obj_succ, obj_pred, neighborhood_hops):
    if view_mode == 'backward':
        return set(obj_seed_nodes) | set(backward_obj_reachable)
    if view_mode == 'forward':
        return set(obj_seed_nodes) | set(forward_obj_reachable)
    if view_mode == 'neighborhood':
        return collect_k_hop_neighborhood(
            start_nodes=obj_seed_nodes,
            succ=obj_succ,
            pred=obj_pred,
            hops=neighborhood_hops,
        )
    return set(obj_seed_nodes) | set(backward_obj_reachable) | set(forward_obj_reachable)


def select_inst_view_nodes(view_mode, inst_seed_pcs,
                           backward_inst_reachable, forward_inst_reachable,
                           inst_succ, inst_pred, neighborhood_hops):
    if view_mode == 'backward':
        return set(inst_seed_pcs) | set(backward_inst_reachable)
    if view_mode == 'forward':
        return set(inst_seed_pcs) | set(forward_inst_reachable)
    if view_mode == 'neighborhood':
        return collect_k_hop_neighborhood(
            start_nodes=inst_seed_pcs,
            succ=inst_succ,
            pred=inst_pred,
            hops=neighborhood_hops,
        )
    return set(inst_seed_pcs) | set(backward_inst_reachable) | set(forward_inst_reachable)


def build_path_steps(path, edge_details, node_meta, edge_pcs_limit=8):
    steps = []
    for idx in range(len(path) - 1):
        src = path[idx]
        dst = path[idx + 1]
        info = edge_details.get((src, dst), {})
        pcs = list(info.get('pcs', []))
        shown_pcs = pcs[:edge_pcs_limit]
        steps.append({
            'src': src,
            'src_label': node_meta.get(src, {}).get('label', src),
            'dst': dst,
            'dst_label': node_meta.get(dst, {}).get('label', dst),
            'kinds': list(info.get('kinds', [])),
            'count': int(info.get('count', 0) or 0),
            'kind_counts': dict(info.get('kind_counts', {})),
            'pcs': shown_pcs,
            'pcs_truncated': max(0, len(pcs) - len(shown_pcs)),
        })
    return steps


def format_txt_path(labels, steps):
    if not labels:
        return ''
    if not steps:
        return ' -> '.join(labels)

    parts = [labels[0]]
    for idx, step in enumerate(steps):
        kinds = '|'.join(step.get('kinds', [])) or '?'
        cnt = step.get('count', 0)
        pcs = step.get('pcs', [])
        pcs_suffix = ''
        if pcs:
            preview = ','.join(pcs[:3])
            if step.get('pcs_truncated', 0) > 0 or len(pcs) > 3:
                preview += ',...'
            pcs_suffix = f';pcs={preview}'
        parts.append(f'-[{kinds};count={cnt}{pcs_suffix}]-> {labels[idx + 1]}')
    return ' '.join(parts)


# ------------------------------------------------------------------------
# 路径报告（方向5 + 方向6）
# ------------------------------------------------------------------------
def bfs_paths(succ, start, goal, max_depth=32, max_paths=3, allowed_nodes=None):
    """
    返回若干条代表性简单路径。
    为避免爆炸：
      - 限制最大深度
      - 限制每个目标最多返回 max_paths
      - 路径内不允许重复节点
    """
    if start == goal:
        return [[start]]

    results = []
    q = deque([[start]])
    seen_prefix = set()

    while q and len(results) < max_paths:
        path = q.popleft()
        cur = path[-1]
        if len(path) - 1 >= max_depth:
            continue

        for nxt in sorted(succ.get(cur, set())):
            if allowed_nodes is not None and nxt not in allowed_nodes:
                continue
            if nxt in path:
                continue

            new_path = path + [nxt]
            if nxt == goal:
                results.append(new_path)
                if len(results) >= max_paths:
                    break
                continue

            prefix_key = tuple(new_path)
            if prefix_key in seen_prefix:
                continue
            seen_prefix.add(prefix_key)
            q.append(new_path)

    return results


def choose_top_nodes_by_degree(nodes, pred, succ, limit):
    scored = []
    for n in nodes:
        score = len(pred.get(n, set())) + len(succ.get(n, set()))
        scored.append((score, n))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [n for _score, n in scored[:limit]]


def build_object_path_report(
    obj_seed_nodes,
    backward_obj_reachable,
    forward_obj_reachable,
    object_edge_meta,
    node_meta,
    obj_leaf_nodes,
    forward_obj_sinks,
    max_depth=48,
    per_target=3,
    top_targets=32,
    edge_pcs_limit=8,
):
    succ, pred = build_adj_from_edge_meta(object_edge_meta)
    edge_details = build_edge_details(object_edge_meta)

    seed_list = sorted(obj_seed_nodes)
    backward_targets = choose_top_nodes_by_degree(
        sorted(obj_leaf_nodes), pred, succ, top_targets
    )
    forward_targets = choose_top_nodes_by_degree(
        sorted(forward_obj_sinks), pred, succ, top_targets
    )

    report = {
        'config': {
            'max_depth': max_depth,
            'per_target': per_target,
            'top_targets': top_targets,
            'edge_pcs_limit': edge_pcs_limit,
        },
        'backward_paths': [],
        'forward_paths': [],
    }

    seed_for_path = seed_list[0] if seed_list else None
    if seed_for_path is None:
        return report

    # backward：从叶子走到 seed
    allowed_bwd_nodes = set(backward_obj_reachable) | set(obj_seed_nodes)
    for leaf in backward_targets:
        paths = bfs_paths(
            succ=succ,
            start=leaf,
            goal=seed_for_path,
            max_depth=max_depth,
            max_paths=per_target,
            allowed_nodes=allowed_bwd_nodes,
        )
        report['backward_paths'].append({
            'target': leaf,
            'target_label': node_meta.get(leaf, {}).get('label', leaf),
            'paths': [
                {
                    'nodes': path,
                    'labels': [node_meta.get(n, {}).get('label', n) for n in path],
                    'steps': build_path_steps(path, edge_details, node_meta, edge_pcs_limit=edge_pcs_limit),
                }
                for path in paths
            ],
        })

    # forward：从 seed 走到前向终点
    allowed_fwd_nodes = set(forward_obj_reachable) | set(obj_seed_nodes)
    for sink in forward_targets:
        paths = bfs_paths(
            succ=succ,
            start=seed_for_path,
            goal=sink,
            max_depth=max_depth,
            max_paths=per_target,
            allowed_nodes=allowed_fwd_nodes,
        )
        report['forward_paths'].append({
            'target': sink,
            'target_label': node_meta.get(sink, {}).get('label', sink),
            'paths': [
                {
                    'nodes': path,
                    'labels': [node_meta.get(n, {}).get('label', n) for n in path],
                    'steps': build_path_steps(path, edge_details, node_meta, edge_pcs_limit=edge_pcs_limit),
                }
                for path in paths
            ],
        })

    return report


def export_object_path_report_txt(path, report):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('# Object Path Report\n\n')

        f.write('## Backward representative paths\n')
        if not report.get('backward_paths'):
            f.write('(none)\n')
        for item in report.get('backward_paths', []):
            f.write(f'\n### {item["target"]} ({item["target_label"]})\n')
            if not item.get('paths'):
                f.write('(no path found under current depth budget)\n')
                continue
            for idx, p in enumerate(item['paths'], 1):
                rendered = format_txt_path(p.get('labels', []), p.get('steps', []))
                f.write(f'[{idx}] {rendered}\n')

        f.write('\n## Forward representative paths\n')
        if not report.get('forward_paths'):
            f.write('(none)\n')
        for item in report.get('forward_paths', []):
            f.write(f'\n### {item["target"]} ({item["target_label"]})\n')
            if not item.get('paths'):
                f.write('(no path found under current depth budget)\n')
                continue
            for idx, p in enumerate(item['paths'], 1):
                rendered = format_txt_path(p.get('labels', []), p.get('steps', []))
                f.write(f'[{idx}] {rendered}\n')


# ------------------------------------------------------------------------
# DOT 导出
# ------------------------------------------------------------------------
def export_cfg_dot(path, pcs, cfg_edges, addr2line_map, node_taint, inst_taint_io, inst_uses_taint, inst_info):
    selected_pcs = _safe_int_set(executed_pcs)
    safe_cfg_edges = _safe_int_edge_set(cfg_edges)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('digraph CFG {\n')
        for pc in sorted(selected_pcs):
            label_lines = [f'0x{pc:x}']
            src_info = addr2line_map.get(pc)
            if src_info:
                label_lines.append(f'{src_info[0]}:{src_info[1]}')
            info = inst_info.get(pc)
            if info:
                label_lines.append(info['disasm'])
                if info.get('semantic_tags'):
                    label_lines.append('Tags: ' + ','.join(sorted(info['semantic_tags'])))

            if pc in node_taint:
                tinfo = node_taint[pc]
                if tinfo['regs']:
                    label_lines.append('Tregs: ' + ','.join(sorted(tinfo['regs'])))
                if tinfo['mems']:
                    mems = [f'0x{x:x}' for x in sorted(tinfo['mems'])[:4]]
                    if len(tinfo['mems']) > 4:
                        mems.append('...')
                    label_lines.append('Tmems: ' + ','.join(mems))

            io = inst_taint_io.get(pc, {})
            if io.get('use_regs'):
                label_lines.append('UseTregs: ' + ','.join(sorted(io['use_regs'])))
            if io.get('use_mems'):
                mems = [f'0x{x:x}' for x in sorted(io['use_mems'])[:4]]
                if len(io['use_mems']) > 4:
                    mems.append('...')
                label_lines.append('UseTmems: ' + ','.join(mems))
            if io.get('def_regs'):
                label_lines.append('DefTregs: ' + ','.join(sorted(io['def_regs'])))
            if io.get('def_mems'):
                mems = [f'0x{x:x}' for x in sorted(io['def_mems'])[:4]]
                if len(io['def_mems']) > 4:
                    mems.append('...')
                label_lines.append('DefTmems: ' + ','.join(mems))

            color = 'red' if inst_uses_taint.get(pc, False) else 'black'
            label = safe_dot('\\n'.join(label_lines))
            f.write(f'  "0x{pc:x}" [label="{label}", color="{color}"];\n')

        for (src, dst) in sorted(safe_cfg_edges):
            if src in selected_pcs and dst in selected_pcs:
                f.write(f'  "0x{src:x}" -> "0x{dst:x}";\n')
        f.write('}\n')


def export_cfg_bb_dot(path, executed_pcs, cfg_edges, addr2line_map, inst_info, node_taint, inst_taint_io, inst_uses_taint):
    selected_pcs = _safe_int_set(executed_pcs)
    safe_cfg_edges = _safe_int_edge_set(cfg_edges)
    succs = defaultdict(set)
    preds = defaultdict(set)
    for src, dst in safe_cfg_edges:
        if src in selected_pcs and dst in selected_pcs:
            succs[src].add(dst)
            preds[dst].add(src)

    def is_terminator(pc):
        info = inst_info.get(pc)
        if not info:
            return False
        opc = info['opc']
        return opc.startswith('j') or opc in ('call', 'ret', 'hlt')

    blocks = []
    visited = set()
    for pc in sorted(selected_pcs):
        if pc in visited:
            continue

        start = pc
        while True:
            preds_set = preds.get(start, set())
            if len(preds_set) != 1:
                break
            prev_pc = next(iter(preds_set))
            if len(succs.get(prev_pc, set())) != 1:
                break
            if is_terminator(prev_pc):
                break
            start = prev_pc

        block = []
        cur = start
        while True:
            block.append(cur)
            visited.add(cur)
            if is_terminator(cur):
                break
            succs_set = succs.get(cur, set())
            if len(succs_set) != 1:
                break
            nxt = next(iter(succs_set))
            if len(preds.get(nxt, set())) != 1:
                break
            cur = nxt

        blocks.append(block)

    pc2block = {}
    for i, pcs in enumerate(blocks):
        bid = f'BB{i}'
        for pc in pcs:
            pc2block[pc] = bid

    block_edges = set()
    for src, dst in safe_cfg_edges:
        bsrc = pc2block.get(src)
        bdst = pc2block.get(dst)
        if bsrc and bdst and bsrc != bdst:
            block_edges.add((bsrc, bdst))

    with open(path, 'w', encoding='utf-8') as f:
        f.write('digraph CFG_BB {\n')
        for i, pcs in enumerate(blocks):
            bid = f'BB{i}'
            lines = []
            for pc in pcs:
                parts = [f'0x{pc:x}']
                src_info = addr2line_map.get(pc)
                if src_info:
                    parts.append(f'{src_info[0]}:{src_info[1]}')
                info = inst_info.get(pc)
                if info:
                    parts.append(info['disasm'])
                    if info.get('semantic_tags'):
                        parts.append('Tags:' + ','.join(sorted(info['semantic_tags'])))
                if pc in node_taint:
                    tinfo = node_taint[pc]
                    if tinfo['regs']:
                        parts.append('Tregs:' + ','.join(sorted(tinfo['regs'])))
                    if tinfo['mems']:
                        mems = [f'0x{x:x}' for x in sorted(tinfo['mems'])[:3]]
                        if len(tinfo['mems']) > 3:
                            mems.append('...')
                        parts.append('Tmems:' + ','.join(mems))
                io = inst_taint_io.get(pc, {})
                if io.get('use_regs'):
                    parts.append('UseTregs:' + ','.join(sorted(io['use_regs'])))
                if io.get('use_mems'):
                    mems = [f'0x{x:x}' for x in sorted(io['use_mems'])[:3]]
                    if len(io['use_mems']) > 3:
                        mems.append('...')
                    parts.append('UseTmems:' + ','.join(mems))
                if io.get('def_regs'):
                    parts.append('DefTregs:' + ','.join(sorted(io['def_regs'])))
                if io.get('def_mems'):
                    mems = [f'0x{x:x}' for x in sorted(io['def_mems'])[:3]]
                    if len(io['def_mems']) > 3:
                        mems.append('...')
                    parts.append('DefTmems:' + ','.join(mems))
                lines.append(' '.join(parts))

            label = safe_dot('\\l'.join(lines) + '\\l')
            color = 'red' if any(inst_uses_taint.get(pc, False) for pc in pcs) else 'black'
            f.write(f'  "{bid}" [shape=box, label="{label}", color="{color}"];\n')

        for bsrc, bdst in sorted(block_edges):
            f.write(f'  "{bsrc}" -> "{bdst}";\n')
        f.write('}\n')


def export_inst_dep_dot(path, executed_pcs, inst_edge_meta, addr2line_map, inst_info, node_taint, inst_uses_taint,
                        backward_inst_reachable, forward_inst_reachable, inst_seed_pcs):
    
    selected_pcs = {pc for pc in executed_pcs if isinstance(pc, int)}
    backward_inst_reachable = {pc for pc in backward_inst_reachable if isinstance(pc, int)}
    forward_inst_reachable = {pc for pc in forward_inst_reachable if isinstance(pc, int)}
    inst_seed_pcs = {pc for pc in inst_seed_pcs if isinstance(pc, int)} if not isinstance(inst_seed_pcs, set) else {pc for pc in inst_seed_pcs if isinstance(pc, int)}

    # ★ 修复：过滤 inst_edge_meta，只保留键为 (int, int) 的条目
    filtered_edge_meta = {
        (src, dst): meta
        for (src, dst), meta in inst_edge_meta.items()
        if isinstance(src, int) and isinstance(dst, int)
    }
    with open(path, 'w', encoding='utf-8') as f:
        f.write('digraph INST_DEP {\n')
        for pc in sorted(selected_pcs):
            label_lines = [f'0x{pc:x}']
            src_info = addr2line_map.get(pc)
            if src_info:
                label_lines.append(f'{src_info[0]}:{src_info[1]}')
            info = inst_info.get(pc)
            if info:
                label_lines.append(info['disasm'])
                if info.get('semantic_tags'):
                    label_lines.append('Tags: ' + ','.join(sorted(info['semantic_tags'])))

            role = []
            if pc in inst_seed_pcs:
                role.append('SEED')
            if pc in backward_inst_reachable:
                role.append('BWD')
            if pc in forward_inst_reachable:
                role.append('FWD')
            if role:
                label_lines.append('Role: ' + ','.join(role))

            if pc in node_taint:
                tinfo = node_taint[pc]
                if tinfo.get('regs'):
                    label_lines.append('Tregs: ' + ','.join(sorted(tinfo['regs'])))
                if tinfo.get('mems'):
                    mems_list = tinfo['mems']
                    # 确保 mems 中元素是整数
                    int_mems = [x for x in mems_list if isinstance(x, int)]
                    mems = [f'0x{x:x}' for x in sorted(int_mems)[:3]]
                    if len(int_mems) > 3:
                        mems.append('...')
                    label_lines.append('Tmems: ' + ','.join(mems))

            if pc in inst_seed_pcs:
                color = 'goldenrod'
            elif pc in backward_inst_reachable and pc in forward_inst_reachable:
                color = 'purple'
            elif pc in backward_inst_reachable:
                color = 'blue'
            elif pc in forward_inst_reachable:
                color = 'red'
            elif inst_uses_taint.get(pc, False):
                color = 'red'
            else:
                color = 'black'

            label = '\\n'.join(label_lines)
            f.write(f'  "0x{pc:x}" [label="{label}", color="{color}"];\n')

        # ★ 使用过滤后的 edge_meta
        for (src, dst), meta in sorted(filtered_edge_meta.items()):
            if src not in selected_pcs or dst not in selected_pcs:
                continue
            kinds = meta.get('kinds', set())
            if 'control' in kinds:
                color = 'darkgreen'
                style = 'dashed'
            elif 'addr' in kinds:
                color = 'blue'
                style = 'dotted'
            else:
                color = 'black'
                style = 'solid'
            label = ','.join(sorted(kinds))
            f.write(f'  "0x{src:x}" -> "0x{dst:x}" [color="{color}", style="{style}", label="{label}"];\n')
        f.write('}\n')


def export_object_dep_dot(path, node_meta, object_edge_meta, backward_obj_reachable, forward_obj_reachable,
                          obj_seed_nodes, obj_leaf_nodes, forward_obj_sinks):
    selected_nodes = set(node_meta.keys())
    with open(path, 'w', encoding='utf-8') as f:
        f.write('digraph OBJECT_DEP {\n')
        for node_id in sorted(selected_nodes):
            meta = node_meta[node_id]
            label_lines = [meta['label'], f"[{meta['type']}]"]
            roles = []
            if node_id in obj_seed_nodes:
                roles.append('SEED')
            if node_id in backward_obj_reachable:
                roles.append('BWD')
            if node_id in forward_obj_reachable:
                roles.append('FWD')
            if node_id in obj_leaf_nodes:
                roles.append('LEAF')
            if node_id in forward_obj_sinks:
                roles.append('SINK')
            if roles:
                label_lines.append('Role: ' + ','.join(roles))
            if meta.get('semantic_tags'):
                label_lines.append('Tags: ' + ','.join(sorted(meta['semantic_tags'])))

            if node_id in obj_seed_nodes:
                color = 'goldenrod'
            elif node_id in backward_obj_reachable and node_id in forward_obj_reachable:
                color = 'purple'
            elif node_id in backward_obj_reachable:
                color = 'blue'
            elif node_id in forward_obj_reachable:
                color = 'red'
            else:
                color = 'black'

            shape = 'ellipse'
            if meta['type'] == 'imm':
                shape = 'diamond'
            elif meta['type'] == 'var':
                shape = 'box'
            elif meta['type'] == 'reg':
                shape = 'oval'
            elif meta['type'] == 'stack':
                shape = 'hexagon'

            label = safe_dot('\\n'.join(label_lines))
            f.write(f'  "{safe_dot(node_id)}" [shape="{shape}", label="{label}", color="{color}"];\n')

        for (src, dst), meta in sorted(object_edge_meta.items()):
            if src not in selected_nodes or dst not in selected_nodes:
                continue
            kinds = meta['kinds']
            if 'control' in kinds:
                color = 'darkgreen'
                style = 'dashed'
            elif 'addr' in kinds:
                color = 'blue'
                style = 'dotted'
            else:
                color = 'black'
                style = 'solid'
            label = ','.join(sorted(kinds))
            f.write(f'  "{safe_dot(src)}" -> "{safe_dot(dst)}" [color="{color}", style="{style}", label="{label}"];\n')
        f.write('}\n')


def export_cdfg_dot(path, executed_pcs, cfg_edges, inst_edge_meta, addr2line_map, inst_info, inst_seed_pcs):
    selected_pcs = _safe_int_set(executed_pcs)
    safe_cfg_edges = _safe_int_edge_set(cfg_edges)
    safe_edge_meta = _safe_int_edge_meta(inst_edge_meta)
    inst_seed_pcs = _safe_int_set(inst_seed_pcs) if inst_seed_pcs else set()
    with open(path, 'w', encoding='utf-8') as f:
        f.write('digraph CDFG {\n')
        for pc in sorted(selected_pcs):
            label_lines = [f'0x{pc:x}']
            src_info = addr2line_map.get(pc)
            if src_info:
                label_lines.append(f'{src_info[0]}:{src_info[1]}')
            info = inst_info.get(pc)
            if info:
                label_lines.append(info['disasm'])
                if info.get('semantic_tags'):
                    label_lines.append('Tags: ' + ','.join(sorted(info['semantic_tags'])))
            color = 'goldenrod' if pc in inst_seed_pcs else 'black'
            label = safe_dot('\\n'.join(label_lines))
            f.write(f'  "0x{pc:x}" [label="{label}", color="{color}"];\n')

        for src, dst in sorted(cfg_edges):
            if src in selected_pcs and dst in selected_pcs:
                f.write(f'  "0x{src:x}" -> "0x{dst:x}" [color="black"];\n')

        for (src, dst), meta in sorted(safe_edge_meta.items()):
            if src not in selected_pcs or dst not in selected_pcs:
                continue
            kinds = meta['kinds']
            if 'control' in kinds:
                color = 'darkgreen'
                style = 'dashed'
            elif 'addr' in kinds:
                color = 'blue'
                style = 'dotted'
            else:
                color = 'red'
                style = 'dashed'
            label = ','.join(sorted(kinds))
            f.write(f'  "0x{src:x}" -> "0x{dst:x}" [color="{color}", style="{style}", label="{label}"];\n')

        f.write('}\n')


# ------------------------------------------------------------------------
# JSON 摘要辅助（方向5 + 方向6）
# ------------------------------------------------------------------------
def build_direct_neighbors(object_edge_meta):
    succ, pred = build_adj_from_edge_meta(object_edge_meta)
    direct_parents = defaultdict(set)
    direct_children = defaultdict(set)

    for (src, dst), meta in object_edge_meta.items():
        direct_children[src].add(dst)
        direct_parents[dst].add(src)

    edge_details = defaultdict(list)
    for (src, dst), meta in object_edge_meta.items():
        edge_details[(src, dst)] = {
            'kinds': sorted(meta['kinds']),
            'pcs': sorted_hex_list(meta['pcs']),
            'count': meta['count'],
            'kind_counts': dict(sorted(meta['kind_counts'].items())),
        }

    return succ, pred, direct_parents, direct_children, edge_details


def build_instruction_details(executed_pcs, inst_info, inst_use_objects, inst_def_objects, inst_addr_objects,
                              inst_immediates, inst_controlled_by, inst_uses_taint, inst_repeat_suppressed,
                              inst_semantic_tags, inst_control_evidence=None, scope='full',
                              slice_inst_pcs=None, inst_seed_pcs=None):
    if scope == 'minimal':
        pcs = sorted(pc for pc in (inst_seed_pcs or set()) if isinstance(pc, int))
    elif scope == 'slice':
        pcs = sorted(pc for pc in (slice_inst_pcs or set()) if isinstance(pc, int))
    else:
        pcs = sorted(pc for pc in executed_pcs if isinstance(pc, int))

    return {
        hex(pc): {
            'disasm': inst_info.get(pc, {}).get('disasm'),
            'semantic_tags': sorted(inst_semantic_tags.get(pc, set()) | set(inst_info.get(pc, {}).get('semantic_tags', set()))),
            'use_objects': sorted(inst_use_objects.get(pc, set())),
            'def_objects': sorted(inst_def_objects.get(pc, set())),
            'addr_objects': sorted(inst_addr_objects.get(pc, set())),
            'immediates': sorted(inst_immediates.get(pc, set())),
            'controlled_by': [hex(x) if isinstance(x, int) else str(x) for x in sorted(
                (c for c in inst_controlled_by.get(pc, set()) if isinstance(c, int)))],
            'control_evidence': {
                hex(branch_pc): sorted((inst_control_evidence or {}).get((branch_pc, pc), set()))
                for branch_pc in sorted(
                    c for c in inst_controlled_by.get(pc, set()) if isinstance(c, int)
                )
            },
            'uses_taint': inst_uses_taint.get(pc, False),
            'suppressed_repeat_records': inst_repeat_suppressed.get(pc, 0),
        }
        for pc in pcs
    }


def build_object_details(node_meta, obj_def_pcs, obj_use_pcs, obj_addr_use_pcs, obj_ctrl_use_pcs,
                         direct_parents, direct_children, edge_details, scope='full',
                         sliced_node_meta=None, obj_seed_nodes=None):
    if scope == 'minimal':
        selected_nodes = sorted(obj_seed_nodes or set())
    elif scope == 'slice':
        selected_nodes = sorted((sliced_node_meta or {}).keys())
    else:
        selected_nodes = sorted(node_meta.keys())

    source_meta = sliced_node_meta if scope in ('minimal', 'slice') and sliced_node_meta is not None else node_meta

    details = {}
    for node_id in selected_nodes:
        meta = source_meta.get(node_id) or node_meta.get(node_id)
        if meta is None:
            continue

        child_edges = {}
        outgoing_prov = 0
        for child in sorted(direct_children.get(node_id, set())):
            info = edge_details.get((node_id, child), {})
            child_edges[child] = info
            outgoing_prov += int(info.get('count', 0) or 0)

        parent_edges = {}
        incoming_prov = 0
        for parent in sorted(direct_parents.get(node_id, set())):
            info = edge_details.get((parent, node_id), {})
            parent_edges[parent] = info
            incoming_prov += int(info.get('count', 0) or 0)

        defined_by = [hex(x) for x in sorted(obj_def_pcs.get(node_id, set()))]
        used_by = [hex(x) for x in sorted(obj_use_pcs.get(node_id, set()))]
        addr_used_by = [hex(x) for x in sorted(obj_addr_use_pcs.get(node_id, set()))]
        ctrl_used_by = [hex(x) for x in sorted(obj_ctrl_use_pcs.get(node_id, set()))]

        details[node_id] = {
            'type': meta['type'],
            'label': meta['label'],
            'semantic_tags': sorted(meta.get('semantic_tags', set())),
            'source_kind': meta.get('source_kind'),
            'occurrence_pc': hex(meta['occurrence_pc']) if isinstance(meta.get('occurrence_pc'), int) else meta.get('occurrence_pc'),
            'operand_index': meta.get('operand_index'),
            'value_hex': meta.get('value_hex'),
            'bit_size': meta.get('bit_size'),
            'defined_by': defined_by,
            'used_by': used_by,
            'addr_used_by': addr_used_by,
            'ctrl_used_by': ctrl_used_by,
            'defined_by_count': len(defined_by),
            'used_by_count': len(used_by),
            'addr_used_by_count': len(addr_used_by),
            'ctrl_used_by_count': len(ctrl_used_by),
            'direct_parents': sorted(direct_parents.get(node_id, set())),
            'direct_children': sorted(direct_children.get(node_id, set())),
            'direct_parent_count': len(direct_parents.get(node_id, set())),
            'direct_child_count': len(direct_children.get(node_id, set())),
            'incoming_provenance_total': incoming_prov,
            'outgoing_provenance_total': outgoing_prov,
            'parent_edge_details': parent_edges,
            'child_edge_details': child_edges,
        }

    return details

# ==================== 安全过滤工具函数 ====================

def _safe_int_set(s):
    """过滤集合/可迭代对象，只保留整数元素"""
    return {x for x in s if isinstance(x, int)}


def _safe_int_edge_meta(edge_meta):
    """过滤 edge_meta 字典，只保留键为 (int, int) 的条目"""
    return {
        (src, dst): meta
        for (src, dst), meta in edge_meta.items()
        if isinstance(src, int) and isinstance(dst, int)
    }


def _safe_int_edge_set(edge_set):
    """过滤边集合，只保留 (int, int) 的元组"""
    return {
        (src, dst) for (src, dst) in edge_set
        if isinstance(src, int) and isinstance(dst, int)
    }


# ------------------------------------------------------------------------
# 主逻辑
# ------------------------------------------------------------------------
def main():
    args = parse_args(sys.argv[1:])
    mode_opts = resolve_mode_options(args)

    global CONTROL_EXPANSION_MODE
    CONTROL_EXPANSION_MODE = mode_opts['control_expansion_mode']

    max_instructions = mode_opts['max_insts']
    taint_symbol_name = mode_opts['secret_symbol']
    default_secret_len = mode_opts['secret_len']
    output_prefix = mode_opts['output_prefix']

    path = args.binary

    # -------------------- 静态准备 --------------------
    segs, entry = load_all_code_segments(path)
    addr2line_map = build_addr2line_map(path)
    symbol_addr_map = build_symbol_addr_map(path)
    global_objects, global_var_by_addr = build_global_objects(path)
    got_map = build_got_plt_map(path)
    main_addr, plt_ranges, text_end = get_main_and_plt_ranges(path)

    ctx = TritonContext()
    ctx.setArchitecture(ARCH.X86_64)
    print(f'[+] Triton initialized, entry = 0x{entry:x}')
    print(f'[+] Mode = {mode_opts["mode"]}, control_expansion_mode = {CONTROL_EXPANSION_MODE}')
    print(f'[+] Object DOT view = {mode_opts["object_dot_view"]}, Inst DOT view = {mode_opts["inst_dot_view"]}')

    for vaddr, data in segs:
        ctx.setConcreteMemoryAreaValue(vaddr, bytearray(data))

    # 静态阶段：只对 CFG 完整的函数建立后支配控制区域；其余函数运行时回退。
    static_control_model = build_static_control_model(ctx, path)
    static_ctrl_stats = static_control_model.get('stats', {})
    print(
        f'[+] Static postdom control model: '
        f'functions={static_ctrl_stats.get("functions_modeled", 0)}/'
        f'{static_ctrl_stats.get("functions_seen", 0)} '
        f'branches={static_ctrl_stats.get("branches_modeled", 0)} '
        f'fallback_functions={static_ctrl_stats.get("functions_fallback", 0)}'
    )

    # -------------------- 运行时初始化 --------------------
    STACK_ADDR, STACK_SIZE = 0x70000000, 0x20000
    ctx.setConcreteMemoryAreaValue(STACK_ADDR, bytearray(STACK_SIZE))

    process_vector = build_minimal_sysv_process_vector(
        stack_addr=STACK_ADDR,
        stack_size=STACK_SIZE,
        argv=('prog',),
    )
    ctx.setConcreteMemoryAreaValue(
        process_vector['initial_rsp'], process_vector['entry_stack_image']
    )
    for string_addr, string_bytes in process_vector['string_writes']:
        ctx.setConcreteMemoryAreaValue(string_addr, string_bytes)

    # 这里执行的是 ELF e_entry/_start，不是 main；进程参数必须从初始栈传入。
    ctx.setConcreteRegisterValue(ctx.registers.rsp, process_vector['initial_rsp'])
    ctx.setConcreteRegisterValue(ctx.registers.rip, entry)

    print(
        f'[+] SysV initial stack: rsp=0x{process_vector["initial_rsp"]:x} '
        f'argc={process_vector["argc"]} '
        f'argv=0x{process_vector["argv_addr"]:x} '
        f'envp=0x{process_vector["envp_addr"]:x}'
    )

    # 定位污点源对象
    taint_source_addr = None
    taint_source_size = default_secret_len
    for obj in global_objects:
        if obj['name'] == taint_symbol_name:
            taint_source_addr = obj['addr']
            if obj['size'] > 0:
                taint_source_size = obj['size']
            break

    if taint_source_addr is None:
        raise RuntimeError(f"Cannot find global symbol '{taint_symbol_name}' in ELF")

    # 当前依赖提取只消费 Triton 污点状态；不创建未使用的逐字节符号 AST。
    taint_memory_region(ctx, taint_source_addr, taint_source_size)

    print(
        f'[+] Secret region tainted (symbolization disabled): '
        f'{taint_symbol_name} 0x{taint_source_addr:x}-'
        f'0x{taint_source_addr + taint_source_size - 1:x}'
    )

    objcanon = ObjectCanonicalizer(
        ctx=ctx,
        global_objects=global_objects,
        stack_addr=STACK_ADDR,
        stack_size=STACK_SIZE,
        taint_symbol_name=taint_symbol_name,
        taint_source_addr=taint_source_addr,
        taint_source_size=taint_source_size,
    )

    hooks = {
        'printf': hook_printf,
        'strlen': hook_strlen,
    }

    exit_addr = None
    if text_end is not None:
        exit_addr = text_end + 0x10
        ctx.setConcreteMemoryAreaValue(exit_addr, bytes([0xF4]))

    code_ranges = [(vaddr, vaddr + len(data)) for vaddr, data in segs]
    if exit_addr is not None:
        code_ranges.append((exit_addr, exit_addr + 1))

    def in_loaded_code(addr):
        return any(s <= addr < e for s, e in code_ranges)

    def in_plt(addr):
        return any(s <= addr < e for s, e in plt_ranges)

    # -------------------- 图/分析状态 --------------------
    cfg_edges = set()
    back_edge_taken = defaultdict(int)
    node_taint = {}
    tainted_regs = set()
    tainted_mems = set()

    inst_info = {}
    pc_hit_count = defaultdict(int)
    inst_uses_taint = {}
    inst_taint_io = {}

    # 指令级 use/def / immediate / 地址 / 控制信息
    inst_use_objects = defaultdict(set)
    inst_def_objects = defaultdict(set)
    inst_addr_objects = defaultdict(set)
    inst_immediates = defaultdict(set)
    inst_ctrl_objects = defaultdict(set)
    inst_controlled_by = defaultdict(set)
    inst_control_evidence = defaultdict(set)
    inst_semantic_tags = defaultdict(set)

    # 三张强类型边表：禁止 PC、对象 ID 和对象关系互相混入。
    #   inst_edge_meta:       (int PC, int PC) -> data/addr/control
    #   object_edge_meta:     (str OID, str OID) -> data/addr/control
    #   object_relation_meta: (str OID, str OID) -> alias/member-of/equivalence
    inst_edge_meta = {}
    object_relation_meta = {}

    # 对象级依赖图
    node_meta = {}

    # seed-slice 构建期再生成的对象图 / 对象事实
    object_edge_meta = {}
    obj_def_pcs = defaultdict(set)
    obj_use_pcs = defaultdict(set)
    obj_addr_use_pcs = defaultdict(set)
    obj_ctrl_use_pcs = defaultdict(set)

    # 每条指令实际触达的“内存对象”集合（仅 load/store 对象）
    inst_mem_objects = defaultdict(set)

    # 对象最近定义：方向3改为统一使用 canonical obj_id -> pc
    last_def_obj = {}

    # === 方案2修订：内存别名追踪器（修订点3）===
    mem_alias_tracker = MemoryAliasTracker()

    # === 方案2修订：统计计数器 ===
    zero_idiom_count = 0          # 修订点1：自归零短路次数
    partial_rmw_count = 0         # 修订点2：partial-write RMW 次数
    mem_alias_extension_count = 0 # 修订点3：别名展开次数
    caller_saved_inject_count = 0 # 修订点4：caller-saved 注入次数
    imm_inst_edge_count = 0       # 修订点5：immediate 指令级边数

    # 保留原有较粗粒度指令 DFG（仅数据）
    dfg_edges = set()
    last_def_reg = {}
    last_def_mem = {}

    # 方向4：重复动态事实模式摘要
    loop_pattern_stats = {}
    loop_unique_patterns = 0
    loop_suppressed_records = 0
    loop_new_pattern_disabled = 0
    inst_repeat_suppressed = defaultdict(int)

    # 动态执行控制
    inst_count = 0
    done = False
    entered_main = False
    call_stack = []
    call_depth = 0

    # 在线控制依赖上下文（替代 trace / branch_events + 事后重建）
    active_control_context = []
    active_control_keys = set()
    static_control_context_pushes = 0
    fallback_control_context_pushes = 0

    debug_start_ts = time.time()
    max_active_ctrl_len = 0
    max_call_depth_seen = 0

    # 初始化 taint source 对象节点（方向3：经 canonicalizer 统一生成）
    seed_obj_id, seed_obj_type, seed_obj_label, seed_meta = objcanon.canon_named_seed(taint_symbol_name)
    ensure_node(node_meta, seed_obj_id, seed_obj_type, seed_obj_label, **seed_meta)

    # ==================== 修订点7 Step 7.1：seed 地址范围映射表 ====================
    # 建立 seed 符号变量 → 运行时地址范围的桥接表
    # 用于在指令执行循环中将 mem:0xNNNNNN 类对象关联回 var:XXXX 种子对象

    seed_address_ranges = {}  # { seed_obj_id: (start_addr, end_addr) }

    # 从 taint_source 配置中提取 seed 的地址范围（这是最可靠的来源）
    if taint_source_addr is not None and taint_source_size is not None and taint_source_size > 0:
        seed_start = taint_source_addr
        seed_end = taint_source_addr + taint_source_size - 1
        seed_address_ranges[seed_obj_id] = (seed_start, seed_end)
        print(f'[plan2-fix7] seed address range: {seed_obj_id} -> '
              f'[0x{seed_start:x}, 0x{seed_end:x}] (size={taint_source_size})')

    # 从 global_objects 中补充：匹配 seed_obj_id 对应的符号名
    # global_objects 格式: [{'name': str, 'addr': int, 'size': int, 'type': str}, ...]
    # seed_obj_id 格式: "var:array2"  →  提取符号名 "array2"
    seed_symbol_name = seed_obj_id[4:] if seed_obj_id.startswith('var:') else seed_obj_id

    if isinstance(global_objects, list):
        for item in global_objects:
            if not isinstance(item, dict):
                continue
            sym_name = item.get('name', '')
            sym_addr = item.get('addr', 0)
            sym_size = item.get('size', 0)
            if not sym_name or not sym_addr:
                continue
            candidate_oid = f'var:{sym_name}'
            # 只匹配与 seed 相同符号名的条目（此时 obj_seed_nodes 尚未定义，用 seed_obj_id 直接比较）
            if candidate_oid == seed_obj_id and candidate_oid not in seed_address_ranges:
                if sym_size and sym_size > 0:
                    seed_address_ranges[candidate_oid] = (sym_addr, sym_addr + sym_size - 1)
                    print(f'[plan2-fix7] additional seed range from global_objects: {candidate_oid} -> '
                          f'[0x{sym_addr:x}, 0x{sym_addr + sym_size - 1:x}]')
    elif isinstance(global_objects, dict):
        for sym_name, val in global_objects.items():
            if isinstance(val, (list, tuple)) and len(val) >= 2:
                sym_addr, sym_size = val[0], val[1]
            elif isinstance(val, dict):
                sym_addr = val.get('addr', val.get('address', 0))
                sym_size = val.get('size', 0)
            else:
                continue
            candidate_oid = f'var:{sym_name}'
            if candidate_oid == seed_obj_id and candidate_oid not in seed_address_ranges:
                if sym_size and sym_size > 0:
                    seed_address_ranges[candidate_oid] = (sym_addr, sym_addr + sym_size - 1)
                    print(f'[plan2-fix7] additional seed range from global_objects: {candidate_oid} -> '
                          f'[0x{sym_addr:x}, 0x{sym_addr + sym_size - 1:x}]')

    # 如果以上都没成功建立范围，打印警告
    if not seed_address_ranges:
        print(f'[plan2-fix7] WARNING: no seed address range established for {seed_obj_id}! '
              f'Bridge will not function.')

    def addr_belongs_to_seed(addr):
        """检查给定地址是否落在任何 seed 的地址范围内，返回 seed_obj_id 或 None"""
        for s_oid, (s_start, s_end) in seed_address_ranges.items():
            if s_start <= addr <= s_end:
                return s_oid
        return None

    def objs_touch_seed(obj_set):
        """检查对象集合中是否有任何对象属于 seed 范围"""
        for oid in obj_set:
            if oid in seed_address_ranges:
                return True
            # 检查 mem:0xNNNN 格式
            if oid.startswith('mem:'):
                try:
                    addr_str = oid[4:]
                    addr_val = int(addr_str, 16) if addr_str.startswith('0x') else int(addr_str)
                    if addr_belongs_to_seed(addr_val) is not None:
                        return True
                except (ValueError, IndexError):
                    pass
        return False

    def bridge_mem_objs_to_seed(obj_set):
        """
        对给定对象集合中的 mem:0xNNNN 对象，检查是否落在 seed 地址范围内。
        如果是，返回需要添加的桥接边集合 + 需要添加到对象集合中的 seed obj_id。
        
        返回: (bridged_seed_ids: set, bridge_edges: list of (src, dst, edge_type))
        """
        bridged_seed_ids = set()
        bridge_edges = []
        for oid in obj_set:
            if oid.startswith('mem:'):
                try:
                    addr_str = oid[4:]
                    addr_val = int(addr_str, 16) if addr_str.startswith('0x') else int(addr_str)
                    matched_seed = addr_belongs_to_seed(addr_val)
                    if matched_seed is not None:
                        bridged_seed_ids.add(matched_seed)
                        # 双向桥接边：mem:addr <-> var:array2
                        bridge_edges.append((oid, matched_seed, 'seed_bridge'))
                        bridge_edges.append((matched_seed, oid, 'seed_bridge'))
                except (ValueError, IndexError):
                    pass
        return bridged_seed_ids, bridge_edges

    # 调试计数器
    seed_bridge_count = 0
    seed_touch_no_suppress_count = 0

    # 在主循环之前定义
    SSE_FLOAT_OPCODES = frozenset({
    'cvtsi2ss', 'cvtsi2sd', 'cvtss2sd', 'cvtsd2ss',
    'cvttss2si', 'cvttsd2si', 'cvtss2si', 'cvtsd2si',
    'addss', 'addsd', 'subss', 'subsd',
    'mulss', 'mulsd', 'divss', 'divsd',
    'sqrtss', 'sqrtsd', 'maxss', 'maxsd', 'minss', 'minsd',
    'movss', 'movsd', 'movaps', 'movups', 'movapd', 'movupd',
    'ucomiss', 'ucomisd', 'comiss', 'comisd',
    'xorps', 'xorpd', 'andps', 'andpd', 'orps', 'orpd',
    'shufps', 'shufpd', 'unpcklps', 'unpckhps',
    'cvtdq2ps', 'cvtps2dq', 'cvttps2dq',
    'pxor', 'por', 'pand', 'pandn',
    'roundss', 'roundsd',
    })

    _sse_chain_int_to_float_inputs = {}
    _sse_float_reg_shadow = {}
    BACK_EDGE_LIMIT = 500

    # -------------------- 动态执行 --------------------
    while not done:
        if inst_count >= max_instructions:
            print(f'[warn] instruction limit reached ({max_instructions}), stopping.')
            break

        pc = ctx.getConcreteRegisterValue(ctx.registers.rip)
        pc_hit_count[pc] += 1

        if call_depth > max_call_depth_seen:
            max_call_depth_seen = call_depth

        _before_ctrl_len = len(active_control_context)
        pop_inactive_control_context(active_control_context, active_control_keys, pc, call_depth)
        _after_ctrl_len = len(active_control_context)

        if DEBUG_CTRL_VERBOSE and _after_ctrl_len != _before_ctrl_len:
            print(
                f'[dbg] ctrl-pop: pc={hex_pc(pc)} '
                f'before={_before_ctrl_len} after={_after_ctrl_len} '
                f'call_depth={call_depth}'
            )

        if not in_loaded_code(pc):
            if call_stack:
                ret_addr = call_stack.pop()
                call_depth = max(call_depth - 1, 0)
                if not in_loaded_code(ret_addr):
                    done = True
                    break
                ctx.setConcreteRegisterValue(ctx.registers.rip, ret_addr)
                continue
            break

        opcode = ctx.getConcreteMemoryAreaValue(pc, 16)
        inst = Instruction()
        inst.setOpcode(opcode)
        inst.setAddress(pc)
        ctx.disassembly(inst)

        disasm = inst.getDisassembly()
        opc = disasm.split()[0].lower() if disasm else 'unknown'
        inst_info[pc] = {'opc': opc, 'disasm': disasm, 'size': inst.getSize()}

        if DEBUG_PROGRESS and inst_count > 0 and inst_count % DEBUG_PROGRESS_EVERY == 0:
            debug_print_progress(
                inst_count, pc, disasm, call_depth, call_stack,
                active_control_context, pc_hit_count, debug_start_ts
            )

        if DEBUG_HOTSPOT and inst_count > 0 and inst_count % DEBUG_HOTSPOT_EVERY == 0:
            debug_print_hotspots(pc_hit_count, inst_info, DEBUG_HOTSPOT_TOPN)

        if DEBUG_PC_STALL_WARN:
            cur_hit = pc_hit_count.get(pc, 0)
            if cur_hit > 0 and cur_hit % DEBUG_PC_STALL_THRESHOLD == 0:
                print(
                    f'[warn] hotspot/stall suspect: '
                    f'pc={hex_pc(pc)} hit={cur_hit} '
                    f'call_depth={call_depth} active_ctrl={len(active_control_context)} '
                    f'disasm={disasm}'
                )

        # 特殊指令
        if opc == 'rdtscp':
            old_pc = pc
            hook_rdtscp(ctx, inst_count, inst)
            new_pc = ctx.getConcreteRegisterValue(ctx.registers.rip)
            cfg_edges.add((old_pc, new_pc))

            apply_online_control_to_inst(
                old_pc,
                set(),
                active_control_context,
                call_depth,
                inst_controlled_by,
                inst_ctrl_objects,
                inst_edge_meta,
                obj_ctrl_use_pcs,
                inst_control_evidence,
            )

            inst_count += 1
            continue

        if opc.startswith('clflush'):
            old_pc = pc
            hook_clflush(ctx, inst)
            new_pc = ctx.getConcreteRegisterValue(ctx.registers.rip)
            cfg_edges.add((old_pc, new_pc))

            apply_online_control_to_inst(
                old_pc,
                set(),
                active_control_context,
                call_depth,
                inst_controlled_by,
                inst_ctrl_objects,
                inst_edge_meta,
                obj_ctrl_use_pcs,
                inst_control_evidence,
            )

            inst_count += 1
            continue
        
        # ==================== 修订点10：SSE/AVX 浮点指令 fallthrough 保护 ====================
        _is_sse_float = opc in SSE_FLOAT_OPCODES

        # 普通指令执行
        ctx.processing(inst)
        inst_count += 1

        # ★ 关键：立即获取 next_pc（在任何后续检查之前）
        next_pc = ctx.getConcreteRegisterValue(ctx.registers.rip)

        # ==================== 修订点10A：SSE 浮点链语义模拟 ====================
        if _is_sse_float and next_pc == pc:
            # RIP 卡住，Triton 无法执行此浮点指令，强制推进
            expected_next = pc + inst.getSize()
            ctx.setConcreteRegisterValue(ctx.registers.rip, expected_next)
            next_pc = expected_next

            # --- 浮点链语义模拟 ---
            operands = inst.getOperands()

            # ==== 辅助函数：从操作数读取浮点 shadow 值 ====
            def _get_sse_src_val(op):
                """从寄存器或内存操作数获取浮点 shadow 值"""
                if op.getType() == OPERAND.REG:
                    return _sse_float_reg_shadow.get(op.getName())
                elif op.getType() == OPERAND.MEM:
                    try:
                        import struct
                        mem_addr = op.getAddress()
                        mem_size = op.getSize()
                        raw = ctx.getConcreteMemoryAreaValue(mem_addr, mem_size)
                        if mem_size == 4:
                            return struct.unpack('<f', bytes(raw))[0]
                        elif mem_size == 8:
                            return struct.unpack('<d', bytes(raw))[0]
                    except Exception:
                        pass
                return None

            # ==== 辅助函数：从操作数读取整数值 ====
            def _get_int_src_val(op):
                """从寄存器或内存操作数获取整数值"""
                if op.getType() == OPERAND.REG:
                    return ctx.getConcreteRegisterValue(op)
                elif op.getType() == OPERAND.MEM:
                    try:
                        mem_addr = op.getAddress()
                        mem_size = op.getSize()
                        raw = ctx.getConcreteMemoryAreaValue(mem_addr, mem_size)
                        return int.from_bytes(raw, byteorder='little', signed=False)
                    except Exception:
                        pass
                return None

            # ---- 分类处理各种 SSE 指令 ----

            if opc in ('cvtsi2ss', 'cvtsi2sd'):
                # 整数 → 浮点转换（链的入口）
                if len(operands) >= 2:
                    dst_op = operands[0]
                    src_op = operands[1]

                    src_val = _get_int_src_val(src_op)

                    if src_val is not None and dst_op.getType() == OPERAND.REG:
                        xmm_name = dst_op.getName()
                        _sse_float_reg_shadow[xmm_name] = float(src_val)
                        _sse_chain_int_to_float_inputs[xmm_name] = (src_val, pc)

                        if pc_hit_count.get(pc, 0) <= 2:
                            print(f'[sse-sim] cvtsi2ss/sd at {hex_pc(pc)}: '
                                  f'{xmm_name} <- float({src_val})')

            elif opc in ('divss', 'divsd'):
                # 浮点除法: dst = dst / src
                if len(operands) >= 2:
                    dst_op = operands[0]
                    src_op = operands[1]

                    if dst_op.getType() == OPERAND.REG:
                        dst_name = dst_op.getName()
                        dst_val = _sse_float_reg_shadow.get(dst_name)
                        src_val = _get_sse_src_val(src_op)

                        if dst_val is not None and src_val is not None and src_val != 0.0:
                            _sse_float_reg_shadow[dst_name] = dst_val / src_val

            elif opc in ('mulss', 'mulsd'):
                # 浮点乘法: dst = dst * src
                if len(operands) >= 2:
                    dst_op = operands[0]
                    src_op = operands[1]

                    if dst_op.getType() == OPERAND.REG:
                        dst_name = dst_op.getName()
                        dst_val = _sse_float_reg_shadow.get(dst_name)
                        src_val = _get_sse_src_val(src_op)

                        if dst_val is not None and src_val is not None:
                            _sse_float_reg_shadow[dst_name] = dst_val * src_val

            elif opc in ('addss', 'addsd'):
                # 浮点加法: dst = dst + src
                if len(operands) >= 2:
                    dst_op = operands[0]
                    src_op = operands[1]

                    if dst_op.getType() == OPERAND.REG:
                        dst_name = dst_op.getName()
                        dst_val = _sse_float_reg_shadow.get(dst_name)
                        src_val = _get_sse_src_val(src_op)

                        if dst_val is not None and src_val is not None:
                            _sse_float_reg_shadow[dst_name] = dst_val + src_val

            elif opc in ('subss', 'subsd'):
                # 浮点减法: dst = dst - src
                if len(operands) >= 2:
                    dst_op = operands[0]
                    src_op = operands[1]

                    if dst_op.getType() == OPERAND.REG:
                        dst_name = dst_op.getName()
                        dst_val = _sse_float_reg_shadow.get(dst_name)
                        src_val = _get_sse_src_val(src_op)

                        if dst_val is not None and src_val is not None:
                            _sse_float_reg_shadow[dst_name] = dst_val - src_val

            elif opc in ('sqrtss', 'sqrtsd'):
                # 浮点开方
                if len(operands) >= 2:
                    dst_op = operands[0]
                    src_op = operands[1]

                    src_val = _get_sse_src_val(src_op)

                    if (dst_op.getType() == OPERAND.REG and
                            src_val is not None and src_val >= 0.0):
                        import math
                        _sse_float_reg_shadow[dst_op.getName()] = math.sqrt(src_val)

            elif opc in ('cvttss2si', 'cvttsd2si', 'cvtss2si', 'cvtsd2si'):
                # 浮点 → 整数转换（链的出口）
                if len(operands) >= 2:
                    dst_op = operands[0]  # 整数目标寄存器
                    src_op = operands[1]  # xmm 源

                    if dst_op.getType() == OPERAND.REG and src_op.getType() == OPERAND.REG:
                        src_name = src_op.getName()
                        shadow_val = _sse_float_reg_shadow.get(src_name)

                        if shadow_val is not None:
                            int_result = int(shadow_val)
                            if int_result < 0:
                                int_result = max(int_result, -(1 << 63))
                            else:
                                int_result = min(int_result, (1 << 63) - 1)

                            ctx.setConcreteRegisterValue(
                                dst_op, int_result & 0xFFFFFFFFFFFFFFFF)

                            if pc_hit_count.get(pc, 0) <= 2:
                                print(f'[sse-sim] cvttss2si at {hex_pc(pc)}: '
                                      f'{dst_op.getName()} <- int({shadow_val}) = {int_result}')
                        else:
                            fallback_info = _sse_chain_int_to_float_inputs.get(src_name)
                            if fallback_info is not None:
                                original_val, _ = fallback_info
                                ctx.setConcreteRegisterValue(
                                    dst_op, original_val & 0xFFFFFFFFFFFFFFFF)

                                if pc_hit_count.get(pc, 0) <= 2:
                                    print(f'[sse-sim] cvttss2si at {hex_pc(pc)}: '
                                          f'{dst_op.getName()} <- {original_val} '
                                          f'(fallback: identity for {src_name})')
                            else:
                                if pc_hit_count.get(pc, 0) <= 2:
                                    print(f'[sse-sim] cvttss2si at {hex_pc(pc)}: '
                                          f'no shadow for {src_name}, keeping value')

            elif opc in ('cvtss2sd', 'cvtsd2ss'):
                # 浮点精度转换：shadow 值直接传播
                if len(operands) >= 2:
                    dst_op = operands[0]
                    src_op = operands[1]

                    src_val = _get_sse_src_val(src_op)
                    if dst_op.getType() == OPERAND.REG and src_val is not None:
                        _sse_float_reg_shadow[dst_op.getName()] = src_val

            elif opc in ('movss', 'movsd', 'movaps', 'movups', 'movapd', 'movupd'):
                # 浮点 mov：传播 shadow
                if len(operands) >= 2:
                    dst_op = operands[0]
                    src_op = operands[1]

                    if dst_op.getType() == OPERAND.REG and src_op.getType() == OPERAND.REG:
                        src_val = _sse_float_reg_shadow.get(src_op.getName())
                        if src_val is not None:
                            _sse_float_reg_shadow[dst_op.getName()] = src_val
                    elif dst_op.getType() == OPERAND.REG and src_op.getType() == OPERAND.MEM:
                        loaded = _get_sse_src_val(src_op)
                        if loaded is not None:
                            _sse_float_reg_shadow[dst_op.getName()] = loaded

            elif opc in ('xorps', 'xorpd', 'pxor'):
                # 自身异或 = 清零
                if len(operands) >= 2:
                    dst_op = operands[0]
                    src_op = operands[1]

                    if (dst_op.getType() == OPERAND.REG and
                        src_op.getType() == OPERAND.REG and
                        dst_op.getName() == src_op.getName()):
                        _sse_float_reg_shadow[dst_op.getName()] = 0.0

            elif opc in ('ucomiss', 'ucomisd', 'comiss', 'comisd'):
                # 比较指令：不修改操作数，不需要 shadow 更新
                pass

            # 打印诊断
            if pc_hit_count.get(pc, 0) <= 2 and opc not in (
                'cvtsi2ss', 'cvtsi2sd',
                'cvttss2si', 'cvttsd2si', 'cvtss2si', 'cvtsd2si',
            ):
                print(f'[sse-fix] RIP stall at {hex_pc(pc)}: {disasm}, '
                      f'forced advance to {hex_pc(expected_next)}')

        # --- CFG 边记录 ---
        cfg_edges.add((pc, next_pc))

        # ==================== 以下继续原有的 read_regs_info 等逻辑 ====================
        read_regs_info = list(inst.getReadRegisters())
        written_regs_info = list(inst.getWrittenRegisters())
        read_mems_info = list(inst.getLoadAccess())
        written_mems_info = list(inst.getStoreAccess())
        read_imms_info = []
        
        try:
            read_imms_info = list(inst.getReadImmediates())
        except Exception:
            read_imms_info = []

        read_regs = [reg for reg, _ in read_regs_info]
        written_regs = [reg for reg, _ in written_regs_info]
        read_mems = [mem for mem, _ in read_mems_info]
        written_mems = [mem for mem, _ in written_mems_info]

        inst_site_tags = classify_instruction_semantics(
            ctx=ctx,
            inst=inst,
            opc=opc,
            read_regs_info=read_regs_info,
            written_regs_info=written_regs_info,
            read_mems_info=read_mems_info,
            written_mems_info=written_mems_info,
        )
        inst_semantic_tags[pc].update(inst_site_tags)
        inst_info[pc]['semantic_tags'] = set(inst_semantic_tags[pc])

        # ---------- 局部依赖事实：先收集，再决定是否写入持久结构 ----------
        local_raw_inst_data_edges = set()
        local_canonical_inst_data_edges = set()
        local_inst_addr_edges = set()
        local_object_relations = set()

        use_objs = set()
        def_objs = set()
        addr_objs = set()
        imm_objs = set()
        mem_objs_local = set()

        _is_zero_idiom = is_self_zero_idiom(
            opc=opc,
            read_regs_info=read_regs_info,
            written_regs_info=written_regs_info,
            read_mems_info=read_mems_info,
            written_mems_info=written_mems_info,
            has_immediates=bool(read_imms_info),
            get_parent_reg_name_fn=get_parent_reg_name,
            ctx=ctx,
        )
        if _is_zero_idiom:
            zero_idiom_count += 1

        operands = list(inst.getOperands())
        pure_reg_move = is_pure_register_move(
            ctx=ctx,
            inst=inst,
            opc=opc,
            read_regs_info=read_regs_info,
            written_regs_info=written_regs_info,
            read_mems_info=read_mems_info,
            written_mems_info=written_mems_info,
            has_immediates=bool(read_imms_info),
        )

        # ---------- 指令级：原始 DFG（仅最近定义，先本地收集） ----------
        for reg in read_regs:
            rname = reg.getName()
            if rname in last_def_reg:
                local_raw_inst_data_edges.add((last_def_reg[rname], pc))

        for mem in read_mems:
            maddr = mem.getAddress()
            if maddr in last_def_mem:
                local_raw_inst_data_edges.add((last_def_mem[maddr], pc))

        # ---------- 对象节点收集：寄存器 / 内存 / immediate ----------
        # 读寄存器对象（方向3：统一 reg canonical id）
        for reg, _ in read_regs_info:
            obj_id, _, _, _ = objcanon.canon_reg(reg)

            # === 方案2修订点1：自归零短路 ===
            # 对于 xor rax, rax 这种归零模式，src reg 不应被视为"被使用"
            # 否则会错误地认为 rax 的旧值传播给了归零后的 rax
            if _is_zero_idiom:
                # 不加入 use_objs，不连 last_def_obj 的边
                # 但仍记录到 inst_addr_objects 之外的辅助结构以便调试
                add_node_tags(node_meta, obj_id, 'self_zero_idiom_src_suppressed')
                continue

            use_objs.add(obj_id)
            if obj_id in last_def_obj:
                local_canonical_inst_data_edges.add((last_def_obj[obj_id], pc))

        # 写寄存器对象
        for reg, _ in written_regs_info:
            obj_id, _, _, _ = objcanon.canon_reg(reg)
            def_objs.add(obj_id)

            # === 方案2修订点2：partial-write read-modify-write 语义 ===
            # 对 16/8 位写入（如 mov al, ...），parent reg (rax) 的高位被保留
            # 必须把 parent 作为隐式 use，并连 last_def_obj 的边
            _is_rmw, _child_name, _parent_name = is_partial_write_rmw(
                reg, ctx, get_parent_reg_name
            )
            if _is_rmw and not _is_zero_idiom:
                # parent oid 就是当前 obj_id（因为 canon_reg 已经归一化到 parent）
                # 但我们需要让"这条指令使用了 parent 的旧值"这一事实显式化
                # parent 的最近定义就是 last_def_obj[obj_id]（如果存在）
                if obj_id in last_def_obj:
                    last_def_pc = last_def_obj[obj_id]
                    # 关键：把 parent 加入 use_objs，建立 RMW 依赖
                    use_objs.add(obj_id)
                    local_canonical_inst_data_edges.add((last_def_pc, pc))
                    partial_rmw_count += 1
                    add_node_tags(node_meta, obj_id, 'partial_write_rmw_parent')
                add_inst_tags(inst_semantic_tags, pc, 'partial_write_rmw')

            role_tags = set()
            if pure_reg_move:
                role_tags.update({'carrier', 'transient_move_only_carrier'})
            add_node_tags(node_meta, obj_id, *role_tags)

        # 读内存对象（值依赖）
        for mem, _ in read_mems_info:
            mem_addr = mem.getAddress()
            mem_size = mem.getSize()
            obj_id, _, _, _ = objcanon.canon_memory_access(
                mem_addr, mem_size, mem=mem
            )

            # === 方案2修订点3：物理地址别名展开 ===
            # 注册到别名追踪器，获取所有等价 oid
            alias_oids = mem_alias_tracker.register(obj_id, mem_addr, mem_size)
            if len(alias_oids) > 1:
                mem_alias_extension_count += 1

            for alias_oid in alias_oids:
                use_objs.add(alias_oid)
                mem_objs_local.add(alias_oid)
                if alias_oid in last_def_obj:
                    local_canonical_inst_data_edges.add((last_def_obj[alias_oid], pc))

            # 即使 obj_id 本身没在 last_def_obj 里，别名可能有
            # 上面的循环已经处理了

        # 写内存对象（定义）
        for mem, _ in written_mems_info:
            mem_addr = mem.getAddress()
            mem_size = mem.getSize()
            obj_id, _, _, _ = objcanon.canon_memory_access(
                mem_addr, mem_size, mem=mem
            )

            # === 方案2修订点3：写侧也注册别名 ===
            alias_oids = mem_alias_tracker.register(obj_id, mem_addr, mem_size)
            if len(alias_oids) > 1:
                mem_alias_extension_count += 1

            for alias_oid in alias_oids:
                def_objs.add(alias_oid)
                mem_objs_local.add(alias_oid)

        # immediate 对象（修订版：按“出现点级 / 语义站点级”建模）
        # 仅从操作数枚举构建 immediate 节点，避免 read_imms 与地址位移重复混淆。
        for operand_index, op in enumerate(operands):
            try:
                if op.getType() != OPERAND.IMM:
                    continue
            except Exception:
                continue

            imm_tags = classify_immediate_semantics(
                ctx=ctx,
                inst=inst,
                pc=pc,
                opc=opc,
                operand_index=operand_index,
                imm_obj=op,
                value=op.getValue(),
                bit_size=op.getBitSize() if hasattr(op, 'getBitSize') else None,
                source_kind='operand_imm',
                in_plt_site=in_plt(pc),
                pc_hit_count_for_site=pc_hit_count.get(pc, 1),
            )
            obj_id, obj_type, label, imm_meta = objcanon.canon_imm_occurrence(
                op,
                pc=pc,
                operand_index=operand_index,
                source_kind='operand_imm',
                bit_size=op.getBitSize() if hasattr(op, 'getBitSize') else None,
                semantic_tags=imm_tags,
            )
            ensure_node(node_meta, obj_id, obj_type, label, **imm_meta)
            imm_objs.add(obj_id)
            use_objs.add(obj_id)

        # 地址对象（从 memory operand 解析出 base/index/disp/scale/segment/pc-relative）
        mem_operands = [
            (idx, op)
            for idx, op in enumerate(operands)
            if op.getType() == OPERAND.MEM
        ]
        for operand_index, mop in mem_operands:
            try:
                breg = mop.getBaseRegister()
                if breg and breg.getName():
                    obj_id, obj_type, label, reg_meta = objcanon.canon_reg(breg)
                    ensure_node(node_meta, obj_id, obj_type, label, **reg_meta)
                    addr_objs.add(obj_id)
                    add_node_tags(node_meta, obj_id, 'address_base')
            except Exception:
                pass

            try:
                ireg = mop.getIndexRegister()
                if ireg and ireg.getName():
                    obj_id, obj_type, label, reg_meta = objcanon.canon_reg(ireg)
                    ensure_node(node_meta, obj_id, obj_type, label, **reg_meta)
                    addr_objs.add(obj_id)
                    add_node_tags(node_meta, obj_id, 'address_index')
            except Exception:
                pass

            try:
                sreg = mop.getSegmentRegister()
                if sreg and sreg.getName():
                    obj_id, obj_type, label, reg_meta = objcanon.canon_reg(sreg)
                    ensure_node(node_meta, obj_id, obj_type, label, **reg_meta)
                    addr_objs.add(obj_id)
                    add_node_tags(node_meta, obj_id, 'address_segment')
            except Exception:
                pass

            try:
                disp = mop.getDisplacement()
                if disp is not None:
                    disp_value = disp.getValue() if hasattr(disp, 'getValue') else disp
                    disp_bits = disp.getBitSize() if hasattr(disp, 'getBitSize') else None
                    imm_tags = classify_immediate_semantics(
                        ctx=ctx,
                        inst=inst,
                        pc=pc,
                        opc=opc,
                        operand_index=operand_index,
                        imm_obj=disp,
                        value=disp_value,
                        bit_size=disp_bits,
                        source_kind='mem_disp',
                        in_plt_site=in_plt(pc),
                        pc_hit_count_for_site=pc_hit_count.get(pc, 1),
                    )
                    obj_id, obj_type, label, imm_meta = objcanon.canon_imm_occurrence(
                        disp,
                        pc=pc,
                        operand_index=operand_index,
                        source_kind='mem_disp',
                        bit_size=disp_bits,
                        semantic_tags=imm_tags,
                    )
                    ensure_node(node_meta, obj_id, obj_type, label, **imm_meta)
                    addr_objs.add(obj_id)
                    imm_objs.add(obj_id)
            except Exception:
                pass

            try:
                scale = mop.getScale()
                if scale is not None:
                    imm_tags = classify_immediate_semantics(
                        ctx=ctx,
                        inst=inst,
                        pc=pc,
                        opc=opc,
                        operand_index=operand_index,
                        imm_obj=scale,
                        value=scale,
                        bit_size=None,
                        source_kind='mem_scale',
                        in_plt_site=in_plt(pc),
                        pc_hit_count_for_site=pc_hit_count.get(pc, 1),
                    )
                    obj_id, obj_type, label, imm_meta = objcanon.canon_imm_occurrence(
                        scale,
                        pc=pc,
                        operand_index=operand_index,
                        source_kind='mem_scale',
                        bit_size=None,
                        semantic_tags=imm_tags,
                    )
                    ensure_node(node_meta, obj_id, obj_type, label, **imm_meta)
                    addr_objs.add(obj_id)
                    imm_objs.add(obj_id)
            except Exception:
                pass

        for src in addr_objs:
            if src in last_def_obj:
                local_inst_addr_edges.add((last_def_obj[src], pc))

        # ---------- taint 观测（当前实现仍保留） ----------
        used_tainted_reg = any(ctx.isRegisterTainted(reg) for reg, _ in read_regs_info)
        used_tainted_mem = any(ctx.isMemoryTainted(mem) for mem, _ in read_mems_info)
        wrote_tainted_reg = any(ctx.isRegisterTainted(reg) for reg, _ in written_regs_info)
        wrote_tainted_mem = any(ctx.isMemoryTainted(mem) for mem, _ in written_mems_info)

        inst_uses_taint_flag = used_tainted_reg or used_tainted_mem or wrote_tainted_reg or wrote_tainted_mem

        use_tainted_regs = set()
        use_tainted_mems = set()
        def_tainted_regs = set()
        def_tainted_mems = set()

        for reg, _ in read_regs_info:
            if ctx.isRegisterTainted(reg):
                use_tainted_regs.add(get_parent_reg_name(ctx, reg))

        for mem, _ in read_mems_info:
            if ctx.isMemoryTainted(mem):
                use_tainted_mems.add(mem.getAddress())

        for reg, _ in written_regs_info:
            if ctx.isRegisterTainted(reg):
                def_tainted_regs.add(get_parent_reg_name(ctx, reg))

        for mem, _ in written_mems_info:
            if ctx.isMemoryTainted(mem):
                def_tainted_mems.add(mem.getAddress())

        regs_t = set()
        for reg in ctx.getParentRegisters():
            if ctx.isRegisterTainted(reg):
                regs_t.add(reg.getName())
                tainted_regs.add(reg.getName())

        mems_t = set()
        for opnd in inst.getOperands():
            if opnd.getType() == OPERAND.MEM and ctx.isMemoryTainted(opnd):
                addr = opnd.getAddress()
                mems_t.add(addr)
                tainted_mems.add(addr)

        

        # ==================== 修订点7 Step 7.2：运行时 seed 桥接 ====================
        # 检查当前指令涉及的所有 mem objects，如果落在 seed 地址范围内，
        # 则建立桥接边并将 seed obj_id 注入到相关集合中

        inst_touches_seed = False
        local_bridge_edges = []

        # 检查 def_objs 中的 mem objects
        bridged_from_def, edges_from_def = bridge_mem_objs_to_seed(def_objs)
        if bridged_from_def:
            inst_touches_seed = True
            local_bridge_edges.extend(edges_from_def)
            # 将 seed obj_id 也加入 def_objs（表示该指令定义了 seed 对象）
            def_objs = set(def_objs) | bridged_from_def

        # 检查 use_objs 中的 mem objects
        bridged_from_use, edges_from_use = bridge_mem_objs_to_seed(use_objs)
        if bridged_from_use:
            inst_touches_seed = True
            local_bridge_edges.extend(edges_from_use)
            use_objs = set(use_objs) | bridged_from_use

        # 检查 addr_objs 中的 mem objects
        bridged_from_addr, edges_from_addr = bridge_mem_objs_to_seed(addr_objs)
        if bridged_from_addr:
            inst_touches_seed = True
            local_bridge_edges.extend(edges_from_addr)
            addr_objs = set(addr_objs) | bridged_from_addr

        # 检查 mem_objs_local 中的 mem objects
        bridged_from_mem, edges_from_mem = bridge_mem_objs_to_seed(mem_objs_local)
        if bridged_from_mem:
            inst_touches_seed = True
            local_bridge_edges.extend(edges_from_mem)
            mem_objs_local = set(mem_objs_local) | bridged_from_mem

        # 注入桥接边到对象级依赖图
        if local_bridge_edges:
            seed_bridge_count += len(local_bridge_edges)
            for (src_oid, dst_oid, etype) in local_bridge_edges:
                # 确保两端节点都在 node_meta 中
                if src_oid not in node_meta:
                    node_meta[src_oid] = {
                        'type': 'mem' if src_oid.startswith('mem:') else 'var',
                        'tags': set(),
                    }
                if dst_oid not in node_meta:
                    node_meta[dst_oid] = {
                        'type': 'var' if dst_oid.startswith('var:') else 'mem',
                        'tags': set(),
                    }
                # seed bridge 表达对象身份对应关系，不是指令数据依赖。
                add_object_relation_meta(
                    object_relation_meta, src_oid, dst_oid, etype, pc=pc
                )
                local_object_relations.add((src_oid, dst_oid, etype))

        record_dynamic_facts = True

        # ---------- 方向4：重复依赖事实签名 ----------
        active_ctrl_branch_sig, active_ctrl_obj_sig = make_active_control_signature(active_control_context, pc)

        loop_signature = make_loop_fact_signature(
            pc=pc,
            call_depth=call_depth,
            use_objs=use_objs,
            def_objs=def_objs,
            addr_objs=addr_objs,
            imm_objs=imm_objs,
            mem_objs=mem_objs_local,
            raw_inst_data_edges=local_raw_inst_data_edges,
            canonical_inst_data_edges=local_canonical_inst_data_edges,
            inst_addr_edges=local_inst_addr_edges,
            object_relations=local_object_relations,
            active_ctrl_branch_sig=active_ctrl_branch_sig,
            active_ctrl_obj_sig=active_ctrl_obj_sig,
            use_tainted_regs=use_tainted_regs,
            use_tainted_mems=use_tainted_mems,
            def_tainted_regs=def_tainted_regs,
            def_tainted_mems=def_tainted_mems,
            regs_t=regs_t,
            mems_t=mems_t,
            touches_seed=inst_touches_seed,  # ★ 修订点9：加入 seed 标记
        )

        # ==================== 修订点8：seed-touching 指令永不熔断 ====================
        # 原始逻辑：当 loop pattern 重复超过阈值时，设置 record_dynamic_facts = False
        # 修订：如果当前指令触及 seed 地址范围，则强制保持 record_dynamic_facts = True

        # 替换原有的熔断判定逻辑
        if LOOP_SUMMARIZATION_ENABLED:
            allow_new_pattern = (loop_signature in loop_pattern_stats) or (len(loop_pattern_stats) < LOOP_SUMMARIZATION_MAX_PATTERNS)
            entry, is_new_pattern = update_loop_pattern_stats(
                loop_pattern_stats=loop_pattern_stats,
                signature=loop_signature,
                pc=pc,
                call_depth=call_depth,
                disasm=disasm,
                use_objs=use_objs,
                def_objs=def_objs,
                addr_objs=addr_objs,
                imm_objs=imm_objs,
                active_ctrl_branch_sig=active_ctrl_branch_sig,
                active_ctrl_obj_sig=active_ctrl_obj_sig,
                inst_uses_taint_flag=inst_uses_taint_flag,
                allow_new_pattern=allow_new_pattern,
            )
            if is_new_pattern:
                loop_unique_patterns += 1
            elif entry is None and not allow_new_pattern:
                loop_new_pattern_disabled += 1
            elif entry is not None and entry['count'] > LOOP_SUMMARIZATION_SUPPRESS_AFTER:
                # ★ 修订点8核心：触及 seed 的指令永不熔断
                if inst_touches_seed:
                    # 即使超过阈值，只要涉及 seed 地址范围，强制保持记录
                    record_dynamic_facts = True
                    seed_touch_no_suppress_count += 1
                else:
                    record_dynamic_facts = False
                    loop_suppressed_records += 1
                    inst_repeat_suppressed[pc] += 1
        else:
            record_dynamic_facts = True

        # ---------- 持久化记录（仅对首次 / 非重复签名写入） ----------
        if record_dynamic_facts:
            # 原始 DFG（仅最近定义）
            for src, dst in local_raw_inst_data_edges:
                dfg_edges.add((src, dst))
                add_inst_edge_meta(inst_edge_meta, src, dst, 'data', pc)
            
            for imm_oid in imm_objs:
                inst_immediates[pc].add(imm_oid)
                imm_inst_edge_count += 1

            # 记录对象级 use/def/addr/immediate / mem facts
            inst_use_objects[pc].update(use_objs)
            inst_def_objects[pc].update(def_objs)
            inst_addr_objects[pc].update(addr_objs)
            inst_immediates[pc].update(imm_objs)
            inst_mem_objects[pc].update(mem_objs_local)

            # 在线控制依赖应用（替代后处理）
            apply_online_control_to_inst(
                pc,
                def_objs,
                active_control_context,
                call_depth,
                inst_controlled_by,
                inst_ctrl_objects,
                inst_edge_meta,
                obj_ctrl_use_pcs,
                inst_control_evidence,
            )

            # 指令级地址依赖（方向3：直接基于 canonical obj_id）
            for src, dst in local_inst_addr_edges:
                add_inst_edge_meta(inst_edge_meta, src, dst, 'addr', pc)

            # 指令级数据依赖（对象级最近定义）
            for src, dst in local_canonical_inst_data_edges:
                add_inst_edge_meta(inst_edge_meta, src, dst, 'data', pc)

            inst_taint_io[pc] = {
                'use_regs': set(use_tainted_regs),
                'use_mems': set(use_tainted_mems),
                'def_regs': set(def_tainted_regs),
                'def_mems': set(def_tainted_mems),
            }

            if regs_t or mems_t:
                node_taint[pc] = {'regs': set(regs_t), 'mems': set(mems_t)}
        else:
            # 即使本次重复事件不再重复写入细粒度事实，也仍维持“该 pc 是否用过 taint”的并集语义。
            prev_flag = inst_uses_taint.get(pc, False)
            inst_uses_taint[pc] = prev_flag or inst_uses_taint_flag

            prev_io = inst_taint_io.get(pc)
            if prev_io is not None:
                prev_io['use_regs'].update(use_tainted_regs)
                prev_io['use_mems'].update(use_tainted_mems)
                prev_io['def_regs'].update(def_tainted_regs)
                prev_io['def_mems'].update(def_tainted_mems)
            else:
                inst_taint_io[pc] = {
                    'use_regs': set(use_tainted_regs),
                    'use_mems': set(use_tainted_mems),
                    'def_regs': set(def_tainted_regs),
                    'def_mems': set(def_tainted_mems),
                }

            if regs_t or mems_t:
                prev_nt = node_taint.get(pc)
                if prev_nt is None:
                    node_taint[pc] = {'regs': set(regs_t), 'mems': set(mems_t)}
                else:
                    prev_nt['regs'].update(regs_t)
                    prev_nt['mems'].update(mems_t)

        inst_uses_taint[pc] = inst_uses_taint.get(pc, False) or inst_uses_taint_flag

        # ---------- 更新当前定义（对象级 / 原始寄存器-内存级） ----------
        for reg in written_regs:
            last_def_reg[reg.getName()] = pc
            obj_id, _, _, _ = objcanon.canon_reg(reg)
            last_def_obj[obj_id] = pc

        for mem in written_mems:
            last_def_mem[mem.getAddress()] = pc
            obj_id, _, _, _ = objcanon.canon_memory_access(
                mem.getAddress(), mem.getSize(), mem=mem
            )
            last_def_obj[obj_id] = pc

        # immediate 没有定义者，不更新 last_def_obj

        # ---------- 回边统计 ----------
        if opc.startswith('j') and next_pc < pc and in_loaded_code(next_pc):
            back_edge_taken[(pc, next_pc)] += 1

            # 方案C：回边截断安全网
            be_count = back_edge_taken[(pc, next_pc)]
            if be_count > BACK_EDGE_LIMIT:
                fallthrough = pc + inst.getSize()
                if in_loaded_code(fallthrough):
                    # 首次截断时打印警告
                    if be_count == BACK_EDGE_LIMIT + 1:
                        print(f'[loop-cut] back edge {hex_pc(pc)}->{hex_pc(next_pc)} '
                              f'exceeded {BACK_EDGE_LIMIT} iterations, '
                              f'forcing exit to {hex_pc(fallthrough)}')

                    ctx.setConcreteRegisterValue(ctx.registers.rip, fallthrough)
                    next_pc = fallthrough
                    # 更新 cfg_edges 以反映强制跳转
                    cfg_edges.add((pc, fallthrough))
                    # 注意：不 continue，让后续的依赖记录逻辑正常处理该条指令

        # ---------- 条件分支条件对象记录 + 在线压栈 ----------
        branch_cond_objs = set()
        branch_target = None
        branch_fallthrough = pc + inst.getSize()

        if opc.startswith('j') and opc != 'jmp':
            branch_cond_objs = set(use_objs | addr_objs)

            if record_dynamic_facts:
                inst_ctrl_objects[pc].update(branch_cond_objs)

            for oid in branch_cond_objs:
                if oid.startswith('reg:'):
                    add_node_tags(node_meta, oid, 'controlling_operand')
                if oid.startswith('imm_occurrence:'):
                    add_node_tags(node_meta, oid, 'comparison_constant')

            add_inst_tags(inst_semantic_tags, pc, 'conditional_branch')

            try:
                if inst.getOperands():
                    op0 = inst.getOperands()[0]
                    if op0.getType() == OPERAND.IMM:
                        branch_target = op0.getValue()
                    elif op0.getType() == OPERAND.MEM:
                        branch_target = op0.getAddress()
            except Exception:
                branch_target = None

            alt_pc = None
            if branch_target is not None:
                alt_pc = branch_fallthrough if next_pc == branch_target else branch_target
            else:
                alt_pc = branch_fallthrough if next_pc != branch_fallthrough else None

            if CONTROL_EXPANSION_MODE != 'none':
                new_control_context = make_hybrid_control_context(
                    static_control_model=static_control_model,
                    branch_pc=pc,
                    cond_objs=branch_cond_objs,
                    call_depth=call_depth,
                    taken_next=next_pc,
                    fallthrough=branch_fallthrough,
                    alt_pc=alt_pc,
                )
                ctx_key = new_control_context['key']

                if ctx_key not in active_control_keys:
                    active_control_context.append(new_control_context)
                    active_control_keys.add(ctx_key)

                    if new_control_context['evidence'] == 'static_postdom_dynamic_edge':
                        static_control_context_pushes += 1
                    else:
                        fallback_control_context_pushes += 1

                    if len(active_control_context) > max_active_ctrl_len:
                        max_active_ctrl_len = len(active_control_context)

                    if DEBUG_CTRL_VERBOSE:
                        cond_preview = sorted(list(branch_cond_objs))[:4]
                        print(
                            f'[dbg] ctrl-push: branch_pc={hex_pc(pc)} '
                            f'taken_next={hex_pc(next_pc)} '
                            f'alt_pc={hex_pc(alt_pc) if alt_pc is not None else None} '
                            f'merge_pc={hex_pc(new_control_context.get("merge_pc")) if new_control_context.get("merge_pc") is not None else None} '
                            f'evidence={new_control_context["evidence"]} '
                            f'call_depth={call_depth} '
                            f'active_ctrl={len(active_control_context)} '
                            f'cond_objs={cond_preview}'
                        )

                    if len(active_control_context) >= DEBUG_CTRL_WARN_THRESHOLD:
                        print(
                            f'[warn] active_control_context unusually large: '
                            f'len={len(active_control_context)} '
                            f'branch_pc={hex_pc(pc)} '
                            f'call_depth={call_depth} '
                            f'disasm={disasm}'
                        )
                else:
                    for i in range(len(active_control_context) - 1, -1, -1):
                        if active_control_context[i].get('key') == ctx_key:
                            active_control_context[i]['cond_objs'].update(branch_cond_objs)
                            break

        # ---------- call 处理 ----------
        if opc == 'call':
            # === 方案2修订点4：caller-saved 注入辅助 ===
            def _inject_caller_saved_defs(at_pc):
                nonlocal caller_saved_inject_count
                cs_oids = get_caller_saved_canonical_oids(ctx, objcanon)
                for cs_oid in cs_oids:
                    last_def_obj[cs_oid] = at_pc
                    caller_saved_inject_count += 1
                if record_dynamic_facts:
                    inst_def_objects[at_pc].update(cs_oids)
                add_inst_tags(inst_semantic_tags, at_pc, 'call_caller_saved_clobber')

            ret_next = pc + inst.getSize()
            target = inst.getOperands()[0] if inst.getOperands() else None
            target_addr = None
            got_entry = None

            if target is not None:
                if target.getType() == OPERAND.IMM:
                    target_addr = target.getValue()
                elif target.getType() == OPERAND.MEM:
                    got_entry = target.getAddress()
                    try:
                        target_addr = read_mem_int(ctx, got_entry, target.getSize())
                    except Exception:
                        target_addr = None
                else:
                    try:
                        target_addr = ctx.getConcreteRegisterValue(target)
                    except Exception:
                        target_addr = None

            target_name = None

            if got_entry and got_entry in got_map:
                target_name = got_map[got_entry]

                if target_name == '__libc_start_main':
                    if not entered_main:
                        entered_main = True
                        if main_addr is None:
                            raise RuntimeError('Cannot resolve main address for __libc_start_main hook')
                        if exit_addr is None:
                            raise RuntimeError('exit_addr is None')

                        # glibc 的 _start 调用 __libc_start_main 时，SysV AMD64
                        # 参数 2/3 分别位于 RSI/RDX，即 argc/argv。该 hook 跳过
                        # libc 并直接进入 main，因此必须显式改写为
                        # main(argc, argv, envp) 的 RDI/RSI/RDX 调用约定。
                        libc_argc = int(ctx.getConcreteRegisterValue(ctx.registers.rsi))
                        libc_argv = int(ctx.getConcreteRegisterValue(ctx.registers.rdx))
                        try:
                            main_argc, main_argv, main_envp = derive_main_process_args(
                                libc_argc, libc_argv, STACK_ADDR, STACK_SIZE
                            )
                        except (TypeError, ValueError) as exc:
                            raise RuntimeError(
                                f'Invalid __libc_start_main process arguments: {exc}'
                            ) from exc

                        call_stack.append(exit_addr)
                        call_depth += 1
                        cfg_edges.add((pc, main_addr))
                        ctx.setConcreteRegisterValue(ctx.registers.rdi, main_argc)
                        ctx.setConcreteRegisterValue(ctx.registers.rsi, main_argv)
                        ctx.setConcreteRegisterValue(ctx.registers.rdx, main_envp)
                        ctx.setConcreteRegisterValue(ctx.registers.rip, main_addr)
                        # 注意：这里是进入 main，不是 callee 返回，不需要 caller_saved 注入
                        continue
                    done = True
                    break

                if target_name in hooks:
                    hooks[target_name](ctx)
                    _inject_caller_saved_defs(pc)   # === 修订点4 ===
                    cfg_edges.add((pc, ret_next))
                    ctx.setConcreteRegisterValue(ctx.registers.rip, ret_next)
                    continue

            if target_addr is not None and target_name is None:
                symname = symbol_addr_map.get(target_addr)
                if symname and symname in hooks:
                    hooks[symname](ctx)
                    _inject_caller_saved_defs(pc)   # === 修订点4 ===
                    cfg_edges.add((pc, ret_next))
                    ctx.setConcreteRegisterValue(ctx.registers.rip, ret_next)
                    continue

            if target_addr is not None and in_plt(target_addr):
                _inject_caller_saved_defs(pc)       # === 修订点4 ===
                cfg_edges.add((pc, ret_next))
                ctx.setConcreteRegisterValue(ctx.registers.rip, ret_next)
                continue

            if target_addr is not None and in_loaded_code(target_addr):
                # 真正调用到加载代码中：不注入 caller_saved（callee 返回后由 ret 处理）
                # 注意：理论上 callee 内部会修改 caller_saved regs，
                # 但因为我们会沿着 callee 真实执行轨迹追踪，那些 def 会被自然记录
                # 所以这里不需要预先注入
                call_stack.append(ret_next)
                call_depth += 1
                cfg_edges.add((pc, target_addr))
                ctx.setConcreteRegisterValue(ctx.registers.rip, target_addr)
                continue

            # fallback：未知 call target，保守注入 caller_saved
            _inject_caller_saved_defs(pc)           # === 修订点4 ===
            cfg_edges.add((pc, ret_next))
            ctx.setConcreteRegisterValue(ctx.registers.rip, ret_next)
            continue

        # ---------- ret 处理 ----------
        if opc == 'ret':
            if call_stack:
                ret_addr = call_stack.pop()
                call_depth = max(call_depth - 1, 0)
                if not in_loaded_code(ret_addr):
                    done = True
                    break
                cfg_edges.add((pc, ret_addr))
                ctx.setConcreteRegisterValue(ctx.registers.rip, ret_addr)
                continue
            done = True
            break

        # ---------- 正常结束 ----------
        if opc == 'hlt':
            done = True
            break

    # -------------------- 正向/反向依赖分析 --------------------
    executed_pcs = set(pc_hit_count.keys())

    inst_succ = defaultdict(set)
    inst_pred = defaultdict(set)
    for (src, dst), _meta in inst_edge_meta.items():
        inst_succ[src].add(dst)
        inst_pred[dst].add(src)

    # 污点源对象节点：固定从变量级 seed 出发
    obj_seed_nodes = {seed_obj_id}
    for oid in node_meta.keys():
        if oid == seed_obj_id:
            obj_seed_nodes.add(oid)
    
    # ==================== 修订点7 后处理：合并桥接边到 slice 输入 ====================
    # 将 object_relation_meta 中的 seed 身份关系映射到 slice 的 use/def 事实。
    # 关系边本身保持在独立表中，绝不写入指令依赖图或对象因果图。
    # 使得 build_seed_object_slice 能够发现 seed 与运行时 mem objects 的连接

    # 方法：确保每条桥接边的两端节点在 node_meta 中存在
    for (src_oid, dst_oid), edge_info in object_relation_meta.items():
        if src_oid not in node_meta:
            node_meta[src_oid] = {'type': 'bridge', 'tags': set()}
        if dst_oid not in node_meta:
            node_meta[dst_oid] = {'type': 'bridge', 'tags': set()}
        # 将桥接边涉及的 PC 注入到 inst_def_objects 和 inst_use_objects
        for bridge_pc in edge_info['pcs']:
            if bridge_pc is None:
                continue
            if isinstance(bridge_pc, str):
                try:
                    bridge_pc = int(bridge_pc, 16) if bridge_pc.startswith('0x') else int(bridge_pc)
                except (ValueError, TypeError):
                    continue
            if src_oid in obj_seed_nodes or dst_oid in obj_seed_nodes:
                # seed 端作为 def 或 use
                if dst_oid in obj_seed_nodes:
                    # src -> seed: src 定义了 seed（例如 STORE 到 array2）
                    inst_def_objects[bridge_pc].add(dst_oid)
                    inst_use_objects[bridge_pc].add(src_oid)
                if src_oid in obj_seed_nodes:
                    # seed -> dst: 从 seed LOAD（例如 LOAD from array2）
                    inst_use_objects[bridge_pc].add(src_oid)
                    inst_def_objects[bridge_pc].add(dst_oid)

    print(f'[plan2-fix7] total object relations in object_relation_meta: '
          f'{len(object_relation_meta)}')
    print(f'[plan2-fix7] node_meta size after bridging: {len(node_meta)}')

    # 方向2：只围绕 seed 构造对象 slice
    slice_result = build_seed_object_slice(
        obj_seed_nodes=obj_seed_nodes,
        executed_pcs=executed_pcs,
        node_meta=node_meta,
        inst_use_objects=inst_use_objects,
        inst_def_objects=inst_def_objects,
        inst_addr_objects=inst_addr_objects,
        inst_mem_objects=inst_mem_objects,
        inst_controlled_by=inst_controlled_by,
        inst_ctrl_objects=inst_ctrl_objects,
        control_expansion_mode=CONTROL_EXPANSION_MODE,
    )

    # === 方案2修订点6：弱连通节点恢复 ===
    # 在 slice 完成后，扫描 backward_reachable 中悬空的节点
    # （入度为0但不是 seed），通过 inst_def_objects 反查它们的真实定义来源
    # 恢复被 hotspot 熔断的依赖链
    recovery_stats = recover_weakly_connected_nodes(
        slice_result=slice_result,
        obj_seed_nodes=obj_seed_nodes,
        executed_pcs=executed_pcs,
        inst_use_objects=inst_use_objects,
        inst_def_objects=inst_def_objects,
        inst_addr_objects=inst_addr_objects,
        inst_mem_objects=inst_mem_objects,
        inst_controlled_by=inst_controlled_by,
        inst_ctrl_objects=inst_ctrl_objects,
        node_meta=node_meta,
        control_expansion_mode=CONTROL_EXPANSION_MODE,
        max_recovery_hops=2,
        max_recovery_nodes=128,
    )

    print(
        f'[recovery] orphans={recovery_stats["orphan_count"]} '
        f'recovered_nodes={recovery_stats["recovered_nodes"]} '
        f'recovered_edges={recovery_stats["recovered_edges"]}'
    )

    # slice_result 已被 in-place 修改，下面的解构会拿到补全后的版本

    object_edge_meta = slice_result['object_edge_meta']
    sliced_node_meta = slice_result['sliced_node_meta']
    forward_obj_reachable = slice_result['forward_obj_reachable']
    backward_obj_reachable = slice_result['backward_obj_reachable']
    obj_def_pcs = slice_result['obj_def_pcs']
    obj_use_pcs = slice_result['obj_use_pcs']
    obj_addr_use_pcs = slice_result['obj_addr_use_pcs']
    obj_ctrl_use_pcs = slice_result['obj_ctrl_use_pcs']

    # 三张图在任何遍历和导出前必须满足端点类型不变量。
    validate_edge_table_types(
        inst_edge_meta=inst_edge_meta,
        object_edge_meta=object_edge_meta,
        object_relation_meta=object_relation_meta,
    )

    obj_succ, obj_pred = build_adj_from_edge_meta(object_edge_meta)
    obj_leaf_nodes = compute_leaf_nodes(backward_obj_reachable, obj_pred)
    forward_obj_sinks = compute_sink_nodes(forward_obj_reachable, obj_succ)

    # 种子指令：use/def/addr 触达 seed 对象的指令
    inst_seed_pcs = set()
    for pc in executed_pcs:
        if obj_seed_nodes & inst_use_objects.get(pc, set()):
            inst_seed_pcs.add(pc)
        if obj_seed_nodes & inst_def_objects.get(pc, set()):
            inst_seed_pcs.add(pc)
        if obj_seed_nodes & inst_addr_objects.get(pc, set()):
            inst_seed_pcs.add(pc)

    # 指令正反向（保持原语义）
    forward_inst_reachable = traverse_graph(inst_seed_pcs, succ=inst_succ, pred=inst_pred, reverse=False)
    backward_inst_reachable = traverse_graph(inst_seed_pcs, succ=inst_succ, pred=inst_pred, reverse=True)
    inst_leaf_pcs = compute_leaf_nodes(backward_inst_reachable, inst_pred)

    # 方向2：指令级导出也只保留 seed slice
    slice_inst_pcs = set(inst_seed_pcs) | set(forward_inst_reachable) | set(backward_inst_reachable)

    # 方向5：基于视图进一步裁剪 DOT 导出节点
    selected_object_dot_nodes = select_object_view_nodes(
        view_mode=mode_opts['object_dot_view'],
        obj_seed_nodes=obj_seed_nodes,
        backward_obj_reachable=backward_obj_reachable,
        forward_obj_reachable=forward_obj_reachable,
        obj_succ=obj_succ,
        obj_pred=obj_pred,
        neighborhood_hops=mode_opts['dot_neighborhood_hops'],
    )
    selected_object_dot_nodes |= set(obj_seed_nodes)

    selected_inst_dot_pcs = select_inst_view_nodes(
        view_mode=mode_opts['inst_dot_view'],
        inst_seed_pcs=inst_seed_pcs,
        backward_inst_reachable=backward_inst_reachable,
        forward_inst_reachable=forward_inst_reachable,
        inst_succ=inst_succ,
        inst_pred=inst_pred,
        neighborhood_hops=mode_opts['dot_neighborhood_hops'],
    )
    selected_inst_dot_pcs |= set(inst_seed_pcs)

    filtered_object_edge_meta = filter_edge_meta_by_nodes(object_edge_meta, selected_object_dot_nodes)
    filtered_inst_edge_meta = filter_edge_meta_by_nodes(inst_edge_meta, selected_inst_dot_pcs)
    filtered_cfg_edges_for_cdfg = filter_plain_edges_by_nodes(cfg_edges, selected_inst_dot_pcs)

    filtered_object_node_meta = {
        oid: sliced_node_meta.get(oid, node_meta.get(oid))
        for oid in selected_object_dot_nodes
        if sliced_node_meta.get(oid, node_meta.get(oid)) is not None
    }

    filtered_backward_obj_reachable = set(backward_obj_reachable) & set(selected_object_dot_nodes)
    filtered_forward_obj_reachable = set(forward_obj_reachable) & set(selected_object_dot_nodes)
    filtered_obj_leaf_nodes = compute_leaf_nodes(filtered_backward_obj_reachable, build_adj_from_edge_meta(filtered_object_edge_meta)[1])
    filtered_forward_obj_sinks = compute_sink_nodes(filtered_forward_obj_reachable, build_adj_from_edge_meta(filtered_object_edge_meta)[0])

    filtered_backward_inst_reachable = set(backward_inst_reachable) & set(selected_inst_dot_pcs)
    filtered_forward_inst_reachable = set(forward_inst_reachable) & set(selected_inst_dot_pcs)

    # 方向6：代表性路径报告
    path_report = None
    if mode_opts['export_path_report']:
        path_report = build_object_path_report(
            obj_seed_nodes=obj_seed_nodes,
            backward_obj_reachable=backward_obj_reachable,
            forward_obj_reachable=forward_obj_reachable,
            object_edge_meta=object_edge_meta,
            node_meta=sliced_node_meta,
            obj_leaf_nodes=obj_leaf_nodes,
            forward_obj_sinks=forward_obj_sinks,
            max_depth=mode_opts['path_report_max_depth'],
            per_target=mode_opts['path_report_per_target'],
            top_targets=mode_opts['path_report_top_targets'],
            edge_pcs_limit=PATH_REPORT_EDGE_PCS_LIMIT,
        )

    # -------------------- 输出汇总 --------------------
    elapsed_total = time.time() - debug_start_ts
    print(f'[dbg] elapsed_total={elapsed_total:.2f}s')
    print(f'[dbg] max_call_depth_seen={max_call_depth_seen}')
    print(f'[dbg] max_active_control_context={max_active_ctrl_len}')
    debug_print_hotspots(pc_hit_count, inst_info, DEBUG_HOTSPOT_TOPN)
    if LOOP_SUMMARIZATION_ENABLED and loop_pattern_stats:
        debug_print_loop_patterns(loop_pattern_stats, LOOP_SUMMARIZATION_TOPN)
    print(f'[+] Executed {inst_count} instructions.')
    print('[+] Tainted registers:', sorted(tainted_regs))
    print('[+] Tainted memory addresses:', [f'0x{x:x}' for x in sorted(tainted_mems)])
    print(f'[+] Object seeds: {sorted(obj_seed_nodes)}')
    print(f'[+] Seed instructions: {[hex(x) for x in sorted(inst_seed_pcs)]}')
    print(f'[+] Backward object reachable: {len(backward_obj_reachable)} nodes')
    print(f'[+] Forward object reachable: {len(forward_obj_reachable)} nodes')
    print(f'[+] Backward instruction reachable: {len(backward_inst_reachable)} pcs')
    print(f'[+] Forward instruction reachable: {len(forward_inst_reachable)} pcs')
    print(f'[+] Object DOT nodes after view filter: {len(selected_object_dot_nodes)}')
    print(f'[+] Inst DOT nodes after view filter: {len(selected_inst_dot_pcs)}')
    if LOOP_SUMMARIZATION_ENABLED:
        print(f'[+] Loop summarization unique patterns: {loop_unique_patterns}')
        print(f'[+] Loop summarization suppressed repeated records: {loop_suppressed_records}')
        if loop_new_pattern_disabled:
            print(f'[warn] Loop summarization pattern cap reached; new patterns recorded normally: {loop_new_pattern_disabled}')
    
        # === 方案2修订：统计输出 ===
    print(
        f'[plan2-stats] '
        f'zero_idiom_suppressed={zero_idiom_count} '
        f'partial_rmw_lifted={partial_rmw_count} '
        f'mem_alias_extensions={mem_alias_extension_count} '
        f'caller_saved_injects={caller_saved_inject_count} '
        f'imm_inst_edges={imm_inst_edge_count}'
    )

    # ==================== 修订点10：暴露新增调试指标 ====================
    print(
        f'[plan2-fix-stats] '
        f'seed_bridge_edges_injected={seed_bridge_count} '
        f'seed_touch_no_suppress={seed_touch_no_suppress_count} '
        f'seed_address_ranges={len(seed_address_ranges)}'
    )

    exported_files = {}

    # 类型错误必须在写入时或上面的统一验证中失败；禁止导出前静默过滤。
    print(
        f'[type-check] inst_edges={len(inst_edge_meta)} int-int; '
        f'object_edges={len(object_edge_meta)} str-str; '
        f'object_relations={len(object_relation_meta)} str-str'
    )

    # 创建纯整数版本的 CFG 边
    cfg_edges = {
        (src, dst) for (src, dst) in cfg_edges
        if isinstance(src, int) and isinstance(dst, int)
    }

    # 清洗所有 PC 集合
    executed_pcs = _safe_int_set(executed_pcs)

    exported_files = {}

    # -------------------- DOT 导出 --------------------
    if mode_opts['export_cfg']:
        out = prefixed_name(output_prefix, 'cfg.dot')
        export_cfg_dot(
            out,
            executed_pcs, cfg_edges, addr2line_map,
            node_taint, inst_taint_io, inst_uses_taint, inst_info,
        )
        exported_files['cfg'] = out

    if mode_opts['export_cfg_bb']:
        out = prefixed_name(output_prefix, 'cfg_bb.dot')
        export_cfg_bb_dot(
            out,
            executed_pcs, cfg_edges, addr2line_map,
            inst_info, node_taint, inst_taint_io, inst_uses_taint,
        )
        exported_files['cfg_bb'] = out

    if mode_opts['export_inst_dep']:
        out = prefixed_name(output_prefix, 'dfg.dot')
        # ---- 诊断：检测 inst_edge_meta 中的类型污染 ----
        _bad_edges = [(k, type(k[0]), type(k[1])) for k in inst_edge_meta.keys()
                    if not (isinstance(k[0], int) and isinstance(k[1], int))]
        if _bad_edges:
            print(f'[BUG] inst_edge_meta has {len(_bad_edges)} non-int keys!')
            for k, t0, t1 in _bad_edges[:5]:
                print(f'  key={k}, types=({t0.__name__}, {t1.__name__})')
        export_inst_dep_dot(
            out,
            selected_inst_dot_pcs, filtered_inst_edge_meta, addr2line_map, inst_info,
            node_taint, inst_uses_taint,
            filtered_backward_inst_reachable, filtered_forward_inst_reachable, inst_seed_pcs,
        )
        exported_files['inst_dep'] = out

    if mode_opts['export_object_dep']:
        out = prefixed_name(output_prefix, 'object_dep.dot')
        export_object_dep_dot(
            out,
            filtered_object_node_meta, filtered_object_edge_meta,
            filtered_backward_obj_reachable, filtered_forward_obj_reachable,
            obj_seed_nodes, filtered_obj_leaf_nodes, filtered_forward_obj_sinks,
        )
        exported_files['object_dep'] = out

    if mode_opts['export_cdfg']:
        out = prefixed_name(output_prefix, 'cdfg.dot')
        export_cdfg_dot(
            out,
            selected_inst_dot_pcs, filtered_cfg_edges_for_cdfg, filtered_inst_edge_meta,
            addr2line_map, inst_info, _safe_int_set(inst_seed_pcs),
        )
        exported_files['cdfg'] = out

    if path_report is not None:
        txt_path = prefixed_name(output_prefix, 'path_report.txt')
        json_path = prefixed_name(output_prefix, 'path_report.json')
        export_object_path_report_txt(txt_path, path_report)
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(path_report, f, ensure_ascii=False, indent=2)
        exported_files['path_report_txt'] = txt_path
        exported_files['path_report_json'] = json_path

    top_loop_patterns = []
    if LOOP_SUMMARIZATION_ENABLED and loop_pattern_stats:
        top_items = sorted(loop_pattern_stats.values(), key=lambda x: x['count'], reverse=True)[:LOOP_SUMMARIZATION_TOPN]
        for item in top_items:
            top_loop_patterns.append({
                'pc': hex(item['pc']),
                'call_depth': item['call_depth'],
                'disasm': item['disasm'],
                'count': item['count'],
                'suppressed_records': item['suppressed_records'],
                'use_objects': list(item['use_objects']),
                'def_objects': list(item['def_objects']),
                'addr_objects': list(item['addr_objects']),
                'immediates': list(item['immediates']),
                'active_control_branch_pcs': [hex(x) for x in item['active_control_branch_pcs']],
                'active_control_objects': list(item['active_control_objects']),
                'uses_taint': item['uses_taint'],
            })

    succ, pred, direct_parents, direct_children, edge_details = build_direct_neighbors(object_edge_meta)

    summary_scope = mode_opts['summary_scope']
    instruction_details = build_instruction_details(
        executed_pcs=executed_pcs,
        inst_info=inst_info,
        inst_use_objects=inst_use_objects,
        inst_def_objects=inst_def_objects,
        inst_addr_objects=inst_addr_objects,
        inst_immediates=inst_immediates,
        inst_controlled_by=inst_controlled_by,
        inst_uses_taint=inst_uses_taint,
        inst_repeat_suppressed=inst_repeat_suppressed,
        inst_semantic_tags=inst_semantic_tags,
        inst_control_evidence=inst_control_evidence,
        scope=summary_scope,
        slice_inst_pcs=slice_inst_pcs,
        inst_seed_pcs=inst_seed_pcs,
    )

    object_details = build_object_details(
        node_meta=node_meta,
        obj_def_pcs=obj_def_pcs,
        obj_use_pcs=obj_use_pcs,
        obj_addr_use_pcs=obj_addr_use_pcs,
        obj_ctrl_use_pcs=obj_ctrl_use_pcs,
        direct_parents=direct_parents,
        direct_children=direct_children,
        edge_details=edge_details,
        scope=summary_scope,
        sliced_node_meta=sliced_node_meta,
        obj_seed_nodes=obj_seed_nodes,
    )

    # -------------------- JSON 摘要 --------------------
    summary = {
        'taint_source': {
            'symbol': taint_symbol_name,
            'address': taint_source_addr,
            'size': taint_source_size,
            'seed_object_nodes': sorted(obj_seed_nodes),
            'seed_instruction_pcs': [hex(x) for x in sorted(inst_seed_pcs)],
        },
        'stats': {
            'executed_instructions': inst_count,
            'executed_unique_pcs': len(executed_pcs),
            'cfg_edges': len(cfg_edges),
            'inst_dependency_edges': len(inst_edge_meta),
            'object_dependency_edges': len(object_edge_meta),
            'object_relation_edges': len(object_relation_meta),
            'backward_object_nodes': len(backward_obj_reachable),
            'forward_object_nodes': len(forward_obj_reachable),
            'backward_instruction_nodes': len(backward_inst_reachable),
            'forward_instruction_nodes': len(forward_inst_reachable),
            'control_expansion_mode': CONTROL_EXPANSION_MODE,
            'static_postdom_functions_seen': static_ctrl_stats.get('functions_seen', 0),
            'static_postdom_functions_modeled': static_ctrl_stats.get('functions_modeled', 0),
            'static_postdom_branches_modeled': static_ctrl_stats.get('branches_modeled', 0),
            'static_postdom_fallback_functions': static_ctrl_stats.get('functions_fallback', 0),
            'static_control_context_pushes': static_control_context_pushes,
            'fallback_control_context_pushes': fallback_control_context_pushes,
            'postprocess_mode': mode_opts['mode'],
            'summary_scope': summary_scope,
            'max_instructions': max_instructions,
            'elapsed_seconds': elapsed_total,
            'seed_bridge_edges_injected': seed_bridge_count,
            'seed_touch_no_suppress': seed_touch_no_suppress_count,
            'seed_address_ranges_count': len(seed_address_ranges),
        },
        'export_policy': {
            'path_report_enabled': mode_opts['export_path_report'],
            'object_dot_view': mode_opts['object_dot_view'],
            'inst_dot_view': mode_opts['inst_dot_view'],
            'dot_neighborhood_hops': mode_opts['dot_neighborhood_hops'],
            'selected_object_dot_nodes': sorted(selected_object_dot_nodes),
            'selected_inst_dot_pcs': [hex(x) for x in sorted(selected_inst_dot_pcs)],
        },
        'tainted_registers': sorted(tainted_regs),
        'tainted_memory_addresses': [hex(x) for x in sorted(tainted_mems)],
        'backward': {
            'objects': sorted(backward_obj_reachable),
            'leaf_objects': sorted(obj_leaf_nodes),
            'instructions': [hex(x) for x in sorted(backward_inst_reachable)],
            'leaf_instructions': [hex(x) for x in sorted(inst_leaf_pcs)],
        },
        'forward': {
            'objects': sorted(forward_obj_reachable),
            'sink_objects': sorted(forward_obj_sinks),
            'instructions': [hex(x) for x in sorted(forward_inst_reachable)],
        },
        'instruction_details': instruction_details,
        'object_details': object_details,
        'object_relations': build_object_relation_details(object_relation_meta),
        'loop_summarization': {
            'enabled': LOOP_SUMMARIZATION_ENABLED,
            'suppress_after': LOOP_SUMMARIZATION_SUPPRESS_AFTER,
            'max_patterns': LOOP_SUMMARIZATION_MAX_PATTERNS,
            'include_control_signature': LOOP_SUMMARIZATION_INCLUDE_CONTROL,
            'unique_patterns': loop_unique_patterns,
            'suppressed_repeated_records': loop_suppressed_records,
            'new_pattern_disabled_count': loop_new_pattern_disabled,
            'top_patterns': top_loop_patterns,
        },
        'path_report_overview': {
            'enabled': path_report is not None,
            'max_depth': mode_opts['path_report_max_depth'],
            'per_target': mode_opts['path_report_per_target'],
            'top_targets': mode_opts['path_report_top_targets'],
            'backward_target_count': len(path_report.get('backward_paths', [])) if path_report else 0,
            'forward_target_count': len(path_report.get('forward_paths', [])) if path_report else 0,
        },
        'hybrid_control_dependence': {
            'model': 'static-postdom-plus-dynamic-taken-edge',
            'fallback': 'dynamic-alt-successor-approximation',
            'static_model_stats': dict(sorted(static_ctrl_stats.items())),
            'static_context_pushes': static_control_context_pushes,
            'fallback_context_pushes': fallback_control_context_pushes,
            'evidence_labels': [
                'static_postdom_dynamic_edge',
                'dynamic_alt_fallback',
            ],
        },
        'files': exported_files,
    }

    if mode_opts['export_summary_json']:
        summary_path = prefixed_name(output_prefix, 'dependency_summary.json')
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, ensure_ascii=False, indent=2)
        exported_files['summary'] = summary_path

    print('[+] Exported files:')
    for k, v in exported_files.items():
        print(f'    - {k}: {v}')
    print('[+] Done.')


if __name__ == '__main__':
    main()
