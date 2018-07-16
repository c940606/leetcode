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
a = Solution()
nums = [1,1,2]
print(a.permuteUnique(nums))