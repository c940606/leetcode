class Solution(object):
	def isPowerOfThree(self, n):
		"""
		给定一个整数，写一个函数来判断它是否是 3 的幂次方。
		:type n: int
		:rtype: bool
		"""
		i = 1
		while i <= (n**(1/3)):
			if i**3 == n:
				return True
			i += 1
		return False

	def isPowerOfThree1(self, n):
		if n <= 0:
			return False
		if n == 1:
			return True
		if n%3==0:
			return self.isPowerOfThree1(n//3)
		return False
a = Solution()
print(a.isPowerOfThree(27))
