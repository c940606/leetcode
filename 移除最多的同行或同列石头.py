class Solution(object):
	def removeStones(self, stones):
		"""
		在二维平面上，我们将石头放置在一些整数坐标点上。每个坐标点上最多只能有一块石头。
		现在，move 操作将会移除与网格上的另一块石头共享一列或一行的石头。
		我们最多能执行多少次 move 操作？
		---

		:type stones: List[List[int]]
		:rtype: int
		"""
		n = len(stones)
		flag = [False]*n
		ret = 0
		def dfs(idx):
			flag[idx] = True
			for i in range(n):
				if not flag[i] and (stones[i][0] == stones[idx][0] or stones[i][1] == stones[idx][1]):
					dfs(i)
		for i in range(n):
			if not flag[i]:
				ret += 1
				dfs(i)
		return n - ret

a = Solution()
print(a.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
print(a.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
print(a.removeStones( [[0,0]]))