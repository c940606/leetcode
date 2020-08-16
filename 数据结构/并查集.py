class UnionFind():
	def __init__(self):
		self.father = {}
		self.size = {}

	def find(self, x):
		self.father.setdefault(x, x)
		# 无压缩路径
		# while self.father[x] != x:
		#     x = self.father[x]
		# return x
		# 压缩路径
		# if self.father[x] == x:
		#     return x
		# else:
		#     self.father[x] = self.find(self.father[x])
		#     return self.father[x]
		if self.father[x] != x:
			self.father[x] = self.find(self.father[x])
		return self.father[x]

		# p = x
		# while x != self.father[x]:
		#     x = self.father[x]
		# while p != x:
		#     t = self.father[p]
		#     self.father[p] = x
		#     p = t
		# return x

	# x为父节点
	def union(self, x, y):
		# self.father[self.find(y)] = self.find(x)

		x_father = self.find(x)
		y_father = self.find(y)
		if x_father != y_father:
			if self.size.setdefault(x_father, 1) < self.size.setdefault(y_father, 1):
				self.father[x_father] = y_father
				self.size[y_father] += self.size[x_father]
			else:
				self.father[y_father] = x_father
				self.size[x_father] += self.size[y_father]


u = UnionFind()
u.union(1, 2)
u.union(2, 3)
u.union(3, 6)
u.union(4, 5)
u.union(4,6)
print(u.father)
