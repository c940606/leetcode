from typing import List


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)



        for x, y in connections:
            union(x, y)

        num = len(set(find(i) for i in range(n)))
        return num - 1

a = Solution()
print(a.makeConnected(n = 4, connections = [[0,1],[0,2],[1,2]]))
print(a.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]))
print(a.makeConnected(n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]))
print(a.makeConnected(n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]))
