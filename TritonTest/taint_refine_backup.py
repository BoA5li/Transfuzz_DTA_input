#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Triton 动态污点 + 双向依赖分析（带源码映射、外部函数与特殊指令模拟）
功能:
  - ELF 段加载 + 动态执行
  - 指令地址 <-> 源码文件 : 行号
  - 寄存器 / 内存地址 <-> 源码变量 / 参数名
  - 外部库函数钩子 (__libc_start_main, printf, strlen 等)
  - 特殊指令 (rdtscp, clflush) 仿真
"""

import struct
import sys
from triton import TritonContext, ARCH, Instruction, MemoryAccess, OPERAND
from elftools.elf.elffile import ELFFile


# ------------------------------------------------------------------------
def load_all_code_segments(path):
    """
    加载所有代码段（PT_LOAD + .text + .plt），同时返回 ELF entry
    """
    segs = []
    e_entry = None
    with open(path, "rb") as f:
        elf = ELFFile(f)
        # 入口地址
        e_entry = elf.header['e_entry']

        # 加载所有 PT_LOAD 段
        for seg in elf.iter_segments():
            if seg['p_type'] == 'PT_LOAD':
                data = seg.data()
                segs.append((seg['p_vaddr'], data))

        # 确保 .text 和 .plt 也加载
        for secname in ('.text', '.plt', '.plt.sec'):
            sec = elf.get_section_by_name(secname)
            if sec:
                data = sec.data()
                segs.append((sec['sh_addr'], data))

    return segs, e_entry


def build_addr2line_map(path):
    """地址 -> (文件名, 行号)"""
    mapping = {}
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        if not elf.has_dwarf_info():
            return mapping
        dwarfinfo = elf.get_dwarf_info()
        for CU in dwarfinfo.iter_CUs():
            lp = dwarfinfo.line_program_for_CU(CU)
            for entry in lp.get_entries():
                if entry.state is None:
                    continue
                addr = entry.state.address
                file_index = entry.state.file
                line = entry.state.line
                filename = lp['file_entry'][file_index - 1].name.decode()
                mapping[addr] = (filename, line)
    return mapping


def build_global_var_map(path):
    """内存地址 -> 全局变量名"""
    varmap = {}
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        symtab = elf.get_section_by_name('.symtab')
        if not symtab:
            return varmap
        for sym in symtab.iter_symbols():
            addr = sym.entry['st_value']
            name = sym.name
            if addr != 0:
                varmap[addr] = name
    return varmap


def build_symbol_addr_map(path):
    """函数地址 -> 名称"""
    symmap = {}
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        symtab = elf.get_section_by_name('.symtab')
        if not symtab:
            return symmap
        for sym in symtab.iter_symbols():
            if sym.entry['st_value'] != 0:
                symmap[sym.entry['st_value']] = sym.name
    return symmap


def read_mem_int(ctx, addr, size):
    raw = ctx.getConcreteMemoryAreaValue(addr, size)
    return int.from_bytes(bytes(raw), "little")


# ------------------------------------------------------------------------


def hook_printf(ctx):
    ctx.setConcreteRegisterValue(ctx.registers.rax, 0)
    return


def hook_strlen(ctx):
    ctx.setConcreteRegisterValue(ctx.registers.rax, 10)
    return


def hook_rdtscp(ctx, inst_count, inst):
    # 模拟 rdtscp 的返回值
    print(f"[hook-rdtscp] at 0x{ctx.getConcreteRegisterValue(ctx.registers.rip):x}")
    ctx.setConcreteRegisterValue(ctx.registers.rax, inst_count & 0xffffffff)
    ctx.setConcreteRegisterValue(ctx.registers.rdx, 0)
    ctx.setConcreteRegisterValue(ctx.registers.rcx, 0)

    # 用 inst 的真实大小推进 RIP
    rip = ctx.getConcreteRegisterValue(ctx.registers.rip)
    ctx.setConcreteRegisterValue(ctx.registers.rip, rip + inst.getSize())


def hook_clflush(ctx, inst):
    print(f"[hook-clflush] at 0x{ctx.getConcreteRegisterValue(ctx.registers.rip):x}")
    # 只跳过指令，不关心缓存效果，也用真实大小推进 RIP
    rip = ctx.getConcreteRegisterValue(ctx.registers.rip)
    ctx.setConcreteRegisterValue(ctx.registers.rip, rip + inst.getSize())


def build_got_plt_map(path):
    """解析 .got.plt/.got 和 .plt/.dyn 段，返回 {GOT条目虚拟地址: 符号名}"""
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
                got_map[rel.entry['r_offset']] = sym.name
    return got_map


# ------------------------------------------------------------------------
def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} ./test_elf")
        return
    path = sys.argv[1]
    segs, entry = load_all_code_segments(path)
    addr2line_map = build_addr2line_map(path)
    global_var_map = build_global_var_map(path)
    symbol_addr_map = build_symbol_addr_map(path)

    ctx = TritonContext()
    ctx.setArchitecture(ARCH.X86_64)
    print(f"[+] Triton initialized, entry = 0x{entry:x}")

    for vaddr, data in segs:
        ctx.setConcreteMemoryAreaValue(vaddr, bytearray(data))

    STACK_ADDR, STACK_SIZE = 0x70000000, 0x20000
    ctx.setConcreteMemoryAreaValue(STACK_ADDR, bytearray(STACK_SIZE))
    rspVal = STACK_ADDR + STACK_SIZE - 0x1000
    argvAddr = STACK_ADDR + 0x100
    ctx.setConcreteMemoryAreaValue(argvAddr, b"prog\0")

    ctx.setConcreteRegisterValue(ctx.registers.rsp, rspVal)
    ctx.setConcreteRegisterValue(ctx.registers.rdi, 1)
    ctx.setConcreteRegisterValue(ctx.registers.rsi, argvAddr)
    ctx.setConcreteRegisterValue(ctx.registers.rip, entry)

    # 在全局符号中查找 array2 的地址
    TaintSource_addr = None
    for addr, name in global_var_map.items():
        if name == 'array2':
            TaintSource_addr = addr
            break

    if TaintSource_addr is None:
        raise RuntimeError("Cannot find global symbol 'array2' in ELF")

    SECRET_ADDR = TaintSource_addr
    SECRET_LEN  = 256 * 512   # 或者根据实际定义改

    sec_name = "array2"

    for i in range(SECRET_LEN):
        m = MemoryAccess(SECRET_ADDR + i, 1)
        ctx.taintMemory(m)
        ctx.symbolizeMemory(m, f"array2_byte_{i}")

    print(f"[+] Secret region tainted: {sec_name} 0x{SECRET_ADDR:x}-0x{SECRET_ADDR+SECRET_LEN-1:x}")

    # 钩子表
    hooks = {
        'printf': hook_printf,
        'strlen': hook_strlen,
    }

    cfg_edges = set()   # {(src_pc, dst_pc)}
    dfg_edges = set()   # {(def_pc, use_pc)}

    # 记录某条指令执行后，是否“含 taint”
    node_taint = {}     # pc -> {"regs": set(reg_names), "mems": set(addresses)}
    tainted_regs = set()
    tainted_mems = set()

    # 最近一次定义某个寄存器/内存的位置（用于建立数据流边）
    last_def_reg = {}   # reg_id -> pc
    last_def_mem = {}   # addr   -> pc

    got_map = build_got_plt_map(path)
    # 启动前取一次 main_addr
    main_addr = None
    plt_ranges = []
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        symtab = elf.get_section_by_name('.symtab')
        if symtab:
            for sym in symtab.iter_symbols():
                if sym.name == 'main':
                    main_addr = sym.entry['st_value']
                    break
        for secname in ('.plt', '.plt.sec'):
            sec_plt = elf.get_section_by_name(secname)
            if sec_plt:
                start = sec_plt['sh_addr']
                end = start + sec_plt['sh_size']
                plt_ranges.append((start, end))

    # 找 exit_addr：这里只是简单找出 entry 段内的最后一个 hlt 的地址
    exit_addr = None
    with open(path, 'rb') as f:
        elf = ELFFile(f)
        text_sec = elf.get_section_by_name('.text')
        if text_sec:
            text_end = text_sec['sh_addr'] + text_sec['sh_size']
            exit_addr = text_end + 0x10  # 文本段之后的安全区域
            # 在内存中写入一个hlt作为结束标记
            ctx.setConcreteMemoryAreaValue(exit_addr, bytes([0xF4]))
    
    code_ranges = [(vaddr, vaddr + len(data)) for (vaddr, data) in segs]
    if exit_addr is not None:
        code_ranges.append((exit_addr, exit_addr + 1))

    def in_loaded_code(addr: int) -> bool:
        return any(s <= addr < e for (s, e) in code_ranges)

    def in_plt(addr: int) -> bool:
        return any(s <= addr < e for (s, e) in plt_ranges)

    tainted_regs, tainted_mems = set(), set()
    inst_count = 0
    done = False
    entered_main = False   # 记录是否已经进入过main
    call_stack = []

    # 记录每个 PC 被执行次数
    pc_hit_count = {}
    # 记录每条“向后跳转”分支的被采用次数（可视为循环迭代次数）
    back_edge_taken = {}   # key: (src_pc, dst_pc)
    inst_info = {}  # 全局：pc -> {"opc": opc, "disasm": disasm}
    inst_uses_taint = {}  # pc -> bool，当前指令是否真正与 taint 交互
    # 记录每条指令“实际参与的 taint”信息
    inst_taint_io = {}  # pc -> {"use_regs": set(), "use_mems": set(),
                        #        "def_regs": set(), "def_mems": set()}


    while not done:
        pc = ctx.getConcreteRegisterValue(ctx.registers.rip)
        pc_hit_count[pc] = pc_hit_count.get(pc, 0) + 1

        # 如果 PC 跳出已加载段，直接根据 call_stack 退回或结束
        if not in_loaded_code(pc):
            print(f"[warn] PC 0x{pc:x} out of loaded code.")
            if call_stack:
                ret_addr = call_stack.pop()
                print(f"[info] popping ret_addr=0x{ret_addr:x} from call_stack")
                if not in_loaded_code(ret_addr):
                    print(f"[warn] ret_addr 0x{ret_addr:x} also invalid, stopping.")
                    done = True
                    break
                ctx.setConcreteRegisterValue(ctx.registers.rip, ret_addr)
                continue
            else:
                print("[info] call_stack empty and PC invalid, stopping.")
                done = True
                break

        # 取指+执行
        opcode = ctx.getConcreteMemoryAreaValue(pc, 16)
        inst = Instruction()
        inst.setOpcode(opcode)
        inst.setAddress(pc)

        ctx.disassembly(inst)
        disasm = inst.getDisassembly()
        # 调试用指令 trace
        '''
        src_info = addr2line_map.get(pc)
        if src_info:
            print(f"[{inst_count+1}] 0x{pc:x}: {disasm}  ; {src_info[0]}:{src_info[1]}")
        else:
            print(f"[{inst_count+1}] 0x{pc:x}: {disasm}")
        '''

        opc = disasm.split()[0].lower()

        inst_info[pc] = {"opc": opc, "disasm": disasm}


        # 特殊指令在执行前拦截
        if opc == 'rdtscp':
            old_pc = pc
            # 用 inst 的真实大小推进 RIP，而不是硬编码 +3
            hook_rdtscp(ctx, inst_count, inst)
            new_pc = ctx.getConcreteRegisterValue(ctx.registers.rip)
            cfg_edges.add((old_pc, new_pc))
            inst_count += 1
            continue

        if opc.startswith('clflush'):
            old_pc = pc
            hook_clflush(ctx, inst)
            new_pc = ctx.getConcreteRegisterValue(ctx.registers.rip)
            cfg_edges.add((old_pc, new_pc))
            inst_count += 1
            continue

        # 普通指令交给 Triton 执行
        ctx.processing(inst)
        inst_count += 1

        next_pc = ctx.getConcreteRegisterValue(ctx.registers.rip)

        # ---------- 记录控制流边 ----------
        cfg_edges.add((pc, next_pc))

        # ---------- 读/写寄存器 ----------
        read_regs_info    = inst.getReadRegisters()      # [(Register, AstNode), ...]
        written_regs_info = inst.getWrittenRegisters()   # [(Register, AstNode), ...]

        # 只取 Register 对象本身
        read_regs    = [reg for (reg, ast) in read_regs_info]
        written_regs = [reg for (reg, ast) in written_regs_info]

        # ---------- 读/写内存 ----------
        read_mems_info    = inst.getLoadAccess()         # [(MemoryAccess, AstNode), ...]
        written_mems_info = inst.getStoreAccess()        # [(MemoryAccess, AstNode), ...]

        # 只取 MemoryAccess 对象本身
        read_mems    = [mem for (mem, ast) in read_mems_info]
        written_mems = [mem for (mem, ast) in written_mems_info]

        # ---------- 数据流图：从上游定义到当前 pc 的依赖 ----------
        # 寄存器依赖
        for reg in read_regs:
            rname = reg.getName()
            if rname in last_def_reg:
                dfg_edges.add((last_def_reg[rname], pc))

        # 内存依赖（以起始地址为 key，简化）
        for mem in read_mems:
            addr = mem.getAddress()
            if addr in last_def_mem:
                dfg_edges.add((last_def_mem[addr], pc))

        # ---------- 更新当前定义 ----------
        for reg in written_regs:
            rname = reg.getName()
            last_def_reg[rname] = pc

        for mem in written_mems:
            addr = mem.getAddress()
            last_def_mem[addr] = pc

        # ---------- 本条指令是否真正使用/传播 taint ----------
        # 1) 读到 tainted 寄存器？
        used_tainted_reg = False
        for reg, _ in read_regs_info:
            if ctx.isRegisterTainted(reg):
                used_tainted_reg = True
                break

        # 2) 读到 tainted 内存？
        used_tainted_mem = False
        for mem, _ in read_mems_info:
            if ctx.isMemoryTainted(mem):
                used_tainted_mem = True
                break

        # 3) 写出了 tainted 寄存器？（结果 tainted）
        wrote_tainted_reg = False
        for reg, _ in written_regs_info:
            if ctx.isRegisterTainted(reg):
                wrote_tainted_reg = True
                break

        # 4) 写出了 tainted 内存？（写目标是 tainted）
        wrote_tainted_mem = False
        for mem, _ in written_mems_info:
            if ctx.isMemoryTainted(mem):
                wrote_tainted_mem = True
                break

        inst_uses_taint_flag = (used_tainted_reg or used_tainted_mem or
                                wrote_tainted_reg or wrote_tainted_mem)

        # 初始化一个全局字典存这个信息（在循环外先声明）
        # inst_uses_taint = {}  # pc -> bool
        inst_uses_taint[pc] = inst_uses_taint_flag


        # ---------- 本条指令实际参与的 taint（Use / Def） ----------
        use_tainted_regs = set()
        use_tainted_mems = set()
        def_tainted_regs = set()
        def_tainted_mems = set()

        # 一个小工具函数：给任意子寄存器取父寄存器名字
        def get_parent_reg_name(ctx, reg):
            try:
                parent = ctx.getParentRegister(reg)
                return parent.getName()
            except Exception:
                # 万一某些情况下出错，就退回当前寄存器名，不让分析中断
                return reg.getName()

        # 1) 本指令读到的 tainted 寄存器
        for reg, _ in read_regs_info:
            if ctx.isRegisterTainted(reg):
                # 用父寄存器名字统一展示
                use_tainted_regs.add(get_parent_reg_name(ctx, reg))

        # 2) 本指令读到的 tainted 内存
        for mem, _ in read_mems_info:
            if ctx.isMemoryTainted(mem):
                use_tainted_mems.add(mem.getAddress())

        # 3) 本指令写出的 tainted 寄存器（结果 tainted）
        for reg, _ in written_regs_info:
            if ctx.isRegisterTainted(reg):
                def_tainted_regs.add(get_parent_reg_name(ctx, reg))

        # 4) 本指令写出的 tainted 内存（写目标是 tainted）
        for mem, _ in written_mems_info:
            if ctx.isMemoryTainted(mem):
                def_tainted_mems.add(mem.getAddress())

        inst_taint_io[pc] = {
            "use_regs": use_tainted_regs,
            "use_mems": use_tainted_mems,
            "def_regs": def_tainted_regs,
            "def_mems": def_tainted_mems,
        }
        

        # ---------- 本条指令的 taint 状态 ----------
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

        if regs_t or mems_t:
            node_taint[pc] = {"regs": regs_t, "mems": mems_t}

        

        # 简单判断：如果是 jmp/jcc 类指令，并且跳转目标 < 当前 pc，则视作“回边”
        if opc.startswith('j'):
            # 如果执行完后的 next_pc 小于当前 pc，并且 next_pc 落在代码段内，当作“回边”
            if next_pc < pc and in_loaded_code(next_pc):
                key = (pc, next_pc)
                back_edge_taken[key] = back_edge_taken.get(key, 0) + 1

        # ---------- call 处理 ----------
        if opc == "call":
            #pc = inst.getAddress()
            ret_next = pc + inst.getSize()
            target = inst.getOperands()[0]
            target_addr = None
            got_entry = None

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

            # 1️⃣ 通过 GOT 表识别外部函数
            if got_entry and got_entry in got_map:
                target_name = got_map[got_entry]
                print(f"[hook] call through GOT entry 0x{got_entry:x} -> {target_name}")

                # 专门处理 __libc_start_main
                if target_name == '__libc_start_main':
                    if not entered_main:
                        entered_main = True
                        print(f"[hook] __libc_start_main -> jump to main at 0x{main_addr:x}")

                        # main ret 后跳到 exit_addr（你写入的 hlt）
                        if exit_addr is None:
                            raise RuntimeError("exit_addr is None")
                        call_stack.append(exit_addr)
                        new_pc = main_addr
                        cfg_edges.add((pc, new_pc))

                        ctx.setConcreteRegisterValue(ctx.registers.rip, main_addr)
                        continue
                    else:
                        done = True
                        break

                # 对 printf / strlen 等钩子函数，执行模拟返回
                if target_name in hooks:
                    hooks[target_name](ctx)
                    new_pc = ret_next
                    cfg_edges.add((pc, new_pc))
                    ctx.setConcreteRegisterValue(ctx.registers.rip, ret_next)
                    continue

            # 2️⃣ 未命中 GOT，再看符号表
            if target_addr is not None and target_name is None:
                symname = symbol_addr_map.get(target_addr)
                if symname and symname in hooks:
                    print(f"[hook] call {symname} at 0x{target_addr:x}")
                    hooks[symname](ctx)
                    new_pc = ret_next
                    cfg_edges.add((pc, new_pc))
                    ctx.setConcreteRegisterValue(ctx.registers.rip, ret_next)
                    continue

            # 3️⃣ PLT表范围 -> 外部库函数，直接模拟返回
            if target_addr is not None and in_plt(target_addr):
                new_pc = ret_next
                cfg_edges.add((pc, new_pc))
                ctx.setConcreteRegisterValue(ctx.registers.rip, ret_next)
                continue

            # 4️⃣ 内部函数：在已加载段内，压入返回地址后跳入执行
            if target_addr is not None and in_loaded_code(target_addr):
                print(f"[debug] push return 0x{ret_next:x} for call at 0x{pc:x}")
                call_stack.append(ret_next)
                new_pc = target_addr
                cfg_edges.add((pc, new_pc))  
                ctx.setConcreteRegisterValue(ctx.registers.rip, target_addr)
                continue

            # 5️⃣ 外部库函数（无实现）
            new_pc = ret_next
            cfg_edges.add((pc, new_pc))
            ctx.setConcreteRegisterValue(ctx.registers.rip, ret_next)
            continue

        # ---------- ret 处理 ----------
        if opc == "ret":
            if call_stack:
                ret_addr = call_stack.pop()
                if not in_loaded_code(ret_addr):
                    print(f"[warn] ret to invalid address 0x{ret_addr:x}, stopping.")
                    done = True
                    break
                cfg_edges.add((pc, ret_addr))
                ctx.setConcreteRegisterValue(ctx.registers.rip, ret_addr)
                continue
            else:
                print("[info] ret with empty call_stack, program finished.")
                done = True
                break

        # ---------- 程序正常结束 ----------
        if opc == "hlt":
            print("[info] HLT reached, program finished.")
            done = True
            break


    # 输出汇总
    print(f"[+] Executed {inst_count} instructions.")
    print("[+] Tainted registers:", sorted(list(tainted_regs)))
    print("[+] Tainted memory addresses:", [f"0x{a:x}" for a in sorted(tainted_mems)])

    '''
    print("[+] Loop head hit counts (pc -> times):")
    # 只打印命中次数较大的 PC，过滤掉噪音
    for addr, cnt in sorted(pc_hit_count.items()):
        if cnt > 1 and in_loaded_code(addr):
            info = addr2line_map.get(addr)
            if info:
                print(f"    0x{addr:x}  hits={cnt:<6}  ; {info[0]}:{info[1]}")
            else:
                print(f"    0x{addr:x}  hits={cnt}")

    print("[+] Back-edge (loop) taken counts (src -> dst -> times):")
    for (src, dst), cnt in sorted(back_edge_taken.items(), key=lambda x: -x[1]):
        info_src = addr2line_map.get(src)
        info_dst = addr2line_map.get(dst)
        src_str = f"0x{src:x}"
        dst_str = f"0x{dst:x}"
        if info_src:
            src_str += f" ({info_src[0]}:{info_src[1]})"
        if info_dst:
            dst_str += f" ({info_dst[0]}:{info_dst[1]})"
        print(f"    {src_str}  ->  {dst_str}  : taken {cnt} times")
    '''
    #CFG
    with open("cfg.dot", "w") as f:
        f.write("digraph CFG {\n")

        # 节点：所有执行过的 pc
        for pc in sorted(pc_hit_count.keys()):
            src_info = addr2line_map.get(pc)
            label_lines = []

            # 行1：pc
            label_lines.append(f"0x{pc:x}")

            # 行2：源码位置
            if src_info:
                label_lines.append(f"{src_info[0]}:{src_info[1]}")

            # 行3/4：taint 细节（如果有）
            if pc in node_taint:
                info = node_taint[pc]
                regs_t = sorted(info["regs"])
                mems_t = sorted(info["mems"])
                if regs_t:
                    label_lines.append("Tregs: " + ",".join(regs_t))
                if mems_t:
                    # 只展示前几个地址，避免过长
                    mem_strs = [f"0x{a:x}" for a in mems_t[:4]]
                    if len(mems_t) > 4:
                        mem_strs.append("...")
                    label_lines.append("Tmems: " + ",".join(mem_strs))

            # 新增：本指令使用/定义的 taint
            io = inst_taint_io.get(pc)
            if io:
                uregs = sorted(io["use_regs"])
                umems = sorted(io["use_mems"])
                dregs = sorted(io["def_regs"])
                dmems = sorted(io["def_mems"])

                if uregs:
                    label_lines.append("UseTregs: " + ",".join(uregs))
                if umems:
                    mem_strs = [f"0x{a:x}" for a in umems[:4]]
                    if len(umems) > 4:
                        mem_strs.append("...")
                    label_lines.append("UseTmems: " + ",".join(mem_strs))

                if dregs:
                    label_lines.append("DefTregs: " + ",".join(dregs))
                if dmems:
                    mem_strs = [f"0x{a:x}" for a in dmems[:4]]
                    if len(dmems) > 4:
                        mem_strs.append("...")
                    label_lines.append("DefTmems: " + ",".join(mem_strs))

            # 合并为多行 label
            label = "\\n".join(label_lines)

            # 颜色：只在“指令真正使用/传播 taint”时标红
            if inst_uses_taint.get(pc, False):
                color = "red"
            else:
                color = "black"

            f.write(f'  "0x{pc:x}" [label="{label}", color="{color}"];\n')

        # 边
        for (src, dst) in cfg_edges:
            f.write(f'  "0x{src:x}" -> "0x{dst:x}";\n')

        f.write("}\n")

    #CFG_BB: 基本块级 CFG
    # 先统计前驱/后继计数
    succs = {}  # pc -> set(next_pcs)
    preds = {}  # pc -> set(prev_pcs)

    for (src, dst) in cfg_edges:
        succs.setdefault(src, set()).add(dst)
        preds.setdefault(dst, set()).add(src)

    def is_terminator(pc):
        """判断一条指令是否作为基本块末尾"""
        info = inst_info.get(pc)
        if not info:
            return False
        opc = info["opc"]
        if opc.startswith('j'):       # jmp, je, jne, ...
            return True
        if opc in ('call', 'ret', 'hlt'):
            return True
        return False

    blocks = []      # list[list[pc]]
    visited = set()  # 已经划入某个块的 pc

    for pc in sorted(pc_hit_count.keys()):
        if pc in visited:
            continue

        # 向前扩展，找出 basic block 的开始
        start = pc
        while True:
            preds_set = preds.get(start, set())
            # 前驱恰好一个，且该前驱的后继也恰好一个，且前驱不是terminator
            if len(preds_set) != 1:
                break
            prev_pc = next(iter(preds_set))
            succs_of_prev = succs.get(prev_pc, set())
            if len(succs_of_prev) != 1:
                break
            if is_terminator(prev_pc):
                break
            start = prev_pc

        # 从 start 往后扩展，直到块末尾
        block_pcs = []
        cur = start
        while True:
            block_pcs.append(cur)
            visited.add(cur)
            if is_terminator(cur):
                break
            succs_set = succs.get(cur, set())
            if len(succs_set) != 1:
                break
            nxt = next(iter(succs_set))
            preds_of_nxt = preds.get(nxt, set())
            if len(preds_of_nxt) != 1:
                break
            cur = nxt

        blocks.append(block_pcs)

    # 为每个 pc 赋所属 block id
    pc2block = {}
    for i, pcs in enumerate(blocks):
        bid = f"BB{i}"
        for pc in pcs:
            pc2block[pc] = bid

    # 构建块级边：只保留跨块边
    block_edges = set()
    for (src, dst) in cfg_edges:
        bsrc = pc2block.get(src)
        bdst = pc2block.get(dst)
        if not bsrc or not bdst:
            continue
        if bsrc != bdst:
            block_edges.add((bsrc, bdst))

    # 输出基本块级 CFG
    with open("cfg_bb.dot", "w") as f:
        f.write("digraph CFG_BB {\n")

        # 节点：每个基本块
        for i, pcs in enumerate(blocks):
            bid = f"BB{i}"
            lines = []

            for pc in pcs:
                parts = [f"0x{pc:x}"]

                # 源码信息
                src_info = addr2line_map.get(pc)
                if src_info:
                    parts.append(f"{src_info[0]}:{src_info[1]}")

                # 指令反汇编
                info = inst_info.get(pc)
                if info:
                    parts.append(info["disasm"])

                # taint 细节
                if pc in node_taint:
                    tinfo = node_taint[pc]
                    regs_t = sorted(tinfo["regs"])
                    mems_t = sorted(tinfo["mems"])
                    if regs_t:
                        parts.append("Tregs:" + ",".join(regs_t))
                    if mems_t:
                        mem_strs = [f"0x{a:x}" for a in mems_t[:3]]
                        if len(mems_t) > 3:
                            mem_strs.append("...")
                        parts.append("Tmems:" + ",".join(mem_strs))

                # 新增：本指令实际使用/定义的 taint（Use / Def）
                io = inst_taint_io.get(pc)
                if io:
                    uregs = sorted(io["use_regs"])
                    umems = sorted(io["use_mems"])
                    dregs = sorted(io["def_regs"])
                    dmems = sorted(io["def_mems"])

                    if uregs:
                        parts.append("UseTregs:" + ",".join(uregs))
                    if umems:
                        mem_strs = [f"0x{a:x}" for a in umems[:3]]
                        if len(umems) > 3:
                            mem_strs.append("...")
                        parts.append("UseTmems:" + ",".join(mem_strs))

                    if dregs:
                        parts.append("DefTregs:" + ",".join(dregs))
                    if dmems:
                        mem_strs = [f"0x{a:x}" for a in dmems[:3]]
                        if len(dmems) > 3:
                            mem_strs.append("..."
                            )
                        parts.append("DefTmems:" + ",".join(mem_strs))

                line = " ".join(parts)
                lines.append(line)

            # Graphviz 左对齐换行
            label = "\\l".join(lines) + "\\l"
            color = "red" if any(inst_uses_taint.get(pc, False) for pc in pcs) else "black"
            f.write(f'  "{bid}" [shape=box, label="{label}", color="{color}"];\n')

        # 边：块与块之间
        for (bsrc, bdst) in sorted(block_edges):
            f.write(f'  "{bsrc}" -> "{bdst}";\n')

        f.write("}\n")

    #DFG: 指令级数据流图（带 taint 细节）
    with open("dfg.dot", "w") as f:
        f.write("digraph DFG {\n")

        # 节点：所有执行过的 pc
        for pc in sorted(pc_hit_count.keys()):
            src_info = addr2line_map.get(pc)
            label_lines = [f"0x{pc:x}"]
            if src_info:
                label_lines.append(f"{src_info[0]}:{src_info[1]}")

            # taint 细节
            if pc in node_taint:
                info = node_taint[pc]
                regs_t = sorted(info["regs"])
                mems_t = sorted(info["mems"])
                if regs_t:
                    label_lines.append("Tregs: " + ",".join(regs_t))
                if mems_t:
                    mem_strs = [f"0x{a:x}" for a in mems_t[:3]]
                    if len(mems_t) > 3:
                        mem_strs.append("...")
                    label_lines.append("Tmems: " + ",".join(mem_strs))

            # 新增：本指令实际使用/定义的 taint
            io = inst_taint_io.get(pc)
            if io:
                uregs = sorted(io["use_regs"])
                umems = sorted(io["use_mems"])
                dregs = sorted(io["def_regs"])
                dmems = sorted(io["def_mems"])

                if uregs:
                    label_lines.append("UseTregs: " + ",".join(uregs))
                if umems:
                    mem_strs = [f"0x{a:x}" for a in umems[:3]]
                    if len(umems) > 3:
                        mem_strs.append("...")
                    label_lines.append("UseTmems: " + ",".join(mem_strs))

                if dregs:
                    label_lines.append("DefTregs: " + ",".join(dregs))
                if dmems:
                    mem_strs = [f"0x{a:x}" for a in dmems[:3]]
                    if len(dmems) > 3:
                        mem_strs.append("...")
                    label_lines.append("DefTmems: " + ",".join(mem_strs))

            label = "\\n".join(label_lines)
            color = "red" if inst_uses_taint.get(pc, False) else "black"
            f.write(f'  "0x{pc:x}" [label="{label}", color="{color}"];\n')

        # 边：数据依赖边
        for (def_pc, use_pc) in dfg_edges:
            # 可选：taint 相关边染红；也可以全黑，这里给一个示例
            if def_pc in node_taint or use_pc in node_taint:
                f.write(f'  "0x{def_pc:x}" -> "0x{use_pc:x}" [color="red"];\n')
            else:
                f.write(f'  "0x{def_pc:x}" -> "0x{use_pc:x}";\n')

        f.write("}\n")

    #CDFG
    with open("cdfg.dot", "w") as f:
        f.write("digraph CDFG {\n")

        for pc in sorted(pc_hit_count.keys()):
            src_info = addr2line_map.get(pc)
            label = f"0x{pc:x}"
            if src_info:
                label += f"\\n{src_info[0]}:{src_info[1]}"
            color = "red" if pc in node_taint else "black"
            f.write(f'  "0x{pc:x}" [label="{label}", color="{color}"];\n')

        # 控制流：黑实线
        for (src, dst) in cfg_edges:
            f.write(f'  "0x{src:x}" -> "0x{dst:x}" [color="black"];\n')

        # 数据流：蓝虚线
        for (def_pc, use_pc) in dfg_edges:
            f.write(f'  "0x{def_pc:x}" -> "0x{use_pc:x}" [color="blue", style="dashed"];\n')

        f.write("}\n")
    

    print("[+] Done.")


if __name__ == "__main__":
    main()