class Solution:
    def getMoneyAmount1(self, n: int) -> int:
        import functools

        @functools.lru_cache(None)
        def helper(left, right):
            if left + 1 >= right:
                return 0
            res = float("inf")
            for i in range(left, right):
                res = min(res, i + max(helper(left, i), helper(i + 1, right)))
            return res

        return helper(1, n + 1)

    def getMoneyAmount(self, n: int) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        for j in range(2, n + 1):
            for i in range(j - 1, -1, -1):
                res = float("inf")
                for k in range(i+1, j):
                    res = min(res, k + max(dp[(i, k-1)], dp[(k+1, j)]))
                dp[(i, j)] = i if i + 1 == j else res
        return dp[(1, n)]

a = Solution()
print(a.getMoneyAmount(10))
