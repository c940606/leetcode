class Solution:
	def repeatedSubstringPattern(self, s):
		"""
		给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。\
		给定的字符串只含有小写英文字母，并且长度不超过10000。
		---
		输入: "abab"
		输出: True
		解释: 可由子字符串 "ab" 重复两次构成。
		---
		思路:
		1.找小于长度一半的约数
		2. 从约数取长度
		3. 看等于原字符
		:type s: str
		:rtype: bool
		"""
		n = len(s)
		# if n == 1:
		# 	return False
		for num in self.divisor(n):
			div_num = n//num
			if s == s[:num]*div_num:
				return True
		return False
	def divisor(self,n):
		# div =[]
		# print(n)
		for i in range(1,n//2+1):
			# print(i)
			if n%i == 0:
				yield i

a = Solution()
print(a.repeatedSubstringPattern("a"))

