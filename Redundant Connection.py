class UnionFind(object):
	def __init__(self, size):
		self.representative = [i for i in range(size)]

	def find(self, node):
		# if self.representative[node] != node:
		# 	self.representative[node] = self.find(self.representative[node])
		while node != self.representative[node]:
			node = self.representative[node]
		return self.representative[node]

	def union(self, nodex, nodey):
		self.representative[self.find(nodex)] = self.find(nodey)


class Solution(object):
	def findRedundantConnection(self, edges):
		"""
		:type edges: List[List[int]]
		:rtype: List[int]
		"""

		union_find = UnionFind(2001)  # Since every integer represented in the 2D-array will be between 1 and 2000.

		for u, v in edges:
			print(u,v)
			print("前：",union_find.representative[:6])
			if union_find.find(u) == union_find.find(v):
				return [u, v]
			union_find.union(u, v)
			print("后：", union_find.representative[:6])
		return []
a = Solution()
print(a.findRedundantConnection([[1,2] ,[2,4],[1,3], [2,3]]))
# print(a.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
class Union:
	def __init__(self):
		self.lookup = [i for i in range(20001)]
	def find(self,node):
		while node != self.lookup[node]:
			node = self.lookup[node]
		return self.lookup[node]
	def union(self,x,y):
		self.lookup[self.find(x)] = self.find(y)
class Solution1(object):
	def findRedundantConnection(self, edges):
		"""
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		union_find = Union()
		for u ,v in edges:
			if union_find.find(u) == union_find.find(v):
				return [u,v]
			union_find.union(u,v)
		return []
class Solution2(object):
	def findRedundantConnection(self, edges):
		"""
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		lookup = {}
		def root(p):
			while p != lookup[p]:
				p = lookup[p]
			return p
		for u,v in edges:
			lookup[u] = v
			lookup[v] = u
			print(lookup)
		for u,v in edges:
			ru,rv = root(u),root(v)
			if ru == rv:
				return [u,v]
			lookup[ru] = rv
# b = Solution1()
# print(b.findRedundantConnection([[1,2], [1,3], [2,3]]))
# print(b.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
