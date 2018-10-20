class Solution(object):
	def firstMissingPositive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 1
		lookup = {}
		for num in nums:
			lookup[num] = 1
		for i in range(1,len(nums)+1):
			if i not in lookup:
				return i

	def firstMissingPositive1(self, nums):
		i = 1
		while True:
			if i not in nums:
				return i
			else:
				i += 1
