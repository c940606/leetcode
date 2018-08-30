from collections import Counter


class Solution(object):
	def isAnagram(self, s, t):
		"""
		给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的一个字母异位词。
		---
		输入: s = "anagram", t = "nagaram"
		输出: true
		--
		首先两个不相等
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if s == t or Counter(s) != Counter(t):
			return False
		for i in range(len(t)):
			if t[:i] in s and t[i+1:] in s:
				return True
		return False
a = Solution()
print(a.isAnagram(s = "rat", t = "car"))
