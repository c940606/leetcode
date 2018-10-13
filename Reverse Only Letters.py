class Solution(object):
	def reverseOnlyLetters(self, S):
		"""
		给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
		---
		输入："ab-cd"
		输出："dc-ba"
		--
		输入："a-bC-dEf-ghIj"
		输出："j-Ih-gfE-dCba"
		---
		输入："Test1ng-Leet=code-Q!"
		输出："Qedo1ct-eeLg=ntse-T!"
		:type S: str
		:rtype: str
		"""
		if not S:
			return ""
		res = []
		other = []
		i = 0
		n = len(S)
		while i < n:
			if S[i].isalpha():
				# print(S[i])
				res.append(S[i])
			else:
				other.append([i,S[i]])
			i += 1
		res = res[::-1]
		for itme in other:
			res.insert(itme[0],itme[1])
		return "".join(res)
a = Solution()
print(a.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
