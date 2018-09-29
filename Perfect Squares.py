class Solution(object):
	def numSquares(self, n):
		"""
		给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）
		使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
		---
		输入: n = 12
		输出: 3
		解释: 12 = 4 + 4 + 4.
		--
		输入: n = 13
		输出: 2
		解释: 13 = 4 + 9.
		--
		思路:

		:type n: int
		:rtype: int
		"""
		num = int(n**0.5)
		num_list = [i**2 for i in range(num,0,-1)]
		res = []
		self.min_count = n+1
		def helper(n,temp,count):
			if n<0:
				return
			if n == 0:
				res.append(temp)
				self.min_count = min(self.min_count,count)
				return
			for num in num_list:
				helper(n-num,temp+[num],count+1)
		helper(n,[],0)
		print(self.min_count)
		return res

	def numSquares1(self, n):
		num = int(n ** 0.5)
		num_list = [i ** 2 for i in range(num, 0, -1)]
		res = [0]*(n+1)
		for i in range(1,n+1):
			min_num = n+1
			for num in num_list:
				if i - num >= 0 and res[i-num] + 1 < min_num:
					min_num = res[i-num]+1
			res[i] = min_num
		return res[-1]

	_dp = [0]

	def numSquares2(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		dp = self._dp
		while len(dp) <= n:
			print(list((min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,)))
			dp += list((min(dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))) + 1,))
			print(dp)
		return dp[n]
a = Solution()
print(a.numSquares2(42))
