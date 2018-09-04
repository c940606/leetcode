class Solution(object):
	def addStrings(self, num1, num2):
		"""
		给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
			注意：
			num1 和num2 的长度都小于 5100.
			num1 和num2 都只包含数字 0-9.
			num1 和num2 都不包含任何前导零。
			你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
		---
		思路:
			用常规的加法
		:type num1: str
		:type num2: str
		:rtype: str
		"""
		m = len(num1)
		n = len(num2)
		carry = 0
		res = []
		while m > 0 and n > 0:
			aNd = ord(num1[m-1]) - 48 + ord(num2[n-1]) - 48 + carry
			carry = aNd // 10
			geweishu = aNd % 10
			res.append(chr(geweishu+48))
			m -= 1
			n -= 1
		print(m,n,carry)
		print(res)
a = Solution()
print(a.addStrings("11","9"))
