class Solution(object):
	def findSubsequences(self, nums):
		"""
		给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
		---
		输入: [4, 6, 7, 7]
		输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
		---
		思路:

		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		res = []
		def helper(nums,temp):
			if len(temp)>1 and temp not in res:
				res.append(temp)
			for i in range(len(nums)):
				if not temp :
					helper(nums[i+1:],temp+[nums[i]])
				elif temp[-1] <= nums[i]:
					helper(nums[i + 1:], temp + [nums[i]])

		helper(nums,[])
		return res
a = Solution()
print(a.findSubsequences([4, 6, 7, 7]))
print(a.findSubsequences([4,3,2,1]))
print(a.findSubsequences([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
