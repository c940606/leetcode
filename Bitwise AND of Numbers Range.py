class Solution:
	def rangeBitwiseAnd(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		i = 0
		while m != n:
			m >>= 1
			n >>= 1
			i += 1
			print(m, n, i)
		return n << i


a = Solution()
print(a.rangeBitwiseAnd(5, 7))
