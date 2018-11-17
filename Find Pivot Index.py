class Solution(object):
	def pivotIndex(self, nums):
		"""
		给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
		我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
		如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
		---
		输入:
		nums = [1, 7, 3, 6, 5, 6]
		输出: 3
		解释:
		索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
		同时, 3 也是第一个符合要求的中心索引。
		:type nums: List[int]
		:rtype: int
		"""
		left = [0]
		right = [0]
		n = len(nums)
		if n <=2:
			return -1
		for i in range(1,n):
			left.append(left[-1]+nums[i-1])
		print(left)
		for j in range(n-1,0,-1):
			right.append(right[-1]+nums[j])
		right = right[::-1]
		print(right)
		loc = 0
		for s,k in zip(left,right):
			if s == k:
				return loc
			loc += 1
		return -1

	def pivotIndex1(self, nums):
		res = sum(nums)
		temp = 0
		for loc,num in enumerate(nums):
			if temp *2 == res-num:
				return loc
			temp += num
		return -1
a = Solution()
print(a.pivotIndex1([1, 7, 3, 6, 5, 6]))