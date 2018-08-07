class Solution:
	def binaryGap(self, N):
		"""
		给定一个正整数 N，找到并返回 N 的二进制表示中两个连续的 1 之间的最长距离。
		如果没有两个连续的 1，返回 0 。
		:type N: int
		:rtype: int
		"""
		s = bin(N)
		index = []
		for i,v in enumerate(s[2:]):
			if v == "1":
				index.append(i)
		if len(index)<=1:
			return 0
		else:
			print(index)
			# print(list(map(lambda x:index[x]-index[x-1],range(1,len(index)))))
			return max(map(lambda x:index[x]-index[x-1],range(1,len(index))))
a = Solution()
print(a.binaryGap(6))




