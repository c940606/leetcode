class Solution(object):
	def maxProduct(self, nums):
		"""
		给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）
		---
		输入: [2,3,-2,4]
		输出: 6
		解释: 子数组 [2,3] 有最大乘积 6。
		---
		输入: [-2,0,-1]
		输出: 0
		解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
		---
		思路:
		动态规划
		max(前i-1最大乘积,自己,和前面一个值乘积)
		:type nums: List[int]
		:rtype: int
		"""
		if not nums :
			return
		res = [nums[0]]
		max_list = [nums[0]]
		min_list = [nums[0]]
		# print(res,max_list,min_list)
		n = len(nums)

		for i in range(1,n):
			tempmax = max(nums[i],max_list[i-1]*nums[i],min_list[i-1]*nums[i])
			max_list.append(tempmax)
			tempmin = min(nums[i],max_list[i-1]*nums[i],min_list[i-1]*nums[i])
			min_list.append(tempmin)
			temp = max(tempmax,tempmin)
			res.append(temp)
		print(max_list,min_list)
		print(res)
		return max(res)
a = Solution()
print(a.maxProduct([2,3,-2,4]))
