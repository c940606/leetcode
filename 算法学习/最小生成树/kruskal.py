""":arg
ksural算法
按权值从小到大, 看两个点是否在同一流通变量, 不是就连起来
当连线和节点个数-1时候,说明所有点都连起来了
"""
# 点的个数
N = 3
graph = [[1, 2, 5], [1, 3, 6], [2, 3, 1]]


def kruskal(N, graph):
    f = {}

    def find(x):
        f.setdefault(x, x)
        if f[x] != x:
            f[x] = find(f[x])
        return f[x]

    # x作为父节点
    def union(x, y):
        f[find(y)] = find(x)

    all_cost = 0
    edge = 0
    for x, y, cost in sorted(graph, key=lambda x: x[2]):
        if find(x) != find(y):
            union(x, y)
            edge += 1
            all_cost += cost
            if edge == N - 1:
                return all_cost
    return -1


print(kruskal(N, graph))
