class Solution(object):
	def findAndReplacePattern(self, words, pattern):
		"""
		你有一个单词列表 words 和一个模式  pattern，你想知道 words 中的哪些单词与模式匹配。
		如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。
		（回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）
		返回 words 中与给定模式匹配的单词列表。
		你可以按任何顺序返回答案。
		---
		输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
		输出：["mee","aqq"]
		解释：
		"mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
		"ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
		因为 a 和 b 映射到同一个字母。
		:type words: List[str]
		:type pattern: str
		:rtype: List[str]
		"""
		res = []
		n = len(pattern)
		for word in words:
			if len(word) == len(pattern) and len(set(word)) == len(set(pattern)):
				lookup = {}
				i = 0
				while i < n:
					if pattern[i] in lookup:
						if lookup[pattern[i]] != word[i]:
							break
					else:
						lookup[pattern[i]] = word[i]
					i += 1
				if i == n:
					res.append(word)
		return res
a = Solution()
print(a.findAndReplacePattern(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"))
