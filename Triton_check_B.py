import json

with open("/root/dependency_summary.json", "r", encoding="utf-8") as f:
    summary = json.load(f)

with open("/root/path_report.json", "r", encoding="utf-8") as f:
    report = json.load(f)

seed_nodes = set(summary["taint_source"]["seed_object_nodes"])
backward_nodes = set(summary["backward"]["objects"])
forward_nodes = set(summary["forward"]["objects"])
leaf_objects = set(summary["backward"]["leaf_objects"])
sink_objects = set(summary["forward"]["sink_objects"])

errors = []
warnings = []

# 1. summary/path_report 计数一致性
if summary["path_report_overview"]["backward_target_count"] != len(report.get("backward_paths", [])):
    errors.append("backward_target_count 与 path_report.backward_paths 数量不一致")

if summary["path_report_overview"]["forward_target_count"] != len(report.get("forward_paths", [])):
    errors.append("forward_target_count 与 path_report.forward_paths 数量不一致")

# 2. backward 检查
for item in report.get("backward_paths", []):
    target = item["target"]

    if target not in leaf_objects:
        errors.append(f"[backward] target 不在 leaf_objects 中: {target}")

    paths = item.get("paths", [])
    if not paths:
        warnings.append(f"[backward] target 有记录但 paths 为空: {target}")

    for idx, p in enumerate(paths, 1):
        nodes = p.get("nodes", [])
        labels = p.get("labels", [])
        steps = p.get("steps", [])

        if not nodes:
            errors.append(f"[backward] {target} path#{idx} nodes 为空")
            continue

        if nodes[0] != target:
            errors.append(f"[backward] {target} path#{idx} 起点不是 target: {nodes[0]}")

        if nodes[-1] not in seed_nodes:
            errors.append(f"[backward] {target} path#{idx} 终点不是 seed: {nodes[-1]}")

        if len(labels) != len(nodes):
            errors.append(f"[backward] {target} path#{idx} labels/nodes 长度不一致")

        if len(steps) != max(0, len(nodes) - 1):
            errors.append(f"[backward] {target} path#{idx} steps/nodes 长度不一致")

        for n in nodes:
            if n not in backward_nodes and n not in seed_nodes:
                errors.append(f"[backward] {target} path#{idx} 节点不在 backward 集合中: {n}")

        for i, s in enumerate(steps):
            if i + 1 >= len(nodes):
                errors.append(f"[backward] {target} path#{idx} step 索引越界")
                continue

            if s.get("src") != nodes[i]:
                errors.append(f"[backward] {target} path#{idx} step#{i} src 不匹配")
            if s.get("dst") != nodes[i+1]:
                errors.append(f"[backward] {target} path#{idx} step#{i} dst 不匹配")
            if not s.get("kinds"):
                errors.append(f"[backward] {target} path#{idx} step#{i} 没有 kinds")
            if int(s.get("count", 0)) <= 0:
                errors.append(f"[backward] {target} path#{idx} step#{i} count<=0")

# 3. forward 检查
for item in report.get("forward_paths", []):
    target = item["target"]

    if target not in sink_objects:
        errors.append(f"[forward] target 不在 sink_objects 中: {target}")

    paths = item.get("paths", [])
    if not paths:
        warnings.append(f"[forward] target 有记录但 paths 为空: {target}")

    for idx, p in enumerate(paths, 1):
        nodes = p.get("nodes", [])
        labels = p.get("labels", [])
        steps = p.get("steps", [])

        if not nodes:
            errors.append(f"[forward] {target} path#{idx} nodes 为空")
            continue

        if nodes[0] not in seed_nodes:
            errors.append(f"[forward] {target} path#{idx} 起点不是 seed: {nodes[0]}")

        if nodes[-1] != target:
            errors.append(f"[forward] {target} path#{idx} 终点不是 target: {nodes[-1]}")

        if len(labels) != len(nodes):
            errors.append(f"[forward] {target} path#{idx} labels/nodes 长度不一致")

        if len(steps) != max(0, len(nodes) - 1):
            errors.append(f"[forward] {target} path#{idx} steps/nodes 长度不一致")

        for n in nodes:
            if n not in forward_nodes and n not in seed_nodes:
                errors.append(f"[forward] {target} path#{idx} 节点不在 forward 集合中: {n}")

        for i, s in enumerate(steps):
            if i + 1 >= len(nodes):
                errors.append(f"[forward] {target} path#{idx} step 索引越界")
                continue

            if s.get("src") != nodes[i]:
                errors.append(f"[forward] {target} path#{idx} step#{i} src 不匹配")
            if s.get("dst") != nodes[i+1]:
                errors.append(f"[forward] {target} path#{idx} step#{i} dst 不匹配")
            if not s.get("kinds"):
                errors.append(f"[forward] {target} path#{idx} step#{i} 没有 kinds")
            if int(s.get("count", 0)) <= 0:
                errors.append(f"[forward] {target} path#{idx} step#{i} count<=0")

print("==== ERRORS ====")
for e in errors:
    print(e)

print("\n==== WARNINGS ====")
for w in warnings:
    print(w)

if not errors:
    print("\n[PASS] 路径方向与 reachable 集合的一致性检查通过")