class Solution(object):
	def scoreOfParentheses(self, S):
		"""
		给定一个平衡括号字符串 S，按下述规则计算该字符串的分数：

		() 得 1 分。
		AB 得 A + B 分，其中 A 和 B 是平衡括号字符串。
		(A) 得 2 * A 分，其中 A 是平衡括号字符串。
		:type S: str
		:rtype: int
		"""
		if not S:
			return 0
		stack = []
		for s in S:
			if s == "(":
				stack.append(-1)
			else:
				cur = 0
				while stack[-1] != -1:
					cur += stack.pop()
				stack.pop()
				stack.append(cur * 2 if cur != 0 else 1)
		return sum(stack)


a = Solution()
print(a.scoreOfParentheses("(()(()))"))
