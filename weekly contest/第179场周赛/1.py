from typing import List


class Solution:
    def frogPosition1(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        from collections import defaultdict
        graph = defaultdict(list)
        for a, b in edges:
            a, b = sorted([a, b])
            graph[a].append(b)
        route = []

        def dfs(root, cur):

            nonlocal route
            # print(root, cur)
            if root == target:
                # print(cur,graph[target],len(cur) < t )
                if graph[target] and len(cur) <= t:
                    cur += ["A"]
                route = cur
                return
            for node in graph[root]:
                dfs(node, cur + [node])

        dfs(1, [1])
        # print(route)
        if not route or len(route) - 1 > t or route[-1] != target:
            return 0
        res = 1
        for it in route:
            if graph[it]:
                res *= (1 / len(graph[it]))
        return res

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        from collections import defaultdict, deque
        graph = defaultdict(list)

        for a, b in edges:
            a, b = sorted([a, b])
            graph[a].append(b)

        queue = deque([[1, 1]])
        while queue and t >= 0:
            # print(queue, t)
            t -= 1
            n = len(queue)
            for _ in range(n):
                root, prob = queue.pop()
                if root == target :
                    # print(t, graph[root])
                    if t < 0 or not graph[root]:
                        return prob
                    else:
                        return 0
                for node in graph[root]:
                    queue.appendleft([node, prob * (1/ len(graph[root]))])
        return 0



a = Solution()
print(a.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=20, target=6))
#
print(a.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=1, target=7))
print(a.frogPosition(3, [[2, 1], [3, 2]], 1, 2))  # 1
print(a.frogPosition(8, [[2, 1], [3, 2], [4, 1], [5, 1], [6, 4], [7, 1], [8, 7]], 7, 7))
print(a.frogPosition(7, [[2, 1], [3, 1], [4, 2], [5, 4], [6, 5], [7, 2]], 3, 2))
print(a.frogPosition(n=7, edges=[[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], t=20, target=6))
print(a.frogPosition(22, [[2, 1], [3, 1], [4, 2], [5, 2], [6, 4], [7, 4], [8, 4], [9, 3], [10, 4], [11, 4], [12, 5],
                          [13, 8], [14, 9], [15, 10], [16, 7], [17, 7], [18, 15], [19, 9], [20, 11], [21, 16], [22, 19]]
                     , 4, 7))
#