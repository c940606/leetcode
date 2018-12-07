class Solution(object):
	def pyramidTransition(self, bottom, allowed):
		"""
		:type bottom: str
		:type allowed: List[str]
		:rtype: bool
		"""
		lookup = {}
		for item in allowed:
			if item[:-1] not in lookup:
				lookup[item[:-1]] = [item[-1]]
			else:
				lookup[item[:-1]].append(item[-1])
		def getList(bottom,idx,s,ls,n):
			if idx == n - 1:
				ls.append(s)
				return
			for com_str in lookup[bottom[idx:idx+2]]:
				getList(bottom,idx+1,s+com_str,ls,n)
		def helper(bottom):
			n = len(bottom)
			if n == 1:
				return True
			for i in range(n-1):
				if bottom[i:i+2] not in lookup:
					return False
			ls = []
			getList(bottom,0,"",ls,n)
			print(ls)
			for l in ls:
				if helper(l):
					return True
			return False

		return helper(bottom)


class Solution(object):
	def pyramidTransition(self, bottom, allowed):
		"""
		:type bottom: str
		:type allowed: List[str]
		:rtype: bool
		"""
		lookup = {}
		# 用前两个字母最为键,找出所有由前两个字母的字符串
		for item in allowed:
			if item[:2] not in lookup:
				lookup[item[:2]] = [item[2]]
			else:
				lookup[item[:2]].append(item[2])

		# 判读这一层是否可以垒到上一层
		def helper(bottom):
			n = len(bottom)
			if n == 1:
				return True
			for i in range(n - 1):
				if bottom[i:i + 2] not in lookup:
					return False
			# 找下一层字符串
			next_strs = []
			getList(bottom, 0, n, "", next_strs)
			for next_str in next_strs:
				if helper(next_str):
					return True
			return False

		# 找下一层的所有字符串的可能
		def getList(bottom, idx, n, temp, next_strs):
			if idx == n - 1:
				next_strs.append(temp)
				return
			for com_str in lookup[bottom[idx:idx + 2]]:
				getList(bottom, idx + 1, n, temp + com_str, next_strs)

		return helper(bottom)
a = Solution()
print(a.pyramidTransition(bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]))
print(a.pyramidTransition(bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]))