#include <fcntl.h>      // open, O_RDONLY
#include <unistd.h>     // lseek, close
#include <sys/mman.h>   // mmap, munmap, PROT_READ, MAP_PRIVATE, MAP_FAILED
#include <elf.h>        // Elf64_Ehdr, Elf64_Phdr, PT_LOAD
#include <cstring>      // memcpy, strlen
#include <vector>
#include <iostream>
#include <unordered_set>
#include <stdexcept>

#include <triton/context.hpp>              // ✅ 改成 context.hpp
#include <triton/instruction.hpp>
#include <triton/x86Specifications.hpp>

using namespace triton;
using namespace triton::arch;
using namespace triton::arch::x86;

/* 手动读取 ELF PT_LOAD 段 */
struct Segment {
    uint64_t vaddr;
    std::vector<uint8_t> data;
};

std::vector<Segment> loadElfSegments(const std::string& path, uint64_t& entry) {
    std::vector<Segment> segs;
    int fd = open(path.c_str(), O_RDONLY);
    if (fd < 0) throw std::runtime_error("Cannot open ELF file");
    off_t len = lseek(fd, 0, SEEK_END);
    void* map = mmap(nullptr, len, PROT_READ, MAP_PRIVATE, fd, 0);
    if (map == MAP_FAILED) throw std::runtime_error("mmap failed");

    const Elf64_Ehdr* eh = reinterpret_cast<const Elf64_Ehdr*>(map);
    entry = eh->e_entry;
    const Elf64_Phdr* phdrs = reinterpret_cast<const Elf64_Phdr*>((char*)map + eh->e_phoff);
    for (int i = 0; i < eh->e_phnum; i++) {
        if (phdrs[i].p_type == PT_LOAD && phdrs[i].p_filesz > 0) {
            Segment s;
            s.vaddr = phdrs[i].p_vaddr;
            s.data.resize(phdrs[i].p_filesz);
            memcpy(s.data.data(), (char*)map + phdrs[i].p_offset, phdrs[i].p_filesz);
            segs.push_back(std::move(s));
        }
    }
    munmap(map, len);
    close(fd);
    return segs;
}

