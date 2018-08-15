from collections import Counter


class Solution(object):
	def firstUniqChar(self, s):
		"""
		给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
		---
		先统计字符的个数
		:type s: str
		:rtype: int
		"""
		count = Counter(s)
		i = 0
		n = len(s)
		while i < n:
			if count[s[i]] == 1:
				return i
			i += 1
		return

	def firstUniqChar1(self, s):
		# if not s:
		# 	return -1
		oneindex = []
		for i in range(97,123):
			if s.count(chr(i)) == 1:
				# print(chr())
				oneindex.append(s.find(chr(i)))
		return min(oneindex) if oneindex else -1

	def firstUniqChar2(self, s):
		oneindex = []
		for i in range(97, 123):
			alp = chr(i)
			l = s.find(alp)
			r = s.rfind(alp)
			if l != -1 and l == r:
				oneindex.append(l)
		return min(oneindex) if oneindex else -1

a = Solution()
print(a.firstUniqChar2("cc"))