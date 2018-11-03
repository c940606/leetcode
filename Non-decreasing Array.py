class Solution(object):
	def checkPossibility(self, nums):
		"""
		给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
		我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。
		---
		输入: [4,2,3]
		输出: True
		解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
		---
		输入: [4,2,1]
		输出: False
		解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
		:type nums: List[int]
		:rtype: bool
		"""
		n = len(nums)
		if n == 1 or n == 0:
			return True
		flag = 0
		for i in range(1,n):
			if nums[i] - nums[i-1] < 0:
				flag += 1
				if flag > 1:
					return False
				if i-2 >= 0 and nums[i] < nums[i-2]:
					nums[i] = nums[i-1]
				elif i -2 >= 0 and nums[i] > nums[i-2]:
					nums[i-1] = nums[i]
				elif i == 1 :
					nums[i-1] = nums[i]
				else:
					return False
		print(nums)
		return True
a = Solution()
print(a.checkPossibility([4,2,3]))
print(a.checkPossibility([3,4,2,3]))
print(a.checkPossibility([-1,4,2,3]))