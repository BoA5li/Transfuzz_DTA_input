import json
import random
import sys

def main(path):
    with open(path, 'r', encoding='utf-8') as f:
        summary = json.load(f)

    backward_objects = set(summary["backward"]["objects"])
    backward_leafs = set(summary["backward"]["leaf_objects"])

    forward_objects = set(summary["forward"]["objects"])
    forward_sinks = set(summary["forward"]["sink_objects"])

    object_details = summary["object_details"]

    errors = []
    warnings = []

    # 基本集合关系检查
    if not backward_leafs.issubset(backward_objects):
        errors.append("backward.leaf_objects 不是 backward.objects 的子集")

    if not forward_sinks.issubset(forward_objects):
        errors.append("forward.sink_objects 不是 forward.objects 的子集")

    # backward leaf 检查
    for obj in sorted(backward_leafs):
        detail = object_details.get(obj)
        if detail is None:
            errors.append(f"backward leaf 缺少 object_details: {obj}")
            continue

        parents = set(detail.get("direct_parents", []))
        parents_in_backward = parents & backward_objects
        if parents_in_backward:
            errors.append(
                f"对象被标为 backward leaf，但仍有 backward 父节点: {obj} <- {sorted(parents_in_backward)}"
            )

    # backward 非 leaf 检查
    for obj in sorted(backward_objects - backward_leafs):
        detail = object_details.get(obj)
        if detail is None:
            errors.append(f"backward object 缺少 object_details: {obj}")
            continue

        parents = set(detail.get("direct_parents", []))
        parents_in_backward = parents & backward_objects
        if not parents_in_backward:
            errors.append(
                f"对象未被标为 backward leaf，但在 backward slice 内没有父节点: {obj}"
            )

    # forward sink 检查
    for obj in sorted(forward_sinks):
        detail = object_details.get(obj)
        if detail is None:
            errors.append(f"forward sink 缺少 object_details: {obj}")
            continue

        children = set(detail.get("direct_children", []))
        children_in_forward = children & forward_objects
        if children_in_forward:
            errors.append(
                f"对象被标为 forward sink，但仍有 forward 子节点: {obj} -> {sorted(children_in_forward)}"
            )

    # forward 非 sink 检查
    for obj in sorted(forward_objects - forward_sinks):
        detail = object_details.get(obj)
        if detail is None:
            errors.append(f"forward object 缺少 object_details: {obj}")
            continue

        children = set(detail.get("direct_children", []))
        children_in_forward = children & forward_objects
        if not children_in_forward:
            errors.append(
                f"对象未被标为 forward sink，但在 forward slice 内没有子节点: {obj}"
            )

    print("==== SUMMARY ====")
    print(f"backward.objects      : {len(backward_objects)}")
    print(f"backward.leaf_objects : {len(backward_leafs)}")
    print(f"forward.objects       : {len(forward_objects)}")
    print(f"forward.sink_objects  : {len(forward_sinks)}")

    print("\n==== ERRORS ====")
    for e in errors:
        print(e)

    print("\n==== WARNINGS ====")
    for w in warnings:
        print(w)

    if not errors:
        print("\n[PASS] 叶子/汇点定义与图结构一致。")
    else:
        print(f"\n[FAIL] 发现 {len(errors)} 个不一致项。")

    # 抽样展示
    print("\n==== SAMPLE BACKWARD LEAFS ====")
    for obj in random.sample(sorted(backward_leafs), min(5, len(backward_leafs))):
        detail = object_details[obj]
        parents = set(detail.get("direct_parents", []))
        parents_in_backward = sorted(parents & backward_objects)
        print(f"{obj}")
        print(f"  direct_parents       = {sorted(parents)}")
        print(f"  parents_in_backward  = {parents_in_backward}")

    print("\n==== SAMPLE FORWARD SINKS ====")
    for obj in random.sample(sorted(forward_sinks), min(5, len(forward_sinks))):
        detail = object_details[obj]
        children = set(detail.get("direct_children", []))
        children_in_forward = sorted(children & forward_objects)
        print(f"{obj}")
        print(f"  direct_children      = {sorted(children)}")
        print(f"  children_in_forward  = {children_in_forward}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python check_leaf_sink_consistency.py dependency_summary.json")
        sys.exit(1)
    main(sys.argv[1])