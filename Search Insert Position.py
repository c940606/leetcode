class Solution:
	def searchInsert(self, nums, target):
		"""
		给定一个排序数组和一个目标值，在数组中找到目标值，
		并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
		-------
		输入: [1,3,5,6], 5
		输出: 2
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		i = 0
		while i < len(nums) and target > nums[i]:
				i += 1
		return i
a = Solution()
print(a.searchInsert([1,3,5,6],7))

