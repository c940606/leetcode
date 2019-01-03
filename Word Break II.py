class Solution:
	def wordBreak(self, s, wordDict):
		"""
		:type s: str
		:type wordDict: List[str]
		:rtype: List[str]
		"""
		wordDict = set(wordDict)
		n = len(s)
		res = []
		long_word = max(map(lambda a:len(a),wordDict))
		lookup  = {}
		# print(long_word)
		def helper(start, tmp):
			# print(tmp)
			if start == n:
				res.append(tmp[:-1])
			for i in range(start, n+1):
				if i - start > long_word:
					break
				if s[start:i] in wordDict:
					# print(s[start:i])
					helper(i, tmp +  s[start:i] + " ")

		helper(0, "")
		return res


a = Solution()
print(a.wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
print(a.wordBreak(s = "pineapplepenapple",wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]))
print(a.wordBreak(s = "catsandog",wordDict = ["cats", "dog", "sand", "and", "cat"]))
# print(a.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
