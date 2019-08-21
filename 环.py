# 一个环有10个节点, 编号0 ~ 9, 从0点出发,走N步又能回到0点,共有多种走法
import functools
import sys

sys.setrecursionlimit(1000000)


# 自底向上
def helper1(N):
    # dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for j in range(10):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][(j + 1) % 10]
    return dp[N][0]


# 自顶向下
@functools.lru_cache(None)
def helper2(i, N):
    if N == 0:
        if i == 0:
            return 1
        else:
            return 0
    res = 0
    res += helper2((i - 1) % 10, N - 1) + helper2((i + 1) % 10, N - 1)
    return res


print(helper1(1022))
print(helper2(0, 1022))
