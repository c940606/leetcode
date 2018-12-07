class Solution:
	def permuteUnique(self, nums):
		"""
		给定一个可包含重复数字的序列，返回所有不重复的全排列。
		----
		输入: [1,1,2]
		输出:
		[
		  [1,1,2],
		  [1,2,1],
		  [2,1,1]
		]
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.res = []
		n = len(nums)
		self.dft([], nums,n)
		return self.res

	def dft(self, sing_list, nums,n):
		if n == 0 and sing_list not in self.res:
			self.res.append(sing_list)
		for i in range(len(nums)):
			self.dft(sing_list + [nums[i]], nums[0:i]+nums[i+1:],n-1)

	def permuteUnique1(self, nums):
		if not nums:
			return []
		nums.sort()
		n = len(nums)
		visited = [0] * n
		res = []

		def helper1(temp_list, length):
			# if length == n and temp_list not in res:
			# 	res.append(temp_list)
			if length == n:
				res.append(temp_list)
			for i in range(n):
				if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
					continue
				visited[i] = 1
				helper1(temp_list + [nums[i]], length + 1)
				visited[i] = 0

		def helper2(nums, temp_list, length):
			if length == n and temp_list not in res:
				res.append(temp_list)
			for i in range(len(nums)):
				helper2(nums[:i] + nums[i + 1:], temp_list + [nums[i]], length + 1)

		# helper1([],0)
		helper2(nums, [], 0)
		return res
a = Solution()
nums = [1,1,2]
print(a.permuteUnique1(nums))
