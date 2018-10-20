class Solution(object):
	def minAddToMakeValid(self, S):
		"""
		:type S: str
		:rtype: int
		"""
		if not S:
			return 0
		stack = []
		count = 0
		i = 0
		n = len(S)
		while i < n:
			if S[i] == "(":
				stack.append(S[i])
			elif S[i] == ")":
				if  stack:
					stack.pop()
				else:
					count += 1
			i += 1
		print(stack)
		return len(stack) + count
a = Solution()
print(a.minAddToMakeValid("())"))