class Solution(object):
	def myAtoi(self, str):
		"""
		实现 atoi，将字符串转为整数。
		在找到第一个非空字符之前，需要移除掉字符串中的空格字符。如果第一个非空字符是正号或负号，选取该符号，
		并将其与后面尽可能多的连续的数字组合起来，
		这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
		字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。
		当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。
		若函数不能执行有效的转换，返回 0。
		说明：
			假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。如果数值超过可表示的范围，
			则返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
		---
		输入: "42"
		输出: 42
		---
		输入: "   -42"
		输出: -42
		解释: 第一个非空白字符为 '-', 它是一个负号。
			 我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
		---
		1. 首先把首尾空格去掉
			判断是否为空
		2.依次判断是否在列表中（数字列表）
		:type str: str
		:rtype: int
		"""
		# lookup = [chr(i) for i in range(48,58)]
		i = 0
		str =str.strip()
		n = len(str)
		if not str :
			return 0
		if str[0] == "-" or str[0] == "+":
			i += 1
		while i < n and str[i].isdigit() :
			i += 1
		# print(i)
		s = str[:i]
		if s == "-" or s == "+" or len(s) == 0:
			return 0
		num = int(s)
		if num < -2147483648:
			return -2147483648
		elif num > 2147483647:
			return 2147483647
		else:
			return num
a = Solution()
print(a.myAtoi("     -42"))

