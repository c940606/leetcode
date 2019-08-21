import functools
import sys

sys.setrecursionlimit(1000000)


class Solution:
    @functools.lru_cache(None)
    def numRollsToTarget1(self, d: int, f: int, target: int) -> int:
        if d == 0 and target == 0:
            return 1
        if d * f < target:
            return 0
        if target < 0:
            return 0
        res = 0
        for i in range(1, f + 1):
            # print(target - f)
            if target - i >= 0:
                res += self.numRollsToTarget(d - 1, f, target - i)
            else:
                # print("dafd")
                break
        return res % (10 ** 9 + 7)

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        # print(dp)
        dp[0][0] = 1
        M = 10 ** 9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                if j > i * f: continue
                for k in range(1, f + 1):
                    if k <= j:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % M
                    else:
                        break
        # print(dp)
        return dp[d][target]


a = Solution()
print(a.numRollsToTarget(1, 6, 3))
print(a.numRollsToTarget(2, 6, 7))
print(a.numRollsToTarget(30, 30, 500))
print(a.numRollsToTarget(10, 29, 601))
print(a.numRollsToTarget(10, 11, 587))
