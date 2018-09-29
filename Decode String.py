class Solution(object):
	def decodeString(self, s):
		"""
		给定一个经过编码的字符串，返回它解码后的字符串。
		编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
		你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
		此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
		--
		s = "3[a]2[bc]", 返回 "aaabcbc".
		s = "3[a2[c]]", 返回 "accaccacc".
		s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
		--
		思路:
		如果是 数字 把后面中括号你字母找出来
		如果不是 不找
		:type s: str
		:rtype: str
		"""
		if not s:
			return ""
		res = ""
		i = 0
		n = len(s)
		while i < n:
			if s[i].isdigit():
				beg = i
				while s[i].isdigit():
					i += 1
				num = int(s[beg:i])
				print(num)
				temp_lc = i

				while s[i] != "]":

					i += 1
				temp = s[temp_lc+1:i]
				i += 1

				res += (num*(temp))
			else:
				res += s[i]
				i += 1
		return res

	def decodeString1(self, s):
		if not s:
			return ""
		stack = []
		i = 0
		n = len(s)
		res = ""
		while i < n:
			print(stack)
			if s[i] == "]":
				s_temp = ""
				num_temp = ""
				while stack and stack[-1].isalpha():
					s_temp = stack.pop() + s_temp
				print(s_temp)
				stack.pop()
				while stack and stack[-1].isdigit():
					num_temp = stack.pop() + num_temp
				print(num_temp)

				if not num_temp:
					num_temp = 1
				stack.extend(int(num_temp)*s_temp)
				i += 1
			else:
				stack.append(s[i])
				i += 1
		return "".join(stack)
a = Solution()
print(a.decodeString1("3[z]2[2[y]pq4[2[jk]e1[f]]]ef",))