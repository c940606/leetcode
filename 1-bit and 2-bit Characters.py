class Solution(object):
	def isOneBitCharacter(self, bits):
		"""
		有两种特殊字符。第一种字符可以用一比特0来表示。第二种字符可以用两比特(10 或 11)来表示。
		现给一个由若干比特组成的字符串。问最后一个字符是否必定为一个一比特字符。给定的字符串总是由0结束
		--
		输入:
		bits = [1, 0, 0]
		输出: True
		解释:
		唯一的编码方式是一个两比特字符和一个一比特字符。所以最后一个字符是一比特字符。
		---
		输入:
		bits = [1, 1, 1, 0]
		输出: False
		解释:
		唯一的编码方式是两比特字符和两比特字符。所以最后一个字符不是一比特字符。
		--
		思路:
		遇到0 走1格
		遇到1 走2格
		:type bits: List[int]
		:rtype: bool
		"""
		if not bits:
			return False
		n = len(bits)
		if n == 1:
			if bits[0]==0:
				return True
			else:
				return False
		i = 0
		while i < n:
			if bits[i] == 0:
				i += 1
			else:
				i += 2
			if i == n -2:
				if bits[i] == 0:
					return True
				else:
					return False
			if i == n-1 and bits[i] == 0:
				return True
		return False
a = Solution()
print(a.isOneBitCharacter([1, 0, 0]))

