from typing import  List
class Solution:
    def isBipartite4(self, graph) -> bool:
        n = len(graph)
        lookup = set()
        for g in graph:
            lookup |= set(g)
        # print(lookup)
        A = []
        B = set()
        # for idx,tmp in enumerate(graph):
        #         #     if idx in A  or idx in B:
        #         #         continue
        #         #     else:
        #         #         A.add(idx)
        #         #         B.update(tmp)
        self.visited = set()

        def helper1(res, tmp):
            # print(res,tmp)
            if not tmp:
                if tmp not in A:
                    A.append(res)
                return
            for i in tmp:
                if i not in self.visited:
                    self.visited.add(i)
                    # self.visited |= set(graph[i])
                    helper1(res | {i}, tmp - set(graph[i]) - {i})

        tmp = lookup.copy()
        helper1(set(), tmp)

        # print(A)
        def helper(parm):
            for i in parm:
                for t in graph[i]:
                    if t in parm:
                        return False
            return True

        for a in A:
            # print(lookup)
            b = lookup - a
            print(a, b)
            if helper(a) and helper(b):
                return True
        return False

    def isBipartite1(self, graph) -> bool:
        n = len(graph)
        # red 1 bule -1
        colors = [0] * n

        def helper(i, color):
            if colors[i] != 0:
                return colors[i] == color
            colors[i] = color
            for tmp in graph[i]:
                if not helper(tmp, -color):
                    return False
            return True

        for i in range(n):
            if colors[i] == 0 and not helper(i, 1):
                return False
        print(colors)
        return True

    def isBipartite2(self, graph) -> bool:
        from collections import deque
        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] != 0: continue
            stack = deque()
            stack.appendleft(i)
            colors[i] = 1
            while stack:
                cur = stack.pop()
                for tmp in graph[cur]:
                    if colors[tmp] == 0:
                        colors[tmp] = -colors[cur]
                        stack.appendleft(tmp)
                    elif colors[tmp] == colors[cur]:
                        return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:

        visited = set()

        for idx, item in enumerate(graph):
            print(visited)
            if idx in visited:
                for t in item:
                    if t in visited:
                        return False
            else:
                for t in item:
                    visited.add(t)

        return True



a = Solution()
# print(a.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]))
# print(a.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]))
print(a.isBipartite([[1], [0, 3], [3], [1, 2]]))
print(a.isBipartite2(
    [[], [], [5], [7], [], [2], [], [3], [], [], [17, 19], [15, 18], [15, 16, 17, 19], [15, 16, 18, 19], [15, 16, 18],
     [11, 12, 13, 14], [12, 13, 14], [10, 12], [11, 13, 14], [10, 12, 13], [25, 26, 27, 28, 29], [25, 26, 27, 28, 29],
     [25, 26, 27, 28, 29], [25, 26, 27, 28, 29], [25, 26, 27, 28, 29], [20, 21, 22, 23, 24], [20, 21, 22, 23, 24],
     [20, 21, 22, 23, 24], [20, 21, 22, 23, 24], [20, 21, 22, 23, 24], [], [36], [], [37], [], [], [31], [33], [], [],
     [45, 46, 47, 48, 49], [45, 46, 48, 49], [45], [47, 48, 49], [45], [40, 41, 42, 44], [40, 41], [40, 43],
     [40, 41, 43], [40, 41, 43], [55, 56, 57, 58, 59], [55, 56, 57, 58, 59], [55, 56, 57, 58, 59], [55, 56, 57, 58, 59],
     [55, 56, 57, 58, 59], [50, 51, 52, 53, 54], [50, 51, 52, 53, 54], [50, 51, 52, 53, 54], [50, 51, 52, 53, 54],
     [50, 51, 52, 53, 54], [66, 68], [65, 66, 67], [65, 66, 67, 68, 69], [65, 66, 67, 69], [65, 67, 68, 69],
     [61, 62, 63, 64], [60, 61, 62, 63], [61, 62, 63, 64], [60, 62, 64], [62, 63, 64], [75, 76, 77, 78, 79],
     [75, 76, 77, 78, 79], [75, 76, 77, 78, 79], [75, 76, 77, 78, 79], [76, 77, 78, 79], [70, 71, 72, 73],
     [70, 71, 72, 73, 74], [70, 71, 72, 73, 74], [70, 71, 72, 73, 74], [70, 71, 72, 73, 74], [85], [86, 87], [88],
     [85, 86, 87, 89], [85, 86, 88, 89], [80, 83, 84], [81, 83, 84], [81, 83], [82, 84], [83, 84], [95, 96, 98, 99],
     [95, 96, 97, 98, 99], [95, 96, 97, 98, 99], [95, 96, 97, 98, 99], [95, 96, 97, 98, 99], [90, 91, 92, 93, 94],
     [90, 91, 92, 93, 94], [91, 92, 93, 94], [90, 91, 92, 93, 94], [90, 91, 92, 93, 94]]))
