from collections import Counter


class Solution:
	def singleNumber(self, nums):
		"""
		给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素
		:type nums: List[int]
		:rtype: int
		"""
		temp = set(nums)
		return (3*sum(temp) - sum(nums))//2

	def singleNumber1(self, nums):
		count = Counter(nums)
		return (list(count.keys())[list(count.values()).index(1)])
a = Solution()
print(a.singleNumber([2,2,2,3,3,3,4]))
