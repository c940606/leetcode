import  math
class Solution:
	def uniquePaths(self, m, n):
		"""
		一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
		机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
		问总共有多少条不同的路径？
		----
		输入: m = 3, n = 2
		输出: 3
		解释:
		从左上角开始，总共有 3 条路径可以到达右下角。
		1. 向右 -> 向右 -> 向下
		2. 向右 -> 向下 -> 向右
		3. 向下 -> 向右 -> 向右
		:type m: int
		:type n: int
		:rtype: int
		"""
		dp = [[1]*m for _ in range(n)]


		for i in range(1,n):
			for j in range(1,m):
				dp[i][j] = dp[i-1][j] + dp[i][j-1]
		return dp[-1][-1]

	def uniquePaths1(self, m, n):
		return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1))
a = Solution()
print(a.uniquePaths(3,2))
