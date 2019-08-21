class Solution:
    def minHeightShelves1(self, books, shelf_width: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)
        # dp[i] 表示 i 最小高度
        dp[0] = 0
        for i in range(1, n + 1):
            w = books[i - 1][0]
            h = books[i - 1][1]
            dp[i] = dp[i - 1] + h
            for j in range(i - 1, 0, -1):
                w += books[j - 1][0]
                h = max(h, books[j - 1][1])
                if w > shelf_width: break
                dp[i] = min(dp[i], dp[j - 1] + h)
        return dp[-1]

    def minHeightShelves(self, books, shelf_width: int) -> int:
        import functools
        n = len(books)
        @functools.lru_cache(None)
        def helper(i):
            if i == n: return 0
            w, res, h = 0, float("inf"), 0
            for j in range(i, n):
                if w + books[j][0] <= shelf_width:
                    w += books[j][0]
                    h = max(h, books[j][1])
                    res = min(res, h + helper(j + 1))
                else:
                    break
            return res

        return helper(0)


a = Solution()
print(a.minHeightShelves([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4))
