from   typing import List
class Solution:
	def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		import functools
		wordDict = set(wordDict)
		max_len = max(len(word) for word in wordDict)
		
		@functools.lru_cache(None)
		def dfs(i):
			if i == len(s):
				return True
			for j in range(i, i + max_len):
				if s[i:j+1] in wordDict and dfs(j + 1):
					return True
	
			return False

		return dfs(0)

a = Solution()
print(a.wordBreak(s = "leetcode", wordDict = ["leet", "code"]))
print(a.wordBreak(s="applepenapple", wordDict=["apple", "pen"]))
print(a.wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))