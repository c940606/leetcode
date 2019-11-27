from typing import List


class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque
        graph = defaultdict(list)

        self.res = -1
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def bfs(i):
            depth = defaultdict(int)
            queue = deque([i])
            visited = set([i])
            while queue:
                i = queue.pop()
                for j in graph[i]:
                    if j not in visited:
                        depth[j] = depth[i] + 1
                        visited.add(j)
                        queue.appendleft(j)
            point = -1
            for i, d in depth.items():
                if d > self.res:
                    self.res = d
                    point = i
            return point

        bfs(bfs(0))
        return self.res


a = Solution()
print(a.treeDiameter([[0, 1], [0, 2]]))
print(a.treeDiameter([[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]]))
