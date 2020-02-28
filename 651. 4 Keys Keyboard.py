class Solution:
    def maxA1(self, N: int) -> int:
        from functools import lru_cache

        @lru_cache(None)
        def dfs(N, tmp, select, copy, buffer):
            if N == 0:
                return 0
            # 打印
            tmp1 = 1 + dfs(N - 1, tmp + 1, False, copy, buffer)
            # 全选
            tmp2 = dfs(N - 1, tmp, True, False, tmp)
            # 复制
            tmp3 = 0
            if select:
                tmp3 = dfs(N - 1, tmp, select, True, buffer)
            # 粘贴
            tmp4 = 0
            if copy:
                tmp4 = buffer + dfs(N - 1, buffer + tmp, False, copy, buffer)
            return max(tmp1, tmp2, tmp3, tmp4)

        return dfs(N, 0, False, False, 0)

    def maxA(self, N: int) -> int:

        dp = [i for i in range(N + 1)]

        for i in range(7, N+1):
            for j in range(1, i - 2):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        # print(dp)
        return dp[-1]

a = Solution()
print(a.maxA(7))
print(a.maxA(11))  # 27
print(a.maxA(50))
# AAAAAA
