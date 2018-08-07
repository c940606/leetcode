class Solution:
	def getRow(self, rowIndex):
		"""
		给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
		---
		输入: 3
		输出: [1,3,3,1]
		:type rowIndex: int
		:rtype: List[int]
		"""
		res = [1 for _ in range(rowIndex+1)]
		for i in range(2,rowIndex+1):
			for j in range(i-1,0,-1):
				res[j] += res[j-1]
		return res
a = Solution()
print(a.getRow(3))
la