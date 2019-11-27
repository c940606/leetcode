from collections import defaultdict
import sys
# areas = int(input())
areas = 4
if areas == 1:
    print(0)
    sys.exit()
# n = int(input())
#
# graph = [[0] * areas for _ in range(areas)]
# g = defaultdict(list)
# for _ in range(n):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c
#     graph[b][a] = c
#     g[a].append(b)
#     g[b].append(a)
# print(graph, g)
graph = [[0, 4, 3, 1], [4, 0, 1, 2], [3, 1, 0, 5], [1, 2, 5, 0]]
g = {0: [1, 2, 3], 1: [0, 2, 3], 2: [0, 1, 3], 3: [0, 1, 2]}
res = float("inf")

def dfs(i,tmp, visited):
    global  res
    if len(visited) == areas:
        #print(visited)
        if 0 in g[visited[-1]]:
            res = min(res, tmp + graph[visited[-1]][0])
        return
    for j in g[i]:
        if j not in visited:
            visited.append(j)
            dfs(j, tmp + graph[i][j],visited)
            visited.pop()


dfs(0, 0, [0])
if res == float("-inf"):
    print(-1)
else:
    print(res)