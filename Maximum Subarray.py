class Solution:
	def maxSubArray(self, nums):
		"""
		给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
		---
		输入: [-2,1,-3,4,-1,2,1,-5,4],
		输出: 6
		解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		Sum = [nums[0] for i in range(n)]
		for i in range(1,n):
			Sum[i] = max(Sum[i-1]+nums[i],nums[i])
		return max(Sum)
nums = [-2,1,-3,4,-1,2,1,-5,4]
a = Solution()
print(a.maxSubArray(nums))

