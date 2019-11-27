class Solution:
    def numWays1(self, steps: int, arrLen: int) -> int:
        M = 10 ** 9 + 7
        dp = [0] * (min(steps // + 1, arrLen))
        dp[0] = 1
        for _ in range(steps):
            tmp = dp[:]
            for i in range(len(dp)):
                if i != 0:
                    tmp[i] += dp[i - 1]
                if i != len(dp) - 1:
                    tmp[i] += dp[i + 1]
            dp = tmp
        return dp[0] % M

    def numWays(self, steps: int, arrLen: int) -> int:

        def helper(i, steps):
            if i == 0 and steps == 0:
                return 1
            if i > steps:
                return 0
            return helper(i, steps - 1) + \
                   helper(i + 1, steps - 1) if i + 1 < arrLen else 0 + \
                                                                   helper(i - 1, steps - 1) if i - 1 >= 0 else 0

        return helper(0, steps)


a = Solution()
print(a.numWays(3, 2))
print(a.numWays(2, 4))
print(a.numWays(4, 2))
print(a.numWays(3, 3))
print(a.numWays(27, 7))
print(a.numWays(430, 148488))
print(a.numWays(438, 315977))
print(a.numWays(434, 291270))
print(a.numWays(500, 969997))
