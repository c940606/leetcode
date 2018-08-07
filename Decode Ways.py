class Solution:
	def numDecodings(self, s):
		"""
		一条包含字母 A-Z 的消息通过以下方式进行了编码：
			'A' -> 1
			'B' -> 2
			...
			'Z' -> 26
			给定一个只包含数字的非空字符串，请计算解码方法的总数
		:type s: str
		:rtype: int
		"""
		n = len(s)
		lookup = [0]*n
		if not s or s[0] == "0":
			return 0
		lookup[0] = 1
		if n == 1: return 1
		if n>=1 and s[1]!= "0" and s[0]+s[1] <="26":
			lookup[1] = 2
		elif s[1] == "0" and s[0]>="3":
			lookup[1] = 0
		else:
			lookup[1] = 1
		# return lookup
		temp = 2
		while temp < n:
			if s[temp] == "0":
				if s[temp-1] == "0" or s[temp-1]>="3":
					return 0
				if s[temp-1] + s[temp] <= "26":
					lookup[temp] =  lookup[temp-2]
					temp += 1
					continue
			if s[temp] != "0":
				if s[temp-1] =="0":
					lookup[temp] = lookup[temp-1]
					temp += 1
					continue
				if s[temp-1] + s[temp] <= "26":
					lookup[temp] = lookup[temp-1] +lookup[temp-2]
					temp += 1
					continue
				else:
					lookup[temp] = lookup[temp-1]
					temp += 1
		return lookup






a = Solution()
s = "301"
print(a.numDecodings(s))



