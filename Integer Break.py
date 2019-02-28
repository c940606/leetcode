class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2: return 1
        if n == 3: return 2
        lookup = {4, 3, 2}
        res = 1
        while n:
            while n - 4 > 0:
                n -= 3
                res *= 3
            if n in lookup:
                res *= n
                n -= n
        return res

    def integerBreak1(self, n):
        dp = [1] * (n + 1)
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j, dp[j]) * max(dp[i - j], i - j))
        return dp[n]


a = Solution()
print(a.integerBreak1(13))
