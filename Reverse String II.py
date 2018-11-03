class Solution(object):
	def reverseStr(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: str
		"""
		n = len(s)
		if n < k:
			return s[::-1]
		# if  n < 2*k:
		# 	return s[::-1]
		res = ""
		for i in range(0,n,2*k):
			print(i)
			if i+2*k <= n:
				res += s[i:i+k][::-1] + s[i+k:i+2*k]
			elif i+k <= n and i+2*k > n:
				res += s[i:i+k][::-1] + s[i+k:]
			else:
				res += s[i:][::-1]
		return res
a = Solution()
# print(a.reverseStr(s = "abcdefg", k = 2))
print(a.reverseStr("abcdefg",8))
print(a.reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl",39))