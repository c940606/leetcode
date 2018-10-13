class Solution(object):
	def hasAlternatingBits(self, n):
		"""
		给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。
		---
		输入: 5
		输出: True
		解释:
		5的二进制数是: 101
		---
		输入: 7
		输出: False
		解释:
		7的二进制数是: 111
		---
		输入: 11
		输出: False
		解释:
		11的二进制数是: 1011
		--
		输入: 10
		输出: True
		解释:
		10的二进制数是: 1010
		:type n: int
		:rtype: bool
		"""
		bin_num = bin(n)[2:]
		n = len(bin_num)
		if n == 1:
			return True
		i = 0
		j = 1
		while j < n:
			if bin_num[i] != bin_num[j]:
				i += 1
				j += 1
			else:
				return False
		return True
