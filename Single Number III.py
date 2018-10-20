class Solution(object):
	def singleNumber(self, nums):
		"""
		给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
		--
		输入: [1,2,1,3,2,5]
		输出: [3,5]
		:type nums: List[int]
		:rtype: List[int]
		"""
		if not nums:
			return []
		res = []
		for num in set(nums):
			if nums.count(num) == 1:
				res.append(num)
		return res

	def singleNumber1(self, nums):
		if not nums:
			return []
		dict = {}
		for num in nums:
			if num in dict:
				dict.pop(num)
			else:
				dict[num] = 1
		return list(dict.keys())

