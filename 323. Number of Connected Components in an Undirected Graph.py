from typing import List


class Solution:
    def countComponents1(self, n: int, edges: List[List[int]]) -> int:
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for x, y in edges:
            union(x, y)

        return len(set(find(x) for x in range(n)))

    def countComponents2(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()

        def dfs(i):
            visited.add(i)
            for j in graph[i]:
                if j not in visited:
                    dfs(j)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()

        def bfs(i):
            queue = deque([i])
            while queue:
                i = queue.pop()
                for j in graph[i]:
                    if j not in visited:
                        visited.add(j)
                        queue.appendleft(j)

        res = 0
        for i in range(n):
            if i not in visited:
                res += 1
                visited.add(i)
                bfs(i)
        return res


a = Solution()
print(a.countComponents(5, [[0, 1], [1, 2], [3, 4]]))
