class Solution(object):
	def summaryRanges(self, nums):
		"""
		给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
		---
		输入: [0,1,2,4,5,7]
		输出: ["0->2","4->5","7"]
		解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
		---
		思路:
		可以用flag
		:type nums: List[int]
		:rtype: List[str]
		"""
		if not nums:
			return []
		res = []
		n = len(nums)
		i = 0
		while i < n:
			beg = i
			while i< n-1 and nums[i+1]-nums[i]==1:
				i += 1
			last = i
			i += 1
			if beg == last:
				res.append(str(nums[beg]))
			else:
				res.append(str(nums[beg])+"->"+str(nums[last]))
		return res
a = Solution()
print(a.summaryRanges([0,2,3,4,6,8,9]))




