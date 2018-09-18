from collections import Counter


class Solution:
	def singleNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		count = Counter(nums)
		return (list(count.keys())[list(count.values()).index(1)])

	def singleNumber1(self, nums):
		return sum(set(nums)) * 2 - sum(nums)
a  = Solution()
a.singleNumber([2,2,1])