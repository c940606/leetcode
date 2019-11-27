class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        left = 1
        right = m * n + 1

        def helper(mid):
            c = 0
            for i in range(1, m + 1):
                c += min(mid // i, n)
            return c

        while left < right:
            mid = left + (right - left) // 2
            if helper(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

a = Solution()
print(a.findKthNumber(2, 3, 6))
