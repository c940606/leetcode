class Solution(object):
	def reverseWords(self, s):
		"""
		给定一个字符串，逐个翻转字符串中的每个单词。
		---
		输入: "the sky is blue",
		输出: "blue is sky the".
		:type s: str
		:rtype: str
		"""
		s = s.split(" ")
		print(s)
		print(len(s[4]))
		n = len(s)
		i = 0
		while "" in s:
			s.remove("")
		s = s[::-1]
		print(s)
		return " ".join(s)
a = Solution()
print(a.reverseWords("the sky is    blue"))
