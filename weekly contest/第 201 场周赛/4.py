from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        cuts.sort()

        cache = {}

        def dfs(left, right, cuts):
            # print(left, right)
            if not cuts: return 0
            if (left, right) in cache:
                return cache[(left, right)]
            ans = float("inf")
            for i in range(len(cuts)):
                cur = right - left
                lc = dfs(left, cuts[i], cuts[:i])
                rc = dfs(cuts[i], right, cuts[i + 1:])
                ans = min(ans, cur + lc + rc)
            cache[(left, right)] = ans
            return ans

        res = dfs(0, n, cuts)

        return res

import sys
sys.setrecursionlimit(200000)
a = Solution()
print(a.minCost(n=7, cuts=[1, 3, 4, 5]))
