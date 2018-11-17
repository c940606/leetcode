class Solution(object):
	def shortestCompletingWord(self, licensePlate, words):
		"""
		如果单词列表（words）中的一个单词包含牌照（licensePlate）中所有的字母，那么我们称之为完整词。
		在所有完整词中，最短的单词我们称之为最短完整词。
		单词在匹配牌照中的字母时不区分大小写，比如牌照中的 "P" 依然可以匹配单词中的 "p" 字母。
		我们保证一定存在一个最短完整词。当有多个单词都符合最短完整词的匹配条件时取单词列表中最靠前的一个。
		牌照中可能包含多个相同的字符，比如说：对于牌照 "PP"，单词 "pair" 无法匹配，但是 "supper" 可以匹配。
		---
		输入：licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
		输出："steps"
		说明：最短完整词应该包括 "s"、"p"、"s" 以及 "t"。对于 "step" 它只包含一个 "s"
		所以它不符合条件。同时在匹配过程中我们忽略牌照中的大小写。
		---
		输入：licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
		输出："pest"
		说明：有三个单词都符合完整词的定义，但是我们返回最先出现的单词。
		---

		:type licensePlate: str
		:type words: List[str]
		:rtype: str
		"""
		from collections import Counter
		lookup = {}
		for alp in licensePlate:
			if alp.isalpha():
				alp = alp.lower()
				if alp in lookup:
					lookup[alp] += 1
				else:
					lookup[alp] = 1
		# print(lookup)
		res = []
		for word in words:
			n = len(word)
			c = Counter(word)
			if all(map(lambda x:c[x]>=lookup[x] if x in c else False,lookup.keys())):
				res.append((word,n))

		res = sorted(res,key=lambda x:x[1])
		return res[0][0]
a = Solution()
print(a.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]))
print(a.shortestCompletingWord(licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]))
