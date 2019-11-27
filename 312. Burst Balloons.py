from functools import lru_cache
from typing import List


class Solution:
    def maxCoins3(self, nums):

        def helper(nums):
            # print(nums)
            if not nums: return 0
            if len(nums) == 1:
                return nums[0]
            res = 0
            for i in range(len(nums)):
                if i == 0:
                    res = max(res, nums[i] * nums[i + 1] + helper(nums[i + 1:]))
                elif i == len(nums) - 1:
                    res = max(res, nums[i] * nums[i - 1] + helper(nums[:i]))
                else:
                    res = max(res, nums[i - 1] * nums[i] * nums[i + 1] + helper(nums[:i] + nums[i + 1:]))
            return res

        return helper(nums)

    def maxCoins1(self, nums):
        nums = [1] + nums + [1]

        @lru_cache(None)
        def helper(left, right):
            if left + 1 == right:
                return 0
            res = 0
            for i in range(left + 1, right):
                res = max(res, nums[left] * nums[i] * nums[right] + helper(left, i) + helper(i, right))
            return res

        return helper(0, len(nums) - 1)

    def maxCoins2(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for k in range(2, n):
            for i in range(n - k):
                j = i + k
                for t in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[t] * nums[j] + dp[i][t] + dp[t][j])
        return dp[0][n - 1]

    def maxCoins(self, nums: List[int]) -> int:
        pass







a = Solution()
print(a.maxCoins3([3, 1, 5, 8]))
print(a.maxCoins2([1,2,3,4,5,6,7,8,9,10,11]))
print(a.maxCoins3([1,2,3,4,5,6,7,8,9,10,11]))

# print(a.maxCoins3([8, 2, 6, 8, 9, 8, 1, 4, 1, 5, 3, 0, 7, 7, 0, 4, 2, 2]))