int main(int argc, const char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " ./test_elf" << std::endl;
        return 1;
    }

    std::string path = argv[1];
    uint64_t entry = 0;
    auto segs = loadElfSegments(path, entry);

    triton::Context ctx;       // ✅ 改成 Context
    ctx.setArchitecture(ARCH_X86_64);
    std::cout << "[+] Triton initialized." << std::endl;

    // 加载段到 Triton 内存
    for (auto& s : segs)
        ctx.setConcreteMemoryAreaValue(s.vaddr, s.data);

    // 栈
    const uint64_t STACK_ADDR = 0x70000000;
    const size_t  STACK_SIZE  = 0x20000;
    ctx.setConcreteMemoryAreaValue(STACK_ADDR, std::vector<uint8_t>(STACK_SIZE, 0));
    uint64_t rspVal = STACK_ADDR + STACK_SIZE - 0x1000;

    // 模拟 argc, argv, envp
    uint64_t argvAddr = STACK_ADDR + 0x100;
    const char* arg0 = "prog";
    ctx.setConcreteMemoryAreaValue(argvAddr, std::vector<uint8_t>(16, 0));
    for (size_t i = 0; i < strlen(arg0); ++i)
        ctx.setConcreteMemoryValue(argvAddr + i, arg0[i]);

    // 设置寄存器
    ctx.setConcreteRegisterValue(ctx.getRegister(ID_REG_X86_RSP), rspVal);
    ctx.setConcreteRegisterValue(ctx.getRegister(ID_REG_X86_RDI), 1);
    ctx.setConcreteRegisterValue(ctx.getRegister(ID_REG_X86_RSI), argvAddr);
    ctx.setConcreteRegisterValue(ctx.getRegister(ID_REG_X86_RIP), entry);

    std::cout << "[+] Entry point: 0x" << std::hex << entry << std::endl;

    // 分配默认空页，防止访问崩溃
    auto map_guard_page = [&](uint64_t addr) {
        uint64_t base = addr & ~0xFFFULL;
        ctx.setConcreteMemoryAreaValue(base, std::vector<uint8_t>(0x1000, 0));
    };

    // 设置 secret 为 taint + symbolize
    const uint64_t SECRET_ADDR = 0x602120; // 根据 nm 确认
    const size_t SECRET_LEN = 8;
    for (size_t i = 0; i < SECRET_LEN; ++i) {
        auto m = MemoryAccess(SECRET_ADDR + i, 1);
        ctx.taintMemory(m);
        ctx.symbolizeMemory(m, "secret_byte_" + std::to_string(i));
    }
    std::cout << "[+] Secret region tainted & symbolized: 0x"
              << std::hex << SECRET_ADDR << "-"
              << SECRET_ADDR + SECRET_LEN - 1 << std::endl;

    size_t instCount = 0;
    bool done = false;
    auto rip = ctx.getRegister(ID_REG_X86_RIP);

    while (!done) {
        uint64_t pc = static_cast<uint64_t>(ctx.getConcreteRegisterValue(rip));

        // 检查当前 pc 是否落在 ELF 段内
        bool found = false;
        for (auto &s : segs) {
            if (pc >= s.vaddr && pc < s.vaddr + s.data.size()) {
                found = true;
                break;
            }
        }
        if (!found) {
            std::cout << "[!] Invalid RIP 0x" << std::hex << pc << " stop." << std::endl;
            break;
        }

        // 取指
        std::vector<uint8_t> bytes(16);
        for (size_t i = 0; i < bytes.size(); ++i) {
            try {
                bytes[i] = ctx.getConcreteMemoryValue(pc + i);
            }
            catch(...) {
                map_guard_page(pc + i);
                bytes[i] = ctx.getConcreteMemoryValue(pc + i);
            }
        }

        Instruction inst(pc, bytes.data(), bytes.size());
        ctx.disassembly(inst);
        ctx.processing(inst);
        instCount++;

        std::cout << "[" << std::dec << instCount << "] "
                  << std::hex << pc << ": " << inst.getDisassembly() << std::endl;

        auto op = inst.getDisassembly();
        if (op.find("syscall") != std::string::npos) {
            std::cout << "    [~] skip syscall" << std::endl;
            ctx.setConcreteRegisterValue(rip, inst.getNextAddress());
            continue;
        }

        if (op.find("@plt") != std::string::npos) {
            std::cout << "    [~] skip external call" << std::endl;
            ctx.setConcreteRegisterValue(rip, inst.getNextAddress());
            continue;
        }

        // 打印被污染寄存器
        for (auto regId : {ID_REG_X86_RAX, ID_REG_X86_RBX, ID_REG_X86_RCX, ID_REG_X86_RDX}) {
            const auto& reg = ctx.getRegister(regId);
            if (ctx.isRegisterTainted(reg))
                std::cout << "    [!] reg " << reg.getName() << " tainted." << std::endl;
        }

        ctx.setConcreteRegisterValue(rip, inst.getNextAddress());
        if (op.find("ret") != std::string::npos) {
            done = true;
            std::cout << "[+] ret encountered, break." << std::endl;
        }
    }

    std::cout << "[+] Executed " << std::dec << instCount << " instructions." << std::endl;

    // 反向依赖分析
    std::cout << "[+] Reverse dependency slice..." << std::endl;
    for (size_t i = 0; i < SECRET_LEN; ++i) {
        auto symVar = ctx.getSymbolicMemory(SECRET_ADDR + i);
        if (symVar) {
            auto expr = ctx.getSymbolicExpression(symVar->getId());
            auto slice = ctx.sliceExpressions(expr);
            std::cout << "secret_byte_" << i << " slice size = " << slice.size() << std::endl;
        }
    }

    std::cout << "[+] Done.\n";
    return 0;
}