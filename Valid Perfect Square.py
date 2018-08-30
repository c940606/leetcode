class Solution(object):
	def isPerfectSquare(self, num):
		"""
		给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
		注意：不要使用任何内置的库函数，如  sqrt。
		---
		1,4,9,16...
		3  5  7
		:type num: int
		:rtype: bool
		"""
		temp = 1
		i = 3
		while temp < num:
			temp += i
			i += 2
		if temp == num:
			return True
		return False
a = Solution()
print(a.isPerfectSquare(15))
