class Solution(object):
	def allPathsSourceTarget(self, graph):
		"""
		给一个有 n 个结点的有向无环图，
		找到所有从 0 到 n-1 的路径并输出（不要求按顺序）
		二维数组的第 i 个数组中的单元都表示有向图中 i 号结点所能到达的下一些结点
		（译者注：有向图是有方向的，即规定了a→b你就不能从b→a）空就是没有下一个结点了。
		---
		示例:
		输入: [[1,2], [3], [3], []]
		输出: [[0,1,3],[0,2,3]]
		解释: 图是这样的:
		0--->1
		|    |
		v    v
		2--->3
		这有两条路: 0 -> 1 -> 3 和 0 -> 2 -> 3.

		:type graph: List[List[int]]
		:rtype: List[List[int]]
		"""
		res = []
		if not graph:
			return res
		n = len(graph)
		def helper(graph,temp,idx):
			if idx == n-1:
				res.append(temp)
				return
			for loc in graph[idx]:
				helper(graph,temp+[loc],loc)
		helper(graph,[0],0)
		return res

	def allPathsSourceTarget1(self, graph):
		n = len(graph)-1
		paths = [[0]]
		res = []
		while paths:
			path = paths.pop()
			for i in graph[path[-1]]:
				if i == n:
					res.append(path + [i])
				else:
					paths.append(path + [i])
		return res
a = Solution()
print(a.allPathsSourceTarget1([[1,2], [3], [3], []] ))
