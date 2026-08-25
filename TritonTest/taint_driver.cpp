#include <triton/api.hpp>
#include <triton/x86Specifications.hpp>

#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>

int main(int argc, const char* argv[]) {
    // 初始化 Triton
    triton::API api;
    api.setArchitecture(triton::arch::ARCH_X86_64);
    api.enableSymbolicEngine(true);
    api.enableTaintEngine(true);
    api.setMode(triton::modes::ALIGNED_MEMORY, true);

    std::vector<uint8_t> code = loadTextSection("spectre_test", text_addr, text_size);

    const triton::uint64 secret_addr = 0x2020e0;
    for (int i = 0; i < 8; i++) {
        triton::arch::MemoryAccess mem(secret_addr + i, 1);
        api.setTaintMemory(mem);
        api.symbolizeMemory(mem, "secret_byte_" + std::to_string(i));
    }

    triton::uint64 pc = text_addr;
    std::set<std::string> forwardTaint;
    std::set<triton::uint64> forwardTaintMemory;
    while (pc < text_addr + text_size) {
        triton::arch::Instruction inst;
        inst.setOpcode(&code[pc - text_addr], getInstSize(code, pc)); // 取一条指令
        inst.setAddress(pc);

        api.processing(inst); // Triton执行符号/污点传播

        // 查询每条指令后的污点状态
        for (auto reg : api.getAllRegisters())
            if (api.isRegisterTainted(reg))
                forwardTaint.insert(reg.getName());

        for (auto& acc : inst.getLoadAccess())
            if (api.isMemoryTainted(acc.first))
                forwardTaintMemory.insert(acc.first);

        for (auto& acc : inst.getStoreAccess())
            if (api.isMemoryTainted(acc.first))
                forwardTaintMemory.insert(acc.first);

        // 控制流前进
        if (inst.isControlFlow()) {
            pc = inst.getNextAddress(); // 简化假定
        } else {
            pc += inst.getSize();
        }
    }

    auto expr = api.getSymbolicRegister(api.getRegister("rax"));
    auto termlist = expr->getChildren();  // 子节点
    visitAST(expr); // 递归收集叶子节点

}