class Solution(object):
	def findMaxConsecutiveOnes(self, nums):
		"""
		给定一个二进制数组， 计算其中最大连续1的个数。
		---
		输入: [1,1,0,1,1,1]
		输出: 3
		解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		max_num = 0
		n = len(nums)
		i = 0
		while i < n:
			temp = 0
			while i < n and nums[i] == 1:
				i += 1
				temp += 1
			if temp > max_num:
				max_num = temp
			i += 1
		return max_num
a = Solution()
print(a.findMaxConsecutiveOnes([1,1,0,1,1,1]))
