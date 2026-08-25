#include <stdio.h>
#include <stdlib.h>
#include <string.h>

volatile int sink = 0;

void baseline_mode(long iters) {
    // 尽量避免分支误预测：让分支保持稳定模式
    int sum = 0;
    for (long i = 0; i < iters; i++) {
        // 总是 taken 或总是 not-taken
        if (1) {
            sum += 1;
        } else {
            sum += 2;
        }
    }
    sink = sum;
}

void mispredict_mode(long iters) {
    // 构造模式：先高度偏向一侧，然后反转
    int sum = 0;
    long train_iters = iters * 9 / 10; // 90% 训练
    for (long i = 0; i < iters; i++) {
        if (i < train_iters) {
            // 让预测器学习“if 为真”
            sum += 1;
        } else {
            // 最后 10% 的迭代，改变分支方向，期望产生误预测
            sum += (i & 1) ? 2 : 3;
        }
    }
    sink = sum;
}

int main(int argc, char** argv) {
    const char* mode = "baseline";
    long iters = 100000000; // 根据机器速度调整

    for (int i = 1; i < argc; i++) {
        if (strcmp(argv[i], "--mode=baseline") == 0) {
            mode = "baseline";
        } else if (strcmp(argv[i], "--mode=test") == 0) {
            mode = "test";
        } else if (strncmp(argv[i], "--iters=", 8) == 0) {
            iters = atol(argv[i] + 8);
        }
    }

    if (strcmp(mode, "baseline") == 0) {
        baseline_mode(iters);
    } else {
        mispredict_mode(iters);
    }

    // 防止被优化掉
    printf("sink=%d\n", sink);
    return 0;
}