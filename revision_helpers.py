# revision_helpers.py
# 方案2修订：自适应 hotspot 熔断的辅助函数集
# 所有函数无副作用（除非显式说明），可独立测试

from collections import defaultdict, deque


# ==============================================================================
# 修订点1：自归零惯用法检测
# ==============================================================================

# 这些 opcode 在 src == dst 时是"无依赖归零"惯用法
# 注意：所有这些 opcode 都不在 MOVE_LIKE_OPCODES 里，所以与 is_pure_register_move 不冲突
ZERO_IDIOM_OPCODES = {
    # 整数归零
    'xor', 'sub',
    # SSE/AVX 浮点/向量归零
    'pxor', 'xorps', 'xorpd', 'vpxor', 'vxorps', 'vxorpd',
    # AVX-512
    'kxorw', 'kxorb', 'kxord', 'kxorq',
}


def is_self_zero_idiom(opc, read_regs_info, written_regs_info,
                      read_mems_info, written_mems_info, has_immediates,
                      get_parent_reg_name_fn, ctx):
    """
    判定是否为"自归零惯用法"（如 xor rax, rax）。

    判定条件（必须全部满足）：
      - opcode 在 ZERO_IDIOM_OPCODES 集合内
      - 无 memory 读写（纯寄存器操作）
      - 无 immediate
      - 恰好 1 个读寄存器、1 个写寄存器
      - 读寄存器和写寄存器的 parent 名称相同（如 al/eax 都映射到 rax）

    返回: bool
    """
    if opc not in ZERO_IDIOM_OPCODES:
        return False
    if has_immediates:
        return False
    if read_mems_info or written_mems_info:
        return False
    if len(read_regs_info) != 1 or len(written_regs_info) != 1:
        return False

    src_reg_obj = read_regs_info[0][0]
    dst_reg_obj = written_regs_info[0][0]

    try:
        src_parent = get_parent_reg_name_fn(ctx, src_reg_obj)
        dst_parent = get_parent_reg_name_fn(ctx, dst_reg_obj)
    except Exception:
        return False

    return src_parent == dst_parent


# ==============================================================================
# 修订点2：partial-write RMW 语义检测
# ==============================================================================

def is_partial_write_rmw(reg_obj, ctx, get_parent_reg_name_fn):
    """
    判定一次寄存器写入是否为"partial write read-modify-write"语义。

    x86-64 规则：
      - 64-bit write (rax, rbx, ...): 完全覆盖，不是 RMW
      - 32-bit write (eax, ebx, ...): 自动清零高 32 位，不是 RMW
      - 16-bit write (ax, bx, ...):  保留高 48 位，是 RMW
      - 8-bit write (al, ah, bl, ...): 保留其他位，是 RMW

    返回: (is_rmw: bool, child_name: str, parent_name: str)
      is_rmw=True 时表示需要把 parent 也加入 use_objs 并连边
    """
    try:
        child_name = reg_obj.getName()
        parent_name = get_parent_reg_name_fn(ctx, reg_obj)

        if child_name == parent_name:
            # 写的就是 parent reg 本身，不是 partial write
            return (False, child_name, parent_name)

        bit_size = reg_obj.getBitSize()

        # 32-bit write 在 x86-64 下会清零高位，不算 RMW
        if bit_size >= 32:
            return (False, child_name, parent_name)

        # 16-bit / 8-bit write 保留高位
        return (True, child_name, parent_name)

    except Exception:
        return (False, None, None)


# ==============================================================================
# 修订点3：memory aliasing 别名等价类
# ==============================================================================

class MemoryAliasTracker:
    """
    维护内存对象的别名等价类。

    两层等价关系（决策3：选项A + 选项C 混合）：
      1) 同函数内：rbp/rsp 偏移相同 → 视为同一 stack slot（选项A）
      2) 跨函数：物理 (addr, size) 相同 → 视为同一物理内存位置（选项C）

    每个物理内存访问会被映射到一个"代表 oid"，所有别名共享。
    """

    def __init__(self):
        # 物理地址索引：(addr, size) → 首次出现的 oid（代表元）
        self._phys_to_canonical = {}

        # 反向索引：oid → 它的所有别名 oid 集合（含自己）
        self._oid_to_aliases = defaultdict(set)

        # 标记 oid 是否为"内存型"对象（仅对 mem:* 做别名展开）
        self._mem_oids = set()

    def register(self, oid, addr, size):
        """
        注册一次内存对象访问。
        返回该 oid 的所有别名集合（含 oid 自身）。
        """
        if not isinstance(oid, str) or not oid.startswith('mem:'):
            # 非内存对象不做别名处理
            return {oid}

        self._mem_oids.add(oid)

        key = (addr, size)

        if key not in self._phys_to_canonical:
            self._phys_to_canonical[key] = oid
            self._oid_to_aliases[oid].add(oid)
            return {oid}

        canonical = self._phys_to_canonical[key]

        # 把 oid 和 canonical 互相加入对方的别名集
        # 同时把它们已有的所有别名互相合并
        existing_aliases = set(self._oid_to_aliases[canonical])
        existing_aliases.add(oid)
        existing_aliases.add(canonical)

        # 还要把 oid 已有的别名合并进来
        if oid in self._oid_to_aliases:
            existing_aliases.update(self._oid_to_aliases[oid])

        # 统一更新所有相关 oid 的别名集
        for related in existing_aliases:
            self._oid_to_aliases[related] = existing_aliases

        return set(existing_aliases)

    def get_aliases(self, oid):
        """
        查询 oid 的所有别名（含自己）。如果未注册，返回 {oid}。
        """
        if oid in self._oid_to_aliases:
            return set(self._oid_to_aliases[oid])
        return {oid}


# ==============================================================================
# 修订点4：call 边界 - caller-saved 寄存器集合
# ==============================================================================

# SysV AMD64 ABI caller-saved registers
# 这些寄存器在 call 之后值"不可预测"，必须视为"被调用方定义过"
CALLER_SAVED_REGS_SYSV = (
    'rax', 'rcx', 'rdx', 'rsi', 'rdi',
    'r8', 'r9', 'r10', 'r11',
    # 浮点/向量寄存器（XMM0-XMM15 在调用约定下也是 caller-saved）
    'xmm0', 'xmm1', 'xmm2', 'xmm3', 'xmm4', 'xmm5', 'xmm6', 'xmm7',
    'xmm8', 'xmm9', 'xmm10', 'xmm11', 'xmm12', 'xmm13', 'xmm14', 'xmm15',
)


def get_caller_saved_canonical_oids(ctx, objcanon):
    """
    返回 caller-saved 寄存器的 canonical obj_id 集合。
    无副作用，可在 call 处理时按需调用。
    """
    oids = set()
    for reg_name in CALLER_SAVED_REGS_SYSV:
        try:
            reg = getattr(ctx.registers, reg_name, None)
            if reg is None:
                continue
            oid, _, _, _ = objcanon.canon_reg(reg)
            oids.add(oid)
        except Exception:
            continue
    return oids


# ==============================================================================
# 修订点6：弱连通节点补全
# ==============================================================================

def recover_weakly_connected_nodes(
    slice_result,
    obj_seed_nodes,
    executed_pcs,
    inst_use_objects,
    inst_def_objects,
    inst_addr_objects,
    inst_mem_objects,
    inst_controlled_by,
    inst_ctrl_objects,
    node_meta,
    control_expansion_mode,
    max_recovery_hops=2,
    max_recovery_nodes=128,
):
    """
    方案2核心：在 slice 完成后，扫描 backward_obj_reachable 中"入度异常为0"的节点，
    通过 obj_def_pcs 反查它们在 trace 中的最近一次有效定义，恢复被 hotspot 熔断的边。

    设计原则：
      - 不修改 main() 中的事实表
      - 只补充 object_edge_meta 中的边（kind='synthetic_recovery'）
      - 同时更新 forward/backward reachable 集合
      - 受 max_recovery_hops 和 max_recovery_nodes 约束，防止图爆炸

    返回（in-place 修改 slice_result，同时返回统计信息）：
      {
        'recovered_edges': int,
        'recovered_nodes': int,
        'recovery_log': [(src_oid, dst_oid, pc, reason), ...]
      }
    """
    object_edge_meta = slice_result['object_edge_meta']
    forward_obj_reachable = slice_result['forward_obj_reachable']
    backward_obj_reachable = slice_result['backward_obj_reachable']
    sliced_node_meta = slice_result['sliced_node_meta']
    obj_def_pcs = slice_result['obj_def_pcs']
    obj_use_pcs = slice_result['obj_use_pcs']
    obj_addr_use_pcs = slice_result['obj_addr_use_pcs']
    obj_ctrl_use_pcs = slice_result['obj_ctrl_use_pcs']

    # 构建当前 slice 内的入度索引（只看 data 和 control 边）
    in_degree = defaultdict(int)
    for (src, dst), meta in object_edge_meta.items():
        kinds = meta.get('kinds', set())
        if 'data' in kinds or 'control' in kinds or 'addr' in kinds:
            in_degree[dst] += 1

    # 找出 backward_reachable 中入度为0且不是 seed 的"悬空节点"
    orphans = []
    for oid in backward_obj_reachable:
        if oid in obj_seed_nodes:
            continue
        if in_degree.get(oid, 0) == 0:
            orphans.append(oid)

    recovered_edges = 0
    recovered_nodes = 0
    recovery_log = []

    # 工作队列：(待恢复 oid, 剩余跳数)
    work_queue = deque((oid, max_recovery_hops) for oid in orphans)
    processed = set()

    while work_queue and recovered_nodes < max_recovery_nodes:
        target_oid, hops_left = work_queue.popleft()

        if target_oid in processed:
            continue
        processed.add(target_oid)

        if hops_left <= 0:
            continue

        # 策略B（决策4）：从全量 inst_def_objects 中反查 target_oid 的所有 def pc
        # （不依赖 slice 内的 obj_def_pcs，因为它已经被裁剪过）
        candidate_def_pcs = set()
        for pc in executed_pcs:
            if target_oid in inst_def_objects.get(pc, set()):
                candidate_def_pcs.add(pc)

        if not candidate_def_pcs:
            # 完全没有定义记录 - 可能是初始值/外部输入
            continue

        # 对每个候选 def pc，把它的 use_objs / 控制源加为新的 edge 来源
        # 这就"恢复"了被 hotspot 熔断的依赖关系
        for def_pc in candidate_def_pcs:
            use_objs_at_def = inst_use_objects.get(def_pc, set())
            ctrl_srcs_at_def = set()

            if control_expansion_mode in ('def-only', 'all'):
                for bpc in inst_controlled_by.get(def_pc, set()):
                    ctrl_srcs_at_def.update(inst_ctrl_objects.get(bpc, set()))

            # 添加 data 恢复边
            for src_oid in use_objs_at_def:
                if src_oid == target_oid:
                    continue
                edge_key = (src_oid, target_oid)
                if edge_key not in object_edge_meta:
                    _add_synthetic_edge(object_edge_meta, src_oid, target_oid,
                                       'synthetic_recovery_data', def_pc)
                    recovered_edges += 1
                    recovery_log.append((src_oid, target_oid, def_pc, 'data_via_def'))

                # 把新引入的节点加入 reachable 集合
                if src_oid not in backward_obj_reachable:
                    backward_obj_reachable.add(src_oid)
                    recovered_nodes += 1
                    # 同步 sliced_node_meta（如果原 node_meta 有这个 oid）
                    if src_oid in node_meta and src_oid not in sliced_node_meta:
                        sliced_node_meta[src_oid] = node_meta[src_oid]
                    # 把新节点加入工作队列，继续向上恢复
                    work_queue.append((src_oid, hops_left - 1))

                # 更新 obj_use_pcs（用于后续报告）
                obj_use_pcs[src_oid].add(def_pc)

            # 添加 control 恢复边
            for src_oid in ctrl_srcs_at_def:
                if src_oid == target_oid:
                    continue
                edge_key = (src_oid, target_oid)
                if edge_key not in object_edge_meta:
                    _add_synthetic_edge(object_edge_meta, src_oid, target_oid,
                                       'synthetic_recovery_control', def_pc)
                    recovered_edges += 1
                    recovery_log.append((src_oid, target_oid, def_pc, 'control_via_def'))

                if src_oid not in backward_obj_reachable:
                    backward_obj_reachable.add(src_oid)
                    recovered_nodes += 1
                    if src_oid in node_meta and src_oid not in sliced_node_meta:
                        sliced_node_meta[src_oid] = node_meta[src_oid]
                    work_queue.append((src_oid, hops_left - 1))

                obj_ctrl_use_pcs[src_oid].add(def_pc)

            # 更新 obj_def_pcs（target_oid 的定义点）
            obj_def_pcs[target_oid].add(def_pc)

    return {
        'recovered_edges': recovered_edges,
        'recovered_nodes': recovered_nodes,
        'recovery_log': recovery_log,
        'orphan_count': len(orphans),
    }


def _add_synthetic_edge(edge_meta, src, dst, kind, pc):
    """
    添加 synthetic_recovery 边。
    避开 add_edge_meta 的 count 累加语义（synthetic 边只记一次）。
    """
    info = edge_meta.setdefault((src, dst), {
        'kinds': set(),
        'pcs': set(),
        'count': 0,
        'kind_counts': {},
    })
    info['kinds'].add(kind)
    info['count'] += 1
    info['kind_counts'][kind] = info['kind_counts'].get(kind, 0) + 1
    if pc is not None:
        info['pcs'].add(pc)