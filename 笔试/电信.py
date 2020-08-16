import sys

graph = []
points = set()
while f := input():
    graph.append(list(map(int, f.split(","))))
    points.add(graph[-1][0])
    points.add(graph[-1][1])
print(graph)
f = {}
def find(x):
    f.setdefault(x, x)
    if f[x] != x:
        f[x] = find(f[x])
    return f[x]

def union(x, y):
    f[find(y)] = find(x)

n = len(points)
res = 0
count = 0
for x, y, w in sorted(graph, key=lambda x: x[2]):
    if find(x) != find(y):
        union(x, y)
        res += w
        count += 1
        if count == n - 1:
            print(res)
            sys.exit()
print(-1)
