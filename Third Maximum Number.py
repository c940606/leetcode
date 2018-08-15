class Solution:
	def thirdMax(self, nums):
		"""
		给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
		---
		输入: [3, 2, 1]
		输出: 1
		解释: 第三大的数是 1.
		:type nums: List[int]
		:rtype: int
		"""
		if len(set(nums)) < 3:
			return max(nums)
		return sorted(list(set(nums)), reverse=True)[2]

a = Solution()
# [2, 2, 3, 1]
print(a.thirdMax([2, 2, 3, 1]))
