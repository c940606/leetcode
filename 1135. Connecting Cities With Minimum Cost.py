class Solution:
    def minimumCost1(self, N: int, connections: List[List[int]]) -> int:
        import heapq
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        res = 0
        heap = []
        edge = 0
        for x, y, c in connections:
            heapq.heappush(heap, [c, x, y])
        while heap:
            c, x, y = heapq.heappop(heap)
            if find(x) != find(y):
                res += c
                union(x, y)
                edge += 1
                if edge == N - 1: return res
        return -1

    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for x, y, c in connections:
            graph[x][y] = min(c, graph[x][y])
            graph[y][x] = min(c, graph[y][x])
        heap = []
        visited = set()
        edge = 0
        res = 0
        while heap:
            c, y = heapq.heappop(heap)
            if y in visited: continue
            res += c
            edge += 1
            visited.add(y)
            if edge == N - 1:
                return res
            for z, c in graph[y].items():
                heapq.heappush(heap, [c, z])
        return -1
