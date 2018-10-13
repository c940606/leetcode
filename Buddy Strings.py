class Solution(object):
	def buddyStrings(self, A, B):
		"""
		给定两个由小写字母构成的字符串 A 和 B ，只要我们可以通过交换 A 中的两个字母得到与 B 相等的结果，
		就返回 true ；否则返回 false 。
		---
		输入： A = "ab", B = "ba"
		输出： true
		---
		输入： A = "ab", B = "ab"
		输出： false
		----
		输入： A = "aa", B = "aa"
		输出： true
		---
		输入： A = "aaaaaaabc", B = "aaaaaaacb"
		输出： true
		--
		输入： A = "", B = "aa"
		输出： false
		---
		:type A: str
		:type B: str
		:rtype: bool
		"""
		n1 = len(A)
		n2 = len(B)
		if n1 != n2:
			return False
		i = 0
		count = 0
		res = []
		while i < n1:
			if A[i] != B[i]:
				if count < 3:
					res.append(i)
					count += 1
				else:
					return False
			i += 1
		if len(res) < 2:
			return False
		return A[res[0]] == B[res[1]] and A[res[1]] == B[res[0]]
a = Solution()
print(a.buddyStrings(A = "aaaaaaabc", B = "aaaaaaacb"))


