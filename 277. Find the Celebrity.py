# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity1(self, n: int) -> int:
        from collections import defaultdict
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        for i in range(n):
            for j in range(n):
                if j == i: continue
                if knows(i, j):
                    indegree[j] += 1
                    outdegree[i] += 1
        x, y = max(indegree.items(), key=lambda x: x[1], default=(0, 0))
        return x if y == n - 1 and outdegree[x] == 0 else -1

    def findCelebrity(self, n: int) -> int:

        res = 0
        for i in range(n):
            if knows(res, i): res = i

        for i in range(res):
            if knows(res, i) or not knows(i, res): return -1
        for i in range(res + 1, n):
            if not knows(i, res): return -1
        return res
