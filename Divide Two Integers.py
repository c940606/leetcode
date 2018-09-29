import math


class Solution(object):
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		res = abs(dividend) // abs(divisor)
		if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
			res *= -1
		if res < -2 ** 31 or res > (2 ** 31 - 1):
			return 2 ** 31 - 1
		return res
a = Solution()
print(a.divide(7,-3))