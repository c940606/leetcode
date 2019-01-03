class Solution:
	def solveEquation(self, equation):
		"""
		:type equation: str
		:rtype: str
		"""
		equ = equation.find("=")
		flag = {
			"x": 0,
			"num": 0
		}
		equation_left = equation[:equ]
		equation_right = equation[equ + 1:]
		# print(equation_left)
		# print(equation_right)

		def helper(s):
			n = len(s)
			i = 0
			res = []
			while i < n:
				if s[i] == "+" or s[i] == "-":
					j = i + 1
					while j < n and not (s[j] == "+" or s[j] == "-"):
						j += 1
					# print(s[i:j])
					res.append(s[i:j])
					i = j
				else:
					j = i + 1
					while j < n and not (s[j] == "+" or s[j] == "-"):
						j += 1
					# print(j)
					res.append("+" + s[i:j])
					i = j
			return res

		# print(helper(equation_left))
		# print(helper(equation_right))
		equation_left = helper(equation_left)
		equation_right = helper(equation_right)
		for left in equation_left:
			# print(left)
			if left[-1] == "x":
				if len(left) == 2:
					flag["x"] += int(left[:-1]+"1")
				else:
					flag["x"] += int(left[:-1])
			else:
				flag["num"] += int(left)

		for right in equation_right:
			if right[-1] == "x":
				if len(right) == 2:
					flag["x"] -= int(right[:-1]+"1")
				else:
					flag["x"] -= int(right[:-1])
			else:
				flag["num"] -= int(right)
		# print(flag)
		if flag["x"] == 0:
			if flag["num"] == 0:

				return "Infinite solutions"
			else:
				return "No solution"
		return "x="+str(-1 * flag["num"] // flag["x"])



a = Solution()
print(a.solveEquation("x+5-3+x=6+x-2"))
print(a.solveEquation("x=x"))
print(a.solveEquation("2x=x"))
print(a.solveEquation("2x+3x-6x=x+2"))
print(a.solveEquation("x=x+2"))