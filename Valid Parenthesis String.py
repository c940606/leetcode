class Solution(object):
	def checkValidString(self, s):
		"""
		给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
		任何左括号 ( 必须有相应的右括号 )。
		任何右括号 ) 必须有相应的左括号 ( 。
		左括号 ( 必须在对应的右括号之前 )。
		* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
		一个空字符串也被视为有效字符串。
		---
		输入: "()"
		输出: True
		---
		输入: "(*)"
		输出: True
		---
		输入: "(*))"
		输出: True
		:type s: str
		:rtype: bool
		"""
		star = 0
		stack = []
		n = len(s)
		i = 0
		while i < n:
			# print(i)
			if s[i] == "(":
				stack.append("(")
			elif s[i] == "*":
				stack.append("*")
			elif s[i] == ")":
				if not stack:
					return False
				elif stack[-1] == "(":
					stack.pop()
				else:
					t = len(stack)-1
					# print(stack,n)
					while t>=0 and stack[t] == "*":
						t -= 1
					# print(stack,t)
					if t >=0:
						stack.pop(t)
					else:
						stack.pop()
			i += 1
		print(stack)
		if "(" in stack:
			return False
		return True


a  = Solution()
# print(a.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
print(a.checkValidString("(*()"))

