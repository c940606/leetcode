class Solution:
	def subsets(self, nums):
		"""
		给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
		说明：解集不能包含重复的子集。
		---
		输入: nums = [1,2,3]
		输出:
		[
		  [3],
		  [1],
		  [2],
		  [1,2,3],
		  [1,3],
		  [2,3],
		  [1,2],
		  []
		]
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.res = []
		# n = len(nums)
		self.Backtracking([],nums)
		return self.res
	def Backtracking(self,temp,nums):
		# if not nums:
		# 	self.res.append(temp)
		# 	return
		if temp not in self.res:
			self.res.append(temp)

		for i in range(len(nums)):
			# temp.append(nums[i])

			self.Backtracking(temp+[nums[i]],nums[i+1:])

	def subsets1(self, nums):
		results = [[]]
		for i in nums:
			results = results + [[i] + num for num in results]

			print(results)
		return results

	def subsets2(self, nums):
		if not nums:
			return []
		res = []
		n = len(nums)

		def helper(idx, temp_list):
			res.append(temp_list)
			for i in range(idx, n):
				helper(i + 1, temp_list + [nums[i]])

		helper(0, [])
		return res

nums = [1,2,3]
a = Solution()
print(a.subsets2(nums))
