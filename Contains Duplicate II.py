class Solution(object):
	def containsNearbyDuplicate(self, nums, k):
		"""
		给定一个整数数组和一个整数 k，
		判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
		---
		输入: nums = [1,2,3,1], k = 3
		输出: true
		---
		输入: nums = [1,0,1,1], k = 1
		输出: true
		---
		输入: nums = [1,2,3,1,2,3], k = 2
		输出: false
		---
		思路:

		:type nums: List[int]
		:type k: int
		:rtype: bool
		"""
		lookup = {}
		for idx,num in enumerate(nums):
			if num not in lookup:
				lookup[num] = idx
			else:
				if idx - lookup[num] <= k:
					return True
				else:
					lookup[num] = idx
		return False


a = Solution()
print(a.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))
print(a.containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
