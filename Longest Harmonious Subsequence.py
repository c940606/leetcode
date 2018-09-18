from collections import Counter


class Solution(object):
	def findLHS(self, nums):
		"""
		和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
		现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
		--
		输入: [1,3,2,2,5,2,3,7]
		输出: 5
		原因: 最长的和谐数组是：[3,2,2,2,3].
		---
		思路:
		1. 想把两个数相减为一组合找到
			排序 后一个减前一个
		2.找长度最长的
		3.顺序
		:type nums: List[int]
		:rtype: int
		"""
		sub_one = []
		c = Counter(nums)
		sorted_nums = sorted(list(set(nums)))
		n = len(sorted_nums)
		for i in range(n-1):
			if sorted_nums[i+1]-sorted_nums[i] == 1:
				sub_one.append((sorted_nums[i],sorted_nums[i+1]))
		max_len = 0
		max_com = []
		for item in sub_one:
			if c[item[0]]+c[item[1]]>max_len:
				max_len = c[item[0]]+c[item[1]]
				# max_com.append(item)
		# l = len(nums)
		# res = []
		# for j in range(l):
		# 	if nums[j] in max_com[-1]:
		# 		res.append(nums[j])
		return max_len

	def findLHS1(self, nums):
		c = Counter(nums)
		max_len = 0
		for key in c.keys():
			if key+1 in c:
				max_len = max(max_len,c[key]+c[key+1])
		return max_len

a = Solution()
print(a.findLHS1([1,3,2,2,5,2,3,7]))


