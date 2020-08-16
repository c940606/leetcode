from typing import List


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        import functools

        @functools.lru_cache(None)
        def dfs(i, s):
            if i == len(hats):
                return 1
            res = 0
            for j in hats[i]:
                cur = 1 << j
                if cur & s == 0:
                    res += dfs(i + 1, cur | s)
            return res % (10 ** 9 + 7)

        return dfs(0, 0)


a = Solution()
print(a.numberWays([[1, 2, 4, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 18, 19, 20, 23, 24, 25], [2, 5, 16],
                    [1, 4, 5, 6, 7, 8, 9, 12, 15, 16, 17, 19, 21, 22, 24, 25],
                    [1, 3, 6, 8, 11, 12, 13, 16, 17, 19, 20, 22, 24, 25], [11, 12, 14, 16, 18, 24],
                    [2, 3, 4, 5, 7, 8, 13, 14, 15, 17, 18, 21, 24], [1, 2, 6, 7, 10, 11, 13, 14, 16, 18, 19, 21, 23],
                    [1, 3, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 18, 20, 21, 22, 23, 24, 25],
                    [2, 3, 4, 6, 7, 10, 12, 14, 15, 16, 17, 21, 22, 23, 24, 25]]))
