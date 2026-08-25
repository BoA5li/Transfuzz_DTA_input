#!/usr/bin/env python3
import json
from collections import Counter

with open('array2_terminal_mapping.json', 'r') as f:
    data = json.load(f)

backward = data.get('backward_leaf_mappings') or data.get('backward_mappings') or []
forward = data.get('forward_sink_mappings') or data.get('forward_mappings') or []

print("=== 映射器输出统计 ===")
print("Backward leaf 映射数: " + str(len(backward)))
print("Forward sink 映射数: " + str(len(forward)))
print("JSON 顶层 keys: " + str(list(data.keys())))

print("")
#print("=== 关键攻击对象映射
 ===")
key_objects = ['var:array2', 'var:array1', 'var:array1_size', 'var:secret']
all_mappings = backward + forward

for obj_id in key_objects:
    found = [m for m in all_mappings if m.get('object_id') == obj_id]
    if found:
        m = found[0]
        print("")
        print("OK " + obj_id)
        print("  Role: " + str(m.get('role', 'N/A')))
        print("  Mapping kind: " + str(m.get('mapping_kind', 'N/A')))
        print("  Confidence: " + str(m.get('confidence', 'N/A')))
        print("  Candidate elements: " + str(m.get('candidate_program_elements', [])))
        
        src_ev = m.get('source_evidence', [])
        if not src_ev:
            exec_ref = m.get('executed_code_reference', {})
            if isinstance(exec_ref, dict):
                src_ev = exec_ref.get('source_evidence', [])
        
        if src_ev:
            print("  Source evidence count: " + str(len(src_ev)))
            for src in src_ev[:2]:
                fn = src.get('function', 'N/A')
                fl = src.get('file', 'N/A')
                ln = src.get('line', 'N/A')
                print("    - " + str(fl) + ":" + str(ln) + " (func: " + str(fn) + ")")
        else:
            print("  Source evidence: none")
        
        anchor_pcs = m.get('anchor_pcs', [])
        print("  Anchor PCs: " + str(anchor_pcs[:5]))
    else:
        print("")
        print("MISS " + obj_id + " not found")

print("")
print("=== Mappings containing 0xbba ===")
for m in all_mappings:
    anchor_pcs = m.get('anchor_pcs', [])
    all_pcs = m.get('all_mapped_pcs', [])
    direct_use = m.get('direct_use_pcs', [])
    if '0xbba' in anchor_pcs or '0xbba' in all_pcs or '0xbba' in direct_use:
        print("Object: " + str(m.get('object_id')))
        print("  Role: " + str(m.get('role')))
        print("  Anchor PCs: " + str(anchor_pcs[:5]))

print("")
print("=== Mappings containing array1_size ===")
for m in all_mappings:
    obj_id = m.get('object_id', '')
    if 'array1_size' in obj_id:
        print("Object: " + obj_id)
        print("  Role: " + str(m.get('role')))
        print("  Mapping kind: " + str(m.get('mapping_kind')))
        print("  Anchor PCs: " + str(m.get('anchor_pcs', [])[:5]))

print("")
print("=== Mapping kind distribution ===")
kinds = Counter(m.get('mapping_kind', 'unknown') for m in all_mappings)
for kind, count in kinds.most_common():
    print("  " + str(kind) + ": " + str(count))

print("")
print("=== Role distribution ===")
roles = Counter(m.get('role', 'unknown') for m in all_mappings)
for role, count in roles.most_common():
    print("  " + str(role) + ": " + str(count))
