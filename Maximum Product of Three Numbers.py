class Solution(object):
	def maximumProduct(self, nums):
		"""
		给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
		---
		输入: [1,2,3]
		输出: 6
		---
		输入: [1,2,3,4]
		输出: 24
		--
		思路:
		动态规划,
		:type nums: List[int]
		:rtype: int
		"""
		# 连续3个数组
		n = len(nums)
		if n < 3:
			return
		if n == 3:
			return nums[0]*nums[1]*nums[2]
		res = [nums[0]*nums[1]*nums[2]]*3
		for i in range(3,n):
			temp = max(res[i-1],nums[i]*nums[i-1]*nums[i-2])
			res.append(temp)
		print(res)
		return res[-1]

	def maximumProduct1(self, nums):
		n = len(nums)
		if n < 3:
			return
		if n == 3:
			return nums[0] * nums[1] * nums[2]
		# res = [nums[0] * nums[1] * nums[2]]
		max_list = [nums[0] * nums[1]]*2
		min_list = [nums[0] * nums[1]]*2
		# print(max_list,min_list)
		for i in range(2, n):
			tempmax = max(max_list[i-1], nums[i]*nums[i-1])
			three_max = tempmax * nums[i]
			max_list.append(tempmax)
			tempmin = min(min_list[i-1],nums[i]*nums[i-1])
			three_min = tempmin*nums[i]
			min_list.append(tempmin)
			temp = max(three_max,three_min)
			# print(temp)
			# res.append(temp)

		# print(res)
		return max(max(max_list)*max(nums),min(min_list)*min(nums))
a = Solution()
print(a.maximumProduct1([1,2,3,4]))


