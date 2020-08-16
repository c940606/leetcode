import sys

import numpy as np

input = sys.stdin.readline
N, weights = map(int, input().split())

# dp = [0] * (weights + 1)
dp = np.zeros(weights + 1, dtype=np.int64)

while N:
    w, v = map(int, input().split())
    np.maximum(dp[:-w] + v, dp[w:], out=dp[w:])
    # for i in range(weights, -1, -1):
    #     if i - w >= 0:
    #         dp[i] = max(dp[i], dp[i - w] + v)
    # print(dp)
    N -= 1
print(dp[-1])
