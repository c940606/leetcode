class Solution(object):
	def longestConsecutive(self, nums):
		"""
		给定一个未排序的整数数组，找出最长连续序列的长度。
		要求算法的时间复杂度为 O(n)。
		---
		输入: [100, 4, 200, 1, 3, 2]
		输出: 4
		解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
		:type nums: List[int]
		:rtype: int
		"""
		nums = set(nums)
		res = 0
		for num in nums:
			if num -1 not in nums:
				# print(num)
				y = num + 1
				while y in nums:
					y += 1
				res = max(res,y-num)
		return res
a = Solution()
print(a.longestConsecutive([100, 4, 200, 1, 3, 2]))
