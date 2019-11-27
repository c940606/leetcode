from functools import lru_cache


class Solution(object):
    def integerBreak2(self, n):
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

    def integerBreak(self, n):
        res = 0
        num = []

        def helper(n, tmp, t):
            nonlocal res, num
            if n == 0:
                if res < tmp:
                    res = max(tmp, res)
                    num = t
                return
            for i in range(1, n + 1):
                helper(n - i, tmp * i, t + [i])

        helper(n, 1, [])

        return num
        # if n == 2: return 1
        # if n == 3: return 3
        # if n == 4: return 4
        # if n % 3 == 0: return 3 ** (n // 3)
        # if n % 3 == 1: return 4 * 3 ** ((n - 4) // 3)
        # if n % 3 == 2: return 2 * 3 ** ((n - 2) // 3)

    @lru_cache(None)
    def integerBreak6(self, n):
        return max(i * max(self.integerBreak(n - i), n - i) for i in range(1, n)) if n != 1 else 1
        # res = 0
        # for i in range(1, n):
        #     res = max(res, i * max(self.integerBreak(n - i), n - i))
        # return res


a = Solution()
# print(a.integerBreak(58))
for i in range(2, 21):
    print(i, a.integerBreak(i))
