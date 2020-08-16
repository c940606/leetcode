from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        arr = []
        for idx, val in enumerate(hasApple):
            if val:
                arr.append(idx)

        if not arr: return 0
        arr.append(0)
        from collections import defaultdict
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)

        def dfs(prev, cur)

        prev = arr[0]
        res = 0
        for cur in arr[1:]:



a = Solution()
