class Solution(object):
	def rotate(self, nums, k):
		"""
		给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
		---
		输入: [1,2,3,4,5,6,7] 和 k = 3
		输出: [5,6,7,1,2,3,4]
		解释:
		向右旋转 1 步: [7,1,2,3,4,5,6]
		向右旋转 2 步: [6,7,1,2,3,4,5]
		向右旋转 3 步: [5,6,7,1,2,3,4]
		---
		输入: [-1,-100,3,99] 和 k = 2
		输出: [3,99,-1,-100]
		解释:
		向右旋转 1 步: [99,-1,-100,3]
		向右旋转 2 步: [3,99,-1,-100]
		---
		思路:
		1. 可以 把 旋转k 位置求出
		2. 可以把前k 反转, 后 k反转 ,最后再反转
		3.
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		# k += 1
		k = k % n
		# print(k)
		copy_nums = nums.copy()
		for i in range(n):
			# print(copy_nums[(i+k)%n])
			nums[(i+k)%n] = copy_nums[i]
			# print(nums)
			# print("-----")
		return nums

	def rotate2(self, nums, k):
		# 反转
		return nums[-k:] + nums[:-k]

	def rotate3(self, nums, k):

		i = 0
		# res = [nums[0]]
		n = len(nums)
		temp1 = nums[i]
		count = n
		while count:
			print((i+k)%n)
			temp2 = nums[(i+k)%n]
			nums[(i + k) % n] = temp1
			temp1 = temp2
			i = (i+k)%n
			count -= 1
		return nums






a = Solution()
print(a.rotate3([1,2,3,4,5,6] ,2))