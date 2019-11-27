class Solution(object):
	def wordPattern2(self, pattern, str):
		"""
		给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
		这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式
		---
		输入: pattern = "abba", str = "dog cat cat dog"
		输出: true
		----
		思路：
		通过模式把字典造出来，
		:type pattern: str
		:type str: str
		:rtype: bool
		"""
		str = str.split(" ")
		pattern_dict = {}
		str_dict = {}
		for index,key in enumerate(pattern):
			if key in pattern_dict:
				pattern_dict[key].append(index)
			else:
				pattern_dict[key] = [index]
		for index,key in enumerate(str):
			if key in str_dict:
				str_dict[key].append(index)
			else:
				str_dict[key] = [index]
		return sorted(pattern_dict.values()) == sorted(str_dict.values())

	def wordPattern1(self, pattern, str):
		str = str.split(" ")
		if len(set(pattern)) != len(set(str)):
			return False
		if len(set(pattern)) == len(set(str)) == len(set(zip(pattern,str))):
			return True
		else:
			return False

	def wordPattern(self, pattern, s):



a = Solution()
print(a.wordPattern1("abba","dog cat cat dog"))
