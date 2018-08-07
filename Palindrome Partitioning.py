class Solution:
	def partition(self, s):
		"""
		给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
		返回 s 所有可能的分割方案。
		---
		输入: "aab"
		输出:
		[
		  ["aa","b"],
		  ["a","a","b"]
		]
		:type s: str
		:rtype: List[List[str]]
		"""
		self.res = []
		self.trace([],s)
		return self.res

	def trace(self,temp,s):
		if not s and temp == temp:
			return self.res.append(temp)


		for i in range(len(s)):
			if s[0:i+1] != s[0:i+1][::-1]:
				continue
			self.trace(temp+[s[0:i+1]],s[i+1:])
a = Solution()
print(a.partition("aab"))

