from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        from functools import lru_cache
        lookup = {}

        def dfs(i):
            res = 1
            if i in lookup:
                return lookup[i]
            for j in range(1, d + 1):
                if i + j < n:
                    if arr[i] <= arr[i + j]: break
                    res = max(res, 1 + dfs(i + j))
            for k in range(1, d + 1):
                if i - k >= 0:
                    if arr[i] <= arr[i - k]: break
                    res = max(res, 1 + dfs(i - k))
            lookup[i] = res
            return res

        n = len(arr)
        res = 1

        for i in range(len(arr)):
            res = max(res, dfs(i))
        return res


a = Solution()
print(a.maxJumps(arr=[1, 2, 5, 4], d=1))
print(a.maxJumps(arr=[6, 4, 14, 6, 8, 13, 9, 7, 10, 6, 12], d=2))
