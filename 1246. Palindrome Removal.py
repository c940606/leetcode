from typing import List


class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        from functools import lru_cache
        @lru_cache(None)
        def helper(i, j):
            print(i, j)
            if i > j:
                return 0
            if i == j:
                return 1
            if j - i == 1 and arr[i] == arr[j]:
                return 1
            if j - i == 1 and arr[i] != arr[j]:
                return 2
            res = float("inf")
            if arr[i] == arr[j]:
                res = min(res, helper(i + 1, j - 1))
            else:
                for k in range(i, j):
                    print(k, i, j)
                    res = min(res, helper(i, k) + helper(k + 1, j))

            return res

        return helper(0, len(arr) - 1)


a = Solution()
# print(a.minimumMoves([1, 2]))
print(a.minimumMoves([1,3,4,1,5]))
