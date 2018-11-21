class Solution(object):
	def diStringMatch(self, S):
		"""
		:type S: str
		:rtype: List[int]
		"""
		lookup = {"I":[],"D":[]}
		for idx,alp in enumerate(S):
			if alp == "I":
				lookup["I"].append(idx)
			if alp == "D":
				lookup["D"].append(idx)
		# print(lookup)
		n = len(S)
		res = [0]*(n+1)
		if S[-1] == "D":
			lookup["I"].append(n)
		if S[-1] == "I":
			lookup["D"].append(n)
		# print(lookup)
		num1 = 0
		for i in lookup["I"]:
			res[i] = num1
			num1 += 1
		num2 = n
		for j in lookup["D"]:
			res[j] = num2
			num2 -= 1
		return res
a = Solution()
print(a.diStringMatch("IDID"))
print(a.diStringMatch("III"))
print(a.diStringMatch("DDI"))