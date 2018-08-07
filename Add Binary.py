
class Solution:
	def addBinary(self, a, b):
		"""
		给定两个二进制字符串，返回他们的和（用二进制表示）。
		输入为非空字符串且只包含数字 1 和 0。
		:type a: str
		:type b: str
		:rtype: str
		"""
		return bin(int(a,2) + int(b,2))[2:]
