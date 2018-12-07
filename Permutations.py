from itertools import  permutations
class Solution:
	def permute(self, nums):
		"""
		给定一个没有重复数字的序列，返回其所有可能的全排列。
		-----------
		输入: [1,2,3]
		输出:
		[
		  [1,2,3],
		  [1,3,2],
		  [2,1,3],
		  [2,3,1],
		  [3,1,2],
		  [3,2,1]
		]
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.res = []
		self.dft([],nums)
		return self.res
	def dft(self,sing_list,nums):
		if len(nums) == 0:
			self.res.append(sing_list)
		for i in range(len(nums)):
			self.dft(sing_list+[nums[i]],nums[0:i]+nums[i+1:])

	def permute1(self, nums):
		if not nums:
			return
		res = []
		n = len(nums)
		visited = [0] * n
		def helper1(temp_list,length):
			if length == n:
				res.append(temp_list)
			for i in range(n):
				if visited[i] :
					continue
				visited[i] = 1
				helper1(temp_list+[nums[i]],length+1)
				visited[i] = 0
		def helper2(nums,temp_list,length):
			if length == n:
				res.append(temp_list)
			for i in range(len(nums)):
				helper2(nums[:i]+nums[i+1:],temp_list+[nums[i]],length+1)
		helper2(nums,[],0)
		return res

a = Solution()
nums = [1,2,3]
print(a.permute1(nums))
