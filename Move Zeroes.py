class Solution(object):
	def moveZeroes(self, nums):
		"""
		给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
		---
		输入: [0,1,0,3,12]
		输出: [1,3,12,0,0]
		---
		思路；

		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		num = nums.count(0)
		while 0 in nums:
			nums.remove(0)
		for i in range(num):
			nums.append(0)

		def moveZeroes1(self, nums):
			n = len(nums)
			i = 0
			j = 0
			while i < n:
				if nums[i] != 0:
					nums[j],nums[i] = nums[i],nums[j]
					j += 1
				i += 1
