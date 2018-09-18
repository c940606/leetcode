class Solution:
	def isPalindrome(self, s):
		"""
		给定一个字符串，验证它是否是回文串，
		只考虑字母和数字字符，可以忽略字母的大小写。
		--
		输入: "A man, a plan, a canal: Panama"
		输出: true
		---
		输入: "race a car"
		输出: false
		:type s: str
		:rtype: bool
		"""
		jup = ""
		for val in s :
			if val.isalnum():
				jup += val.lower()
		return jup == jup[::-1]
	def isPalindrome1(self, s):
		new_s = list(map(lambda x: x.lower() if x.isalnum() else None, s))
		print(new_s)
		return new_s == new_s[::-1]
a = Solution()
print(a.isPalindrome1("race a car"))
