class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        # if m > n:
        #     m -= n
        dp = [i for i in range(n)]
        i = 0
        while len(dp) > 1:
            div, mod = divmod(i + m, len(dp))
            # print(dp, mod)

            if mod == 0:
                dp.pop()
                i = 0
            else:
                dp.pop(mod - 1)
                i = mod - 1
        return dp[0]
a = Solution()
print(a.lastRemaining(77781, 92332))