# 一堆物品, 有重量 W = {w1, w2, w3..., wn}, 有价值 V = {v1, v2, v3, ... vn}
# 有一个背包可以容下C重量的背包


class Solution:
    # 带记忆搜索
    # def knapsack01(self, W, V, C):
    #     # 位置和大小 定义状态
    #     import functools
    #     n = len(W)
    #     @functools.lru_cache(None)
    #     def helper(idx, c):
    #         if idx >= n:
    #             return 0
    #         res = helper(idx + 1, c)
    #         if c >= W[idx]:
    #             res = max(res, V[idx] + helper(idx + 1, c - W[idx]))
    #         return res
    #     return helper(0, C)

    def knapsack01(self, W, V, C):
        n = len(W)
        dp = [[0] * (C + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for c in range(1, C + 1):
                dp[i][c] = dp[i - 1][c]
                if c - W[i - 1] >= 0:
                    dp[i][c] = max(dp[i][c], V[i - 1] +
                                   dp[i - 1][c - W[i - 1]])
        # print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    a = Solution()
    W = [2, 3, 2]
    V = [1, 2, 3]
    C = 6
    print(a.knapsack01(W, V, C))
