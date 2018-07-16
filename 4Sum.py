class Solution:
	def fourSum(self, nums, target):
		"""
		给定一个包含 n 个整数的数组 nums
		和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，
		使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
		-------------------------------------------------------------
		给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
			满足要求的四元组集合为：
			[
			  [-1,  0, 0, 1],
			  [-2, -1, 1, 2],
			  [-2,  0, 0, 2]
			]
		:type nums: List[int]
		:type target: int
		:rtype: List[List[int]]
		"""
		nums.sort()
		n = len(nums)
		res = []
		if len(nums) < 4:
			return []
		if len(nums) == 4 and target == sum(nums):
			res.append(nums)
			return res
		for i in range(0,n-3):
			for j in range(i+1,n-2):
				# if nums[j] == nums[j-1] and j > 0:
				# 	continue
				left = j+1
				right = n-1
				while left<right:
					temp = nums[i]+nums[j]+nums[left]+nums[right]
					if temp == target:
						temp_list =[nums[i],nums[j],nums[left],nums[right]]
						if temp_list not in res:

							res.append(temp_list)
						right -= 1
						left += 1
						while left < right and nums[left] == nums[left - 1]:
							left += 1
						while left < right and nums[right] == nums[right + 1]:
							right -= 1
					elif temp > target:
						right -= 1
					else:
						left += 1

		return res
nums = [1, 0, -1, 0, -2, 2]
target = -1
nums1 = [-1,0,1,2,-1,-4]
nums2 = [1,0,-1,0,-2,2]
nums3 = [-3,-2,-1,0,0,1,2,3]
target3 = 0
target2 = 0
a = Solution()
print(a.fourSum(nums3,target3))