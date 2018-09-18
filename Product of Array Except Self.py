class Solution(object):
	def productExceptSelf(self, nums):
		"""
		给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
		其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
		---
		输入: [1,2,3,4]
		输出: [24,12,8,6]
		:type nums: List[int]
		:rtype: List[int]
		"""
		left = [1]
		right = [1]
		n = len(nums)
		for i in range(1,n):
			left.append(nums[i-1]*left[-1])
		# print(left)
		for i in range(n-2,-1,-1):
			right.insert(0,right[0]*nums[i+1])
		# print(right)
		return list(map(lambda x:x[0]*x[1],zip(left,right)))

a = Solution()
print(a.productExceptSelf([1,2,3,4]))


