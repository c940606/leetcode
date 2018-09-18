from collections import Counter


class Solution(object):
	def canConstruct(self, ransomNote, magazine):
		"""
		给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
		判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。
		(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
		---
		canConstruct("a", "b") -> false
		canConstruct("aa", "ab") -> false
		canConstruct("aa", "aab") -> true
		--
		思路:
		集合
		首先看字符串是否是包含的
		然后看个数
		:type ransomNote: str
		:type magazine: str
		:rtype: bool
		"""
		c1 = Counter(ransomNote)
		c2 = Counter(magazine)
		ransomNote_set = set(ransomNote)
		# if ransomNote_set&set(magazine) == ransomNote_set and all(map(lambda x:c1[x]<=c2[x],ransomNote_set)):
		# 	return True
		for  item in ransomNote_set:
			if c1[item] > c2[item]:
				return False
		return True
a = Solution()
print(a.canConstruct("aa", "aab"))