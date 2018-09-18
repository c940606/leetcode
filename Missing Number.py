class Solution(object):
	def missingNumber(self, nums):
		"""
		给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
		---
		输入: [3,0,1]
		输出: 2
		----
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		lookup = list(range(n+1))
		return list(set(lookup) - set(nums))[0]

	def missingNumber1(self, nums):
		n = len(nums)
		lookup = list(range(n + 1))
		return sum(lookup)-sum(nums)
a = Solution()
print(a.missingNumber1([3,0,1]))