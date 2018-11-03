class Solution(object):
	def integerBreak(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		res = [0]*(n+1)
		res[2] = 1
		res[3] = 2
		res[4] = 4
		res[5] = 6
		i = 6
		# for i in enumerate
		while i < n+1:
			res[i] = max(map(lambda x:x[1]*(i-x[0]) ,enumerate(res[:i])))
			i += 1
		print(res)
		return res[-1]
a = Solution()
print(a.integerBreak(6))