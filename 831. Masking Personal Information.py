class Solution(object):
	def maskPII(self, S):
		"""
		:type S: str
		:rtype: str
		"""
		# 邮箱
		idx = S.find("@")
		if idx != -1:
			S = S.lower()
			tmp = S[:idx]
			return tmp[0]+"*"*5+tmp[-1]+S[idx:]
		else:
			S = [x for x in S if x.isdigit()]
			n = len(S)
			if n == 10:
				return "*"*3+"-"+"*"*3+"-"+"".join(S[-4:])
			else:
				return "+"+"*"*(n-10)+"-"+"*"*3+"-"+"*"*3+"-"+"".join(S[-4:])

a = Solution()
# print(a.maskPII("LeetCode@LeetCode.com"))
# print(a.maskPII("AB@qq.com"))
print(a.maskPII("1(234)567-890"))
print(a.maskPII("86-(10)12345678"))