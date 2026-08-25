import subprocess
import statistics
import os
from typing import List, Dict, Tuple

# 你可以在这里配置想要测的事件
PMU_EVENTS = [
    "branches",
    "branch-misses",
    "br_inst_retired.all_branches",
    "br_misp_retired.all_branches",
    "int_misc.recovery_cycles_any",
    "machine_clears.count",
    "machine_clears.memory_ordering",
    "machine_clears.smc",
]

TEST_BINARY = "./test"
SOURCE_FILE = "branch_test.c"

def compile_test_program():
    if not os.path.exists(TEST_BINARY):
        print(f"Compiling {SOURCE_FILE} -> {TEST_BINARY}")
        cmd = ["gcc", "-o", TEST_BINARY, SOURCE_FILE]
        subprocess.check_call(cmd)
    else:
        print(f"{TEST_BINARY} already exists, skip compilation.")

def run_perf(events: List[str], mode: str, iters: int = 100_000_000) -> Dict[str, int]:
    """
    使用 perf stat 运行一次程序，返回每个事件的计数值。
    使用 CSV 输出格式 (-x,) 便于解析。
    """
    events_str = ",".join(events)
    cmd = [
        "perf", "stat",
        "-x", ",",  # CSV 格式，字段用逗号分隔
        "-e", events_str,
        TEST_BINARY,
        f"--mode={mode}",
        f"--iters={iters}",
    ]

    # perf 将统计信息输出到 stderr
    print("Running:", " ".join(cmd))
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    out, err = proc.communicate()

    if proc.returncode != 0:
        print("Program output:", out)
        print("perf error output:", err)
        raise RuntimeError(f"perf stat failed with code {proc.returncode}")

    # 解析 perf 的 CSV 输出
    # 通常格式类似：  <count>,<unit>,<event>,<run>,<metric>
    results: Dict[str, int] = {}
    for line in err.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(",")
        if len(parts) < 3:
            continue
        count_str, _unit, event_name = parts[:3]
        event_name = event_name.strip()

        # 只解析我们关注的事件
        if event_name not in events:
            continue

        # 有的计数可能是 "<not supported>" 或 "<not counted>" 等
        try:
            count = int(count_str)
        except ValueError:
            # 可以根据需要记录为 None 或 0
            count = 0
        results[event_name] = count

    return results

def run_experiments(
    events: List[str],
    iters: int = 50_000_000,
    repeats: int = 5
) -> Tuple[List[Dict[str, int]], List[Dict[str, int]]]:
    """
    多次运行 baseline 和 test 模式，返回两个列表：
    baseline_results, test_results
    每个元素是 {event_name: count}
    """
    baseline_results = []
    test_results = []

    print("=== Baseline mode ===")
    for i in range(repeats):
        print(f"Baseline run {i+1}/{repeats}")
        res = run_perf(events, mode="baseline", iters=iters)
        baseline_results.append(res)

    print("=== Test (mispredict) mode ===")
    for i in range(repeats):
        print(f"Test run {i+1}/{repeats}")
        res = run_perf(events, mode="test", iters=iters)
        test_results.append(res)

    return baseline_results, test_results

def summarize(results: List[Dict[str, int]], events: List[str]) -> Dict[str, Dict[str, float]]:
    """
    对多次实验的结果做统计，返回:
    { event_name: { 'mean': x, 'stdev': y } }
    """
    summary: Dict[str, Dict[str, float]] = {}
    for ev in events:
        values = [r.get(ev, 0) for r in results]
        mean = statistics.mean(values) if values else 0.0
        stdev = statistics.pstdev(values) if len(values) > 1 else 0.0
        summary[ev] = {
            "mean": mean,
            "stdev": stdev,
        }
    return summary

def print_summary_table(
    baseline_summary: Dict[str, Dict[str, float]],
    test_summary: Dict[str, Dict[str, float]],
    events: List[str]
):
    print("\n=== Summary (mean ± stdev) ===")
    header = f"{'Event':35s} {'Baseline':25s} {'Test':25s} {'Test/Baseline':>15s}"
    print(header)
    print("-" * len(header))
    for ev in events:
        b = baseline_summary[ev]
        t = test_summary[ev]
        ratio = (t["mean"] / b["mean"]) if b["mean"] > 0 else float('inf')
        print(f"{ev:35s} "
              f"{b['mean']:.2f} ± {b['stdev']:.2f}".ljust(25),
              f"{t['mean']:.2f} ± {t['stdev']:.2f}".ljust(25),
              f"{ratio:15.2f}")

if __name__ == "__main__":
    # 1. 编译测试程序（如需要）
    compile_test_program()

    # 2. 运行实验
    baseline_results, test_results = run_experiments(
        PMU_EVENTS,
        iters=50_000_000,   # 可调整，使每次运行时间在 0.5~2 秒左右
        repeats=5
    )

    # 3. 统计分析
    baseline_summary = summarize(baseline_results, PMU_EVENTS)
    test_summary = summarize(test_results, PMU_EVENTS)

    # 4. 打印结果表
    print_summary_table(baseline_summary, test_summary, PMU_EVENTS)