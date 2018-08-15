class Solution(object):
	def findLengthOfLCIS(self, nums):
		"""
		给定一个未经排序的整数数组，找到最长且连续的的递增序列。
		---
		输入: [1,3,5,4,7]
		输出: 3
		解释: 最长连续递增序列是 [1,3,5], 长度为3。
		尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
		---
		思路：
		用三个指针：
		一个记录开始位置
		另外两个记录 是否是递增
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		max_len = 0
		if n < 2:
			return n
		i,k,j = 0,0,1
		while j<n:
			while j< n and nums[k]<nums[j]:
				k += 1
				j += 1
			# if j == n and nums[k]<nums[j]:
			# 	k = j
			print(i,k,j)
			max_len = max(max_len,j-i)
			i = j
			k = j
			j += 1
		return max_len
a = Solution()
print(a.findLengthOfLCIS([2,2,2,2,2,2,2,2,2,2]))
