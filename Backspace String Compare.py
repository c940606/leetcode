class Solution(object):
	def backspaceCompare(self, S, T):
		"""
		给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符
		---
		输入：S = "ab#c", T = "ad#c"
		输出：true
		解释：S 和 T 都会变成 “ac”。
		---
		输入：S = "ab##", T = "c#d#"
		输出：true
		解释：S 和 T 都会变成 “”。
		:type S: str
		:type T: str
		:rtype: bool
		"""
		S_list = []
		for item in S:
			if item == "#":
				if  S_list:
					S_list.pop()
				continue
			S_list.append(item)
		T_list = []
		for item in T:
			if item == "#":
				if  T_list:
					T_list.pop()
				continue
			T_list.append(item)
		# print(S_list,T_list)
		return S_list == T_list
a = Solution()
print(a.backspaceCompare(S = "ab#c", T = "ad#c"))

