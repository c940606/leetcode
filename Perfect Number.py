class Solution(object):
	def checkPerfectNumber(self, num):
		"""
		对于一个 正整数，如果它和除了它自身以外的所有正因子之和相等，我们称它为“完美数”。
		给定一个 正整数 n， 如果他是完美数，返回 True，否则返回 False
		---
		输入: 28
		输出: True
		解释: 28 = 1 + 2 + 4 + 7 + 14
		:type num: int
		:rtype: bool
		"""
		if num <= 1:
			return False
		res =[1]
		n = int(num**(0.5))
		for i in range(2,n):
			if num % i == 0:
				res.append(i)
				res.append(num//i)
		if num == sum(res):
			return True
		return False
a = Solution()
print(a.checkPerfectNumber(48))