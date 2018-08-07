import math


class Solution:
	def titleToNumber(self, s):
		"""
		给定一个Excel表格中的列名称，返回其相应的列序号。
		---
		思路:
		用字典
		:type s: str
		:rtype: int
		"""
		alp_list = list(map(lambda x:chr(x),range(65,91)))
		lookup = {}
		for key,val in zip(alp_list,range(1,27)):
			lookup[key] = val
		# print(lookup)
		n = len(s)
		res = 0
		for i in s:
			res += 26**(n-1)*lookup[i]
			n -= 1
		return res






a = Solution()

print(a.titleToNumber("ZYXYZAAAAAAAAAAAAAAAAAAAAAAAAA"))
print(math.pi)
