from typing import List


class Solution(object):
    def largestDivisibleSubset1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        pre = [-1] * n
        max_count = 0
        max_index = 0
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    # dp[i] = max(dp[j] + 1,dp[i])
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        pre[i] = j
            if dp[i] > max_count:
                max_count = dp[i]
                max_index = i

        print(dp)
        print(pre)
        print()
        # max_loc = dp.index(max(dp))
        res = []
        while max_index != -1:
            res.append(nums[max_index])
            max_index = pre[max_index]
        return res

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums: return []
        nums.sort()
        dp = {}
        for num in nums:
            t = [num]
            for k in dp:
                if num % k == 0 and len(dp[k]) + 1 > len(t):
                    t = dp[k] + [num]
            dp[num] = t
        print(dp)
        return max(dp.values(), key=len)


a = Solution()
# print(a.largestDivisibleSubset([1, 2, 3]))
# print(a.largestDivisibleSubset([1,2,4,8]))
print(a.largestDivisibleSubset([1, 2, 3]))
print(a.largestDivisibleSubset([1, 2, 4, 8]))
print(a.largestDivisibleSubset([3, 4, 16, 8]))
