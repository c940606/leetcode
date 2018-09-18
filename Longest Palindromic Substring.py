class Solution(object):
	def longestPalindrome(self, s):
		"""
		给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
		----
		输入: "babad"
		输出: "bab"
		注意: "aba"也是一个有效答案。
		===
		输入: "cbbd"
		输出: "bb"
		--
		思路:

		:type s: str
		:rtype: str
		"""
		n = len(s)
		if n < 2 or s == s[::-1]:
			return s
		max_len = 1
		start = 0
		for i in range(1,n):
			even = s[i-max_len:i+1]
			odd = s[i-max_len-1:i+1]
			if i-max_len-1>=0 and odd == odd[::-1]:
				start = i-max_len-1
				max_len += 2
				continue
			if i-max_len>=0 and even == even[::-1]:
				start = i-max_len
				max_len += 1
		return s[start:start+max_len]
a = Solution()
print(a.longestPalindrome("babad"))

