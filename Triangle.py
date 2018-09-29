class Solution:
	def minimumTotal(self, triangle):
		"""
		给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
		:type triangle: List[List[int]]
		:rtype: int
		---
		[
		 [2],
		[3,4],
	   [6,5,7],
	  [4,1,8,3]
		]
		自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
		---
		思路:
		先建立和题中构造一样的结构
		1.边界
			直接上一个边界加上来就行
		2. 中间
			同一位置 和 旁边位置最小值
		"""
		n = len(triangle)
		if n==0:
			return 0
		res = [[0]*i for i in range(1,n+1)]
		res[0][0] = triangle[0][0]

		for i in range(1,n):
			for k in range(i+1):
				print(i,k)
				print(res)
				if k == 0 :
					res[i][k] = res[i-1][k] + triangle[i][k]
				elif k == i:
					res[i][k] = res[i-1][k-1] + triangle[i][k]
				else:
					print("..")
					res[i][k] = min(res[i-1][k-1]+triangle[i][k],res[i-1][k]+triangle[i][k])
		return min(res[-1])
# a = Solution()
# print(a.minimumTotal())


a = Solution()
t = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
t1 = [[-1],[2,3],[1,-1,-3]]
print(a.minimumTotal(t1))
