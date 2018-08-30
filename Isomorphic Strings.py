class Solution(object):
	def isIsomorphic(self, s, t):
		"""
		给定两个字符串 s 和 t，判断它们是否是同构的。
		如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
		所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
		---
		输入: s = "egg", t = "add"
		输出: true
		---
		输入: s = "foo", t = "bar"
		输出: false
		---
		输入: s = "paper", t = "title"
		输出: true
		:type s: str
		:type t: str
		:rtype: bool
		"""
		if len(set(s)) == len(set(t)) == len(set(zip(s,t))):
			return True
		return False
a = Solution()
print(a.isIsomorphic("paper","title"))