class Solution(object):
	def convertToBase7(self, num):
		"""
		给定一个整数，将其转化为7进制，并以字符串形式输出。
		---
		输入: 100
		输出: "202"
		---
		输入: -7
		输出: "-10"
		:type num: int
		:rtype: str
		"""
		if num == 0:
			return 0
		else:
			res = ""
			n = abs(num)
			while n :
				res = str(n%7) +res
				n //= 7
			return res if num > 0 else "-"+res
a = Solution()
print(a.convertToBase7(100))