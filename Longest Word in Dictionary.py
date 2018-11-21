class Solution(object):
	def longestWord(self, words):
		"""
		给出一个字符串数组words组成的一本英语词典。从中找出最长的一个单词，
		该单词是由words词典中其他单词逐步添加一个字母组成。若其中有多个可行的答案，则返回答案中字典序最小的单词。
		若无答案，则返回空字符串。
		---
		输入:
		words = ["w","wo","wor","worl", "world"]
		输出: "world"
		解释:
		单词"world"可由"w", "wo", "wor", 和 "worl"添加一个字母组成。
		--
		输入:
		words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
		输出: "apple"
		解释:
		"apply"和"apple"都能由词典中的单词组成。但是"apple"得字典序小于"apply"。
		---

		:type words: List[str]
		:rtype: str
		"""
		words.sort()
		word_set = set()
		word_set.add("")
		long_word = ""
		print(words)
		for word in words:
			if word[:-1] in word_set:
				print(word)
				word_set.add(word)
				if len(word) > len(long_word):
					long_word = word
		return long_word
a = Solution()
# print(a.longestWord(words = ["w","wo","wor","worl", "world"]))
print(a.longestWord(["a","banana","app","appl","ap","apply","apple"]))
