from collections import Counter


class Solution(object):
	def findTheDifference(self, s, t):
		"""
		给定两个字符串 s 和 t，它们只包含小写字母。
		字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
		请找出在 t 中被添加的字母。
		---
		输入：
		s = "abcd"
		t = "abcde"
		输出：
		e
		解释：
		'e' 是那个被添加的字母。
		---

		:type s: str
		:type t: str
		:rtype: str
		"""
		s = Counter(s)
		t = Counter(t)
		# print(s,t)
		for i in range(97,123):
			alp = chr(i)
			# print(alp)
			# print(t.get(alp),s.get(alp,default=0))
			if t.get(alp):
				if s.get(alp) and t.get(alp) - s.get(alp) == 1:
					return alp
				elif not s.get(alp):
					return alp

	def findTheDifference1(self, s, t):
		s = sum(map(ord,s))
		t = sum(map(ord,t))
		return chr(t-s)


a = Solution()
print(a.findTheDifference1("a","aa"))


