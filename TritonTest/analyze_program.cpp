#include <triton/api.hpp>
#include <triton/x86Specifications.hpp>

#include <iostream>
#include <fstream>
#include <unordered_map>
#include <vector>

int main(int argc, const char* argv[]) {
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " <raw binary file>" << std::endl;
    return 1;
  }

  const char* filename = argv[1];
  std::ifstream fin(filename, std::ios::binary);
  if (!fin.good()) {
    std::cerr << "Cannot open file: " << filename << std::endl;
    return 1;
  }

  // 读取全部内容
  std::vector<unsigned char> buffer(
      (std::istreambuf_iterator<char>(fin)),
      std::istreambuf_iterator<char>());
  fin.close();

  // 初始化 Triton
  triton::API ctx;
  ctx.setArchitecture(triton::arch::ARCH_X86_64);

  // CFG: 指令地址 -> 分支目标集合
  std::unordered_map<triton::uint64, std::vector<triton::uint64>> CFG;

  triton::uint64 base = 0x400000;              // 虚拟起始地址（假定）
  triton::uint64 pc   = base;
  triton::uint64 end  = base + buffer.size();

  while (pc < end) {
    triton::arch::Instruction inst;
    triton::uint64 offset = pc - base;
    triton::uint32 maxsz  = std::min<triton::uint32>(15, buffer.size() - offset);

    inst.setOpcode(&buffer[offset], maxsz);
    inst.setAddress(pc);

    ctx.processing(inst);
    std::cout << std::hex << pc << ": " << inst.getDisassembly() << std::endl;

    for (auto& r : inst.getReadRegisters())
      std::cout << "   READ  " << r.first << std::endl;
    for (auto& r : inst.getWrittenRegisters())
      std::cout << "   WRITE " << r.first << std::endl;

    // 控制流分析：分支目标记录（兼容 v0.9）
    // 控制流分析：分支目标记录（兼容老版）
    if (inst.isControlFlow()) {
        triton::uint64 nextAddr = inst.getNextAddress();
        CFG[pc].push_back(nextAddr);

        for (auto& op : inst.operands) {
            if (op.getType() == triton::arch::OP_IMM) {
                triton::uint64 target = op.getImmediate().getValue();
                CFG[pc].push_back(target);
            }
        }
    }

    pc += inst.getSize();
  }

  // 输出 CFG dot 文件
  std::ofstream gv("cfg.dot");
  gv << "digraph CFG {\n";
  for (auto& kv : CFG)
    for (auto t : kv.second)
      gv << "  \"" << std::hex << kv.first << "\" -> \"" << t << "\";\n";
  gv << "}\n";
  gv.close();
  std::cout << "[*] CFG exported to cfg.dot\n";

  return 0;
}