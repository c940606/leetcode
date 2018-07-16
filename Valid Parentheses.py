class Solution:
	def isValid(self, s):
		"""
		给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
		--------------------------
		输入: "()"
		输出: true
		输入: "()[]{}"
		输出: true
		:type s: str
		:rtype: bool
		"""
		lookup={
			"(":")",
			"[":"]",
			"{":"}"
		}

		if s == "":
			return  False
		left_list = []
		i= 0
		for item in s:
			if item in list(lookup.keys()):
				left_list.append(item)
			else:
				if len(left_list) != 0 and lookup[left_list.pop()]==item:
					continue
				else:
					return False
		if len(left_list) == 0:
			return True
		else:
			return False

s1= "()"
s2="()[]{}"
s3 ="(]"
s4 ="([)]"
s5 ="{[]}"
a = Solution()
print(a.isValid(s1))
print(a.isValid(s2))
print(a.isValid(s3))
print(a.isValid(s4))
print(a.isValid(s5))

