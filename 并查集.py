# https://www.cnblogs.com/xzxl/p/7226557.html
class UnionFind():
    def __init__(self):
        self.father = {}

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

    def union(self, x, y):
        self.father[self.find(y)] = self.find(x)


u = UnionFind()
u.union(1, 2)
u.union(2, 3)
u.union(3, 6)
u.union(4, 5)
print(u.father)
