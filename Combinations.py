class Solution:
	def combine(self, n, k):
		"""
		给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
		---
		输入: n = 4, k = 2
		输出:
		[
		  [2,4],
		  [3,4],
		  [2,3],
		  [1,2],
		  [1,3],
		  [1,4],
		]
		:type n: int
		:type k: int
		:rtype: List[List[int]]
		"""
		self.res = []
		nums = [i+1 for i in range(n)]
		self.dsf([],nums,k)
		return self.res

	def dsf(self,temp,nums,k):
		if k == 0 and sorted(temp) not in self.res:
			self.res.append(sorted(temp))
		elif k > 0:
			for i in range(len(nums)):
				self.dsf(temp+[nums[i]],nums[0:i]+nums[i+1:],k-1)
n = 10
k = 3
a = Solution()
print(a.combine(n,k))


