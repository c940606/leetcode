class Solution(object):
	def repeatedStringMatch(self, A, B):
		"""
		给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。
		举个例子，A = "abcd"，B = "cdabcdab"。
		答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。
		注意:
		 A 与 B 字符串的长度在1和10000区间范围内。
		 ---

		:type A: str
		:type B: str
		:rtype: int
		"""
		n_b = len(B)
		n_a = len(A)
		if n_b < n_a:
			if B in A:
				return 1
			elif B in A * 2:
				return 2
			else:
				return -1
		num = n_b // n_a
		print(num)
		while B not in A * (num):
			if len(B)*2 < len(A*(num)):
				return -1
			print(B,A*num)
			num += 1

		return num
a = Solution()
print(a.repeatedStringMatch("abaabaa","abaababaab"))
print(a.repeatedStringMatch("abcbc","cabcbca"))