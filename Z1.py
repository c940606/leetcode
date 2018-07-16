class Solution:
	def convert(self, s, numRows):
		"""
		:type s: str
		:type numRows: int
		:rtype: str
		"""
		n = len(s)
		num = 0
		while numRows + 2 * (numRows - 1) * num < n:
			num += 1
		col = 1 + (numRows - 1) * num
		maxic = [[None] * col for _ in range(numRows)]
		# 填充位置
		i = 0
		j = 0
		for item in s:
			if j % (numRows - 1) == 0:
				maxic[i][j] = item
				i += 1
				if i == numRows:
					j += 1
					i -= 2
			else:
				maxic[i][j] = item
				i -= 1
				j += 1
				if i == -1:
					i += 2
					j -= 1
		Z_list = []
		for i in range(len(maxic)):
			for j in range(len(maxic[0])):
				if maxic[i][j] != None:
					Z_list.append(maxic[i][j])
		return "".join(Z_list)
s = "PAYPALISHIRING"
a = Solution()
print(a.convert(s, 4))