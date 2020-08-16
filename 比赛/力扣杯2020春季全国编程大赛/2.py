import collections
from typing import List


class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:

        graph = collections.defaultdict(list)
        for x, y in relation:
            graph[x].append(y)

        res = 0

        def dfs(i, k):
            nonlocal res
            if i == n - 1 and k == 0:
                res += 1
                return
            if k < 0:
                return
            for nxt in graph[i]:
                dfs(nxt, k - 1)

        dfs(0, k)
        return res


a = Solution()
print(a.numWays(n=5, relation=[[0, 2], [2, 1], [3, 4], [2, 3], [1, 4], [2, 0], [0, 4]], k=3))
print(a.numWays(n=3, relation=[[0, 2], [2, 1]], k=2))
