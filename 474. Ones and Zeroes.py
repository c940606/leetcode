from typing import List


class Solution:
    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        import functools

        @functools.lru_cache(None)
        def dfs(i, m, n):
            if i == len(strs):
                return 0
            res = 0
            ones = strs[i].count("1")
            zeros = strs[i].count("0")
            if ones <= n and zeros <= m:
                res = 1 + dfs(i + 1, m - zeros, n - ones)
            res = max(res, dfs(i + 1, m, n))
            return res

        return dfs(0, m, n)

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]

        for i in range(1, len(strs) + 1):
            ones = strs[i - 1].count("1")
            zeros = strs[i - 1].count("0")
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i][j][k] = dp[i - 1][j][k]
                    if j >= zeros and k >= ones and dp[i][j][k] < dp[i - 1][j - zeros][k - ones] + 1:
                        dp[i][j][k] = dp[i - 1][j - zeros][k - ones] + 1
        return dp[-1][-1][-1]


a = Solution()
print(a.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3))
print(a.findMaxForm(["10", "0", "1"], m=1, n=1))
