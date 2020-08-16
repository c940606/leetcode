from typing import List


class Solution:
	def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
		num = n
		n = len(edges)

		for i in range(n):
			edges[i].append(i)

		edges.sort(key=lambda x: x[2])
		# print(edges)

		f = {}

		def find(x):
			f.setdefault(x, x)
			if f[x] != x:
				f[x] = find(f[x])
			return f[x]

		def union(x, y):
			f[find(y)] = find(x)

		def clear():
			f.clear()


		def getMST(block, pre=-1):
			# print("b", f)
			clear()
			weight = 0
			if pre != -1:
				weight += edges[pre][2]
				union(edges[pre][0], edges[pre][1])

			for i in range(n):
				if i == block: continue
				if find(edges[i][0]) == find(edges[i][1]): continue
				weight += edges[i][2]
				union(edges[i][0], edges[i][1])
				# print(i)

			# print(f)
			for i in range(num):
				# print(find(i), find(0))
				if find(i) != find(0):
					return float("inf")
			# print("l", f)
			clear()
			return weight

		prev = getMST(-1)
		print(prev)
		a, b = [], []
		for i in range(n):
			print(getMST(i))
			if prev < getMST(i):
				a.append(edges[i][3])
			elif prev == getMST(-1, i):
				b.append(edges[i][3])
		return [a, b]
a = Solution()
# print(a.findCriticalAndPseudoCriticalEdges(n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]))
# print(a.findCriticalAndPseudoCriticalEdges(n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]))
print(a.findCriticalAndPseudoCriticalEdges(4,
[[0,1,1],[0,2,2],[0,3,3]]))