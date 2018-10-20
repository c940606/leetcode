class Solution(object):
	def judgeSquareSum(self, c):
		"""
		:type c: int
		:rtype: bool
		"""
		i = 1
		while i*i < c:
			temp = (c - i*i)**0.5
			if temp == int(temp):
				return True
			i += 1
		return False
a = Solution()
print(a.judgeSquareSum(3))
