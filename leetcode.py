class Solution(object):
	def isPowerOfTwo(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		if n<=0:
			return False
		if n == 1:
			return True
		if n %2 == 0:
			return self.isPowerOfTwo(n//2)
		return False

	def isPowerOfTwo1(self, n):
		return n &(n-1)==0 if n!= 0 else False
a = Solution()
print(a.isPowerOfTwo1(8))
