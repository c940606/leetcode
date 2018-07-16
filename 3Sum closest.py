class Solution:
	def threeSumClosest(self, nums, target):
		"""
		给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
		找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案
		-------------------------------
		例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
			与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		cmp_t = 2**31
		res = 0
		n = len(nums)
		nums = sorted(nums)
		for i in range(n):
			left,right = i+1,n-1
			while left < right:
				temp = nums[i] + nums[left] + nums[right]
				num_abs = temp-target
				if num_abs==0:
					res = temp
					cmp_t = abs(num_abs)
					left += 1
					right -= 1
				elif num_abs > 0 :
					if cmp_t > abs(num_abs):
						cmp_t = abs(num_abs)
						res = temp
					right -= 1
				else:
					if cmp_t > abs(num_abs):
						cmp_t = abs(num_abs)
						res = temp
					left += 1
		return res
nums = [-1,2,1,-4]
target = 1
a = Solution()
print(a.threeSumClosest(nums,target))

