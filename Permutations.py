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
a = Solution()
nums = [1,2,3]
print(a.permute(nums))
