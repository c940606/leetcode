from typing import List


class Solution:
    def wiggleMaxLength1(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [[1] * 2 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i][1] = max(dp[i][1], dp[j][0] + 1)
                elif nums[j] > nums[i]:
                    dp[i][0] = max(dp[i][0], dp[j][1] + 1)
        return max(dp[-1])

    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [[1] * 2 for _ in range(n)]
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                dp[i][1] = dp[i - 1][0] + 1
                dp[i][0] = dp[i - 1][0]
            elif nums[i - 1] > nums[i]:
                dp[i][0] = dp[i - 1][1] + 1
                dp[i][1] = dp[i - 1][1]
            else:
                dp[i][0] = dp[i - 1][0]
                dp[i][1] = dp[i - 1][1]
        # print(dp)
        return max(dp[-1])


a = Solution()
print(a.wiggleMaxLength([1, 7, 4, 9, 2, 5]))
print(a.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))

print(a.wiggleMaxLength([1, 9]))
print(a.wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(a.wiggleMaxLength([0, 0]))
