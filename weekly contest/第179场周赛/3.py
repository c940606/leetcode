from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        from collections import defaultdict
        graph = defaultdict(dict)
        for idx, val in enumerate(manager):
            graph[val][idx] = informTime[val]

        def dfs(root):
            res = 0
            for node in graph[root]:
                res = max(res, graph[root][node] + dfs(node))
            return res

        return dfs(headID)


a = Solution()
print(a.numOfMinutes(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]))
print(a.numOfMinutes(n=7, headID=6, manager=[1, 2, 3, 4, 5, 6, -1], informTime=[0, 6, 5, 4, 3, 2, 1]))
print(a.numOfMinutes(n=4, headID=2, manager=[3, 3, -1, 2], informTime=[0, 0, 162, 914]))
