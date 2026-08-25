#!/usr/bin/env python3
import json
import sys

with open('_dependency_summary.json', 'r') as f:
    data = json.load(f)

print("=== 验证 1: 检查 0xbba 的指令详情 ===")
inst_0xbba = data.get('instruction_details', {}).get('0xbba')
if inst_0xbba:
    print(f"反汇编: {inst_0xbba.get('disasm')}")
    print(f"语义标签: {inst_0xbba.get('semantic_tags')}")
    print(f"使用对象: {inst_0xbba.get('use_objects')}")
    print(f"地址对象: {inst_0xbba.get('addr_objects')}")
    print(f"控制依赖: {inst_0xbba.get('controlled_by')}")
    print(f"使用污点: {inst_0xbba.get('uses_taint')}")
else:
    print("未找到 0xbba 的指令详情")

print("\n=== 验证 2: 检查 backward slice 中的关键对象 ===")
backward_objs = data.get('backward', {}).get('objects', [])
print(f"Backward 对象总数: {len(backward_objs)}")

key_objects = ['var:array1', 'var:array1_size', 'var:array2', 'var:secret']
for obj in key_objects:
    if obj in backward_objs:
        print(f"✓ 包含 {obj}")
    else:
        print(f"✗ 缺失 {obj}")

print("\n=== 验证 3: 检查 scale 常量（512 或 0x9）===")
scale_found = []
for obj in backward_objs:
    if '0x9' in obj or '512' in obj or '0x200' in obj:
        scale_found.append(obj)

if scale_found:
    print(f"找到 {len(scale_found)} 个 scale 相关对象:")
    for obj in scale_found[:5]:  # 只显 5 个
        print(f"  - {obj}")
else:
    print("未找到 scale 常量（可能使用了其他表示方式）")

print("\n=== 验证 4: Seed 指令 ===")
seed_pcs = data.get('taint_source', {}).get('seed_instruction_pcs', [])
print(f"Seed 指: {seed_pcs}")
if '0xbba' in seed_pcs:
    print("✓ 0xbba 是 seed 指令（瞬态访存）")
if '0xd7b' in seed_pcs:
    print("✓ 0xd7b 是 seed 指令（初始化循环，噪声）")

print("\n=== 验证 5: 统计信息 ===")
stats = data.get('stats', {})
print(f"执行指令数: {stats.get('executed_instructions')}")
print(f"最大调用深度: {stats.get('max_call_depth', 'N/A')}")
print(f"Backward 对象数: {stats.get('backward_object_nodes')}")
print(f"Forward 对象数: {stats.get('forward_object_nodes')}")
