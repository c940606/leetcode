from itertools import combinations


class Solution:
	def combinationSum3(self, k, n):
		"""
		找出所有相加之和为 n 的 k 个数的组合。
		组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
		说明：
		所有数字都是正整数。
		解集不能包含重复的组合\
		---
		输入: k = 3, n = 7
		输出: [[1,2,4]]
		:type k: int
		:type n: int
		:rtype: List[List[int]]
		"""
		self.res = []
		self.trace([],k,n)
		return self.res
	def trace(self,temp,k,n):
		print(n)
		if k == 0 and n == 0:
			return self.res.append(sorted(temp))
		if k == 0 or n < 0:
			return

		for i in range(1,10):
			if i > n or i in temp:
				return
			self.trace(temp+[i],k-1,n-i)

	def combinationSum_3(self, k, n):
		res = []
		for i in combinations(range(1,10),k):
			if sum(i) == n:
				res.append(i)
		return res

a = Solution()
# print(a.combinationSum3(8,36))
print(a.combinationSum_3(3,7))

