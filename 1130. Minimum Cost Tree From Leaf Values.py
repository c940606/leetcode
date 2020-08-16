from typing import List


class Solution:
    def mctFromLeafValues1(self, arr: List[int]) -> int:
        import functools

        @functools.lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            res = float("inf")
            for k in range(i, j):
                res = min(res, dfs(i, k) + dfs(k + 1, j) + max(arr[i:k + 1]) * max(arr[k + 1:j + 1]))
            return res

        return dfs(0, len(arr) - 1)

    def mctFromLeafValues(self, arr: List[int]) -> int:

        stack = [float("inf")]
        res = 0
        for a in arr:
            while stack[-1] < a:
                res += stack.pop() * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res

a = Solution()
print(a.mctFromLeafValues([6, 15, 5, 2]))
print(a.mctFromLeafValues([6, 2, 4]))
print(a.mctFromLeafValues([3, 7, 2, 12, 15, 10, 3, 9]))
print(a.mctFromLeafValues([6, 8, 5, 3, 8, 4, 14, 14, 4, 11, 11]))
print(a.mctFromLeafValues([3, 15, 11, 9, 11, 10, 7, 8, 2, 1, 11, 6, 8, 5, 13, 1, 5, 2, 5, 12, 1, 12, 10, 7]))
