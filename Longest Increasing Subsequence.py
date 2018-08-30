class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		给定一个无序的整数数组，找到其中最长上升子序列的长度。
		---
		输入: [10,9,2,5,3,7,101,18]
		输出: 4
		解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
		---
		思路：

		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		res = [1]*n
		for i in range(n):
			for j in range(i):
				if nums[j] < nums[i] and res[j]+1 >=res[i]:
					res[i] = res[j] + 1
		return max(res)
a = Solution()
print(a.lengthOfLIS([10,9,2,5,3,7,101,18]))
