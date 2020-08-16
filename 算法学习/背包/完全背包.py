""":arg
给定数量不限币值, 25, 10, 5, 1
计算可以得到n分的有多少种方法
f(i, v) 用前i币组成v值有多少种方法
当第i种币为 ci
f(i, v) = f(i-1, v) + f(i - 1, v - ci) + f(i-1, v - 2ci) + ... f(i - 1, v - kci) k是 v//c_i
时间复杂度为 4 * (n + 1) * k
令 v = v - ci
f(i, v - ci) = f(i-1, v-ci) + f(i-1, v-2ci) + ... + f(i-1, v-kci) k是v//ci
得到
f(i, v) = f(i - 1, v) + f(i, v - ci)
"""
import sys
sys.setrecursionlimit(10000000)

def complete_backpack1(n):
    M = 1000000007
    coins = [1, 5, 10, 25]
    dp = [[1] + [0] * (n) for _ in range(len(coins) + 1)]
    for i in range(1, 5):
        for j in range(1, n + 1):
            for k in range(j // coins[i - 1] + 1):
                dp[i][j] += dp[i - 1][j - k * coins[i - 1]]
    return dp[-1][-1] % M


def complete_backpack2(n):
    M = 1000000007
    coins = [1, 5, 10, 25]
    dp = [[1] + [0] * n for _ in range(len(coins) + 1)]
    for i in range(1, 5):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + (dp[i][j - coins[i - 1]] if j - coins[i - 1] >= 0 else 0)
    return dp[-1][-1] % M


def complete_backpack3(n):
    """
    滚动数组
    """
    M = 1000000007
    coins = [1, 5, 10, 25]
    dp = [1] + [0] * n
    for i in range(1, 5):
        nxt = [1] + [0] * n
        for j in range(1, n + 1):
            nxt[j] = dp[j] + (nxt[j - coins[i - 1]] if j - coins[i - 1] >= 0 else 0)
        dp = nxt
    # print(dp)
    return dp[-1] % M


def complete_backpack4(n):
    M = 1000000007
    coins = [1, 5, 10, 25]
    dp = [1] + [0] * n
    for i in range(1, 5):
        for j in range(1, n + 1):
            dp[j] += dp[j - coins[i - 1]] if j - coins[i - 1] >= 0 else 0
    # print(dp)
    return dp[-1] % M


print(complete_backpack4(5))
# print(complete_backpack(10))
print(complete_backpack4(1000000))
