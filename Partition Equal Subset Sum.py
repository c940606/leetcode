class Solution(object):
	def canPartition(self, nums):
		"""
		给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
		注意:
		每个数组中的元素不会超过 100
		数组的大小不会超过 200
		---
		输入: [1, 5, 11, 5]
		输出: true
		解释: 数组可以分割成 [1, 5, 5] 和 [11].
		---
		输入: [1, 2, 3, 5]
		输出: false
		解释: 数组不能分割成两个元素和相等的子集.
		---
		思路:
		动态规划
		1. 排序(从小到大)
		2. 从末最后一个分割集合
			1. 分割点满足前后集合相等 return
			2. 后集合大 直接退出
			3. 前集合大 分割点向前
		:type nums: List[int]
		:rtype: bool
		"""
		if not nums:
			return False
		n = len(nums)
		nums.sort()
		front_sum = sum(nums)
		last_sum = 0
		i = n-1
		while i>0:
			front_sum -= nums[i]
			last_sum += nums[i]
			if front_sum == last_sum:
				print(nums,i)
				return True
			elif front_sum > last_sum:
				i -= 1
			elif front_sum < last_sum:
				return False
		return False
a = Solution()
print(a.canPartition([1,2,3,4,5,6,7]))

