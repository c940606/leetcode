class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):
        from collections import defaultdict, deque
        red_edges_dict = defaultdict(list)
        blue_edges_dict = defaultdict(list)
        res = [-1] * n

        queue = deque()

        for x, y in red_edges:
            red_edges_dict[x].append(y)
            # red_edges_dict[y].append(x)

        for x, y in blue_edges:
            blue_edges_dict[x].append(y)
            # blue_edges_dict[y].append(x)

        # 初始化队列 red -1 blue 1
        for i in red_edges_dict[0]:
            queue.appendleft((i, -1))
        for i in blue_edges_dict[0]:
            queue.appendleft((i, 1))
        visited = set()
        step = 1
        res[0] = 0
        while queue:
            #print(queue)
            c = len(queue)
            for _ in range(c):
                x, y = queue.pop()
                if (x, y) in visited:
                     continue

                if (x, y) not in visited:
                    if res[x] == -1:
                        res[x] = step
                    visited.add((x, y))
                if y == -1:
                    for i in blue_edges_dict[x]:
                        queue.appendleft((i, 1))
                else:
                    for i in red_edges_dict[x]:
                        queue.appendleft((i, -1))
            step += 1
        return res


a = Solution()
# print(a.shortestAlternatingPaths(n=3, red_edges=[[0, 1], [1, 2]], blue_edges=[]))
# print(a.shortestAlternatingPaths(n=3, red_edges=[[0, 1], [0, 2]], blue_edges=[[1, 0]]))
# print(a.shortestAlternatingPaths(n=3, red_edges=[[1, 0]], blue_edges=[[2, 1]]))
# print(a.shortestAlternatingPaths(n=3, red_edges=[[0, 1]], blue_edges=[[1, 2]]))
print(a.shortestAlternatingPaths(5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[1, 2], [2, 3], [3, 1]]))
print(a.shortestAlternatingPaths(3, [[0, 1], [0, 2]], [[1, 0]]))
print(a.shortestAlternatingPaths(5, [[3, 2], [4, 1], [1, 4], [2, 4]], [[2, 3], [0, 4], [4, 3], [4, 4], [4, 0], [1, 0]]))
