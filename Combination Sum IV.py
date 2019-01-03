class Solution(object):
	def combinationSum4(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		self.res = 0
		nums.sort()

		def helper(start, last, target):
			# print(target)
			for i in range(start,last):
				tmp = target - nums[i]
				if tmp == 0:
					self.res += 1
				elif tmp > 0:
					helper(start, last , tmp)
				else:
					break

		helper(0, len(nums), target)
		return self.res

	def combinationSum4_1(self, nums, target):
		from collections import defaultdict
		nums.sort()
		lookup = defaultdict()
		lookup[0] = 1
		def helper(nums,target):
			if target in lookup:
				return lookup[target]
			res = 0
			for num in nums:
				if target >= num:
					res += helper(nums, target-num)
				else:
					break
			lookup[target] = res
			return res
		return helper(nums, target )
a = Solution()
print(a.combinationSum4(nums = [1, 2, 3],target = 4))
print(a.combinationSum4_1([4,2,1],62))
