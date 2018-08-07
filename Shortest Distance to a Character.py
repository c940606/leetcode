class Solution:
	def shortestToChar(self, S, C):
		"""
		给定一个字符串 S 和一个字符 C。返回一个代表字符串 S 中每个字符到字符串 S 中的字符 C 的最短距离的数组。
		---
		输入: S = "loveleetcode", C = 'e'
		输出: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
		---
		思路:
		1. 找出查找字符的索引值
		2. 找与索引值相减最小值
		:type S: str
		:type C: str
		:rtype: List[int]
		"""
		n = len(S)
		res = []
		look = self.look_str_index(S,C)
		# n_look = len(look)
		look_index = 0
		for i in range(n):
			if i < look[0]:
				# print("1")
				res.append(look[0]-i)
			elif i > look[-1]:
				# print("2")
				res.append(i-look[-1])
			else:
				if look[look_index] == i:
					print(look[look_index])
					look_index += 1
					res.append(0)
				elif look[look_index] > i:
					res.append( min(map(lambda x:abs(x-i),[look[look_index-1],look[look_index]])))
		return res


	def look_str_index(self,S,C):
		str_index = []
		for index,value in enumerate(S):
			if value == C:
				str_index.append(index)
		print(str_index)
		return str_index

a = Solution()
S = "loveleetcode"
C = 'e'
print(a.shortestToChar(S,C))
