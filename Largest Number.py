from functools import cmp_to_key


class Solution(object):
	def largestNumber(self, nums):
		"""
		给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
		---
		输入: [10,2]
		输出: 210
		---
		输入: [3,30,34,5,9]
		输出: 9534330
		---
		思路:

		:type nums: List[int]
		:rtype: str
		"""
		def jup(x,y):
			if x+y > y+x:
				return -1
			elif x+y < y+x:
				return 1
			elif x+y == y+x:
				return 0
			return 0
		nums = list(map(str,nums))
		nums = sorted(nums,key=cmp_to_key(lambda x,y:jup(x,y)))
		return "".join(nums)
a = Solution()
print(a.largestNumber([3,30,34,5,9]))