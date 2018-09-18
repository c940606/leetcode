class Solution:
	def threeSum1(self, nums):
		"""
		给定一个包含 n 个整数的数组 nums，
		判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
		注意：答案中不可以包含重复的三元组。
		例子:
		例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
		满足要求的三元组集合为：
				[
				  [-1, 0, 1],
				  [-1, -1, 2]
				]
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		n = len(nums)
		threeSum = []
		for i in range(n):
			for j in range(i+1,n):
				for k in range(j+1,n):
					if nums[i] + nums[j] + nums[k] == 0:
						if sorted([nums[i],nums[j],nums[k]]) not in threeSum:
							threeSum.append(sorted([nums[i],nums[j],nums[k]]))
		return threeSum

	def threeSum2(self, nums):
		nums = sorted(nums)
		n = len(nums)
		res = []
		for i in range(n):
			if nums[i] == nums[i-1] and i > 0:
				continue
			left,right = i+1,n-1
			while left < right:
				temp = nums[i] + nums[left] + nums[right]
				if temp == 0:
					res.append([nums[i],nums[left],nums[right]])
					left += 1
					right -= 1
					while nums[left-1] == nums[left] and left < right:
						left += 1
					while nums[right+1] == nums[right] and left < right:
						right -= 1
				elif temp > 0:
					right -= 1
				else:
					left += 1
		return  res

	def threeSum3(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		n = len(nums)
		res = []
		if n < 3:
			return res
		nums.sort()
		print(nums)
		for k in range(n - 2):
			if k > 0 and nums[k] == nums[k-1]:
				continue

			if (nums[k] + nums[k + 1] + nums[k + 2]) > 0:
				break
			if (nums[k] + nums[n - 2] + nums[n - 1]) < 0:
				continue

			i = k + 1
			j = n - 1
			print(i,j)
			while i < j:
				target = nums[k] + nums[i] + nums[j]
				print(target)
				# mid = (i + j) // 2
				if target == 0:
					res.append([nums[k], nums[i], nums[j]])
					while i < j and nums[i] == nums[i + 1]:
						i += 1
					while j < j and nums[j] == nums[j - 1]:
						j -= 1
					i += 1
					j -= 1
				elif target > 0:
					j -= 1
				else:
					i += 1
		return res


nums1 = [-1,0,1,2,-1,-4]
nums2 =[7,5,-8,-6,-13,7,10,1,1,-4,-14,0,-1,-10,1,-13,-4,6,-11,8,-6,0,0,-5,0,11,-9,8,2,-6,4,-14,6,4,-5,0,-12,12,-13,5,-6,10,-10,0,7,-2,-5,-12,12,-9,12,-9,6,-11,1,14,8,-1,7,-13,8,-11,-11,0,0,-1,-15,3,-11,9,-7,-10,4,-2,5,-4,12,7,-8,9,14,-11,7,5,-15,-15,-4,0,0,-11,3,-15,-15,7,0,0,13,-7,-12,9,9,-3,14,-1,2,5,2,-9,-3,1,7,-12,-3,-1,1,-2,0,12,5,7,8,-7,7,8,7,-15]
a = Solution()
print(a.threeSum3(nums1))
# print(a.threeSum1(nums2))
# print("----------------------------------")
# print(a.threeSum2(nums1))
# print(a.threeSum2(nums2))


