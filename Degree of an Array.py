class Solution(object):
	def findShortestSubArray(self, nums):
		"""
		给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
		你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
		---
		输入: [1, 2, 2, 3, 1]
		输出: 2
		解释:
		输入数组的度是2，因为元素1和2的出现频数最大，均为2.
		连续子数组里面拥有相同度的有如下所示:
		[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
		最短连续子数组[2, 2]的长度为2，所以返回2.
		:type nums: List[int]
		:rtype: int
		"""
		lookup1 = {}
		lookup2 = {}
		for idx,num in enumerate(nums):
			if num in lookup1:
				lookup1[num].append(idx)
				lookup2[num] += 1
			else:
				lookup1[num] = [idx]
				lookup2[num] = 1
		lookup2 = sorted(lookup2.items(),key=lambda x:x[1],reverse=True)
		max_degree = lookup2[0][1]
		max_len = 500001
		for item in lookup2:
			if item[1] == max_degree:
				max_len = min(lookup1[item[0]][-1]-lookup1[item[0]][0]+1,max_len )
			else:
				break
		return max_len
a = Solution()
print(a.findShortestSubArray([1, 2, 2, 3, 1]))
