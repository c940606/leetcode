class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		给定一个字符串，找出不含有重复字符的最长子串的长度。
		---
		输入: "abcabcbb"
		输出: 3
		解释: 无重复字符的最长子串是 "abc"，其长度为 3。
		---
		思路:
		例如 输入"abcabcbb"
		abc 当选到a 时候,我们要把上一个a位置向后移一位
		:type s: str
		:rtype: int
		"""
		lookup = {}

		pre = 0
		res  = 0
		for i,c in enumerate(s):
			print(lookup)
			if  c in lookup and pre<=lookup[c]:
				pre  = lookup[c]+1
				print("if",pre)
			lookup[c] = i
			res = max(res,i-pre+1)
			print(res)
		return res
a = Solution()
# print(a.lengthOfLongestSubstring("abcabcbb"))
print(a.lengthOfLongestSubstring("abba"))