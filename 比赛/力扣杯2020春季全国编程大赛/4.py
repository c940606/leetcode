import sys
from typing import List

sys.setrecursionlimit(5000000)


class Solution:
    def minJump1(self, jump: List[int]) -> int:
        import functools
        n = len(jump)
        visited = set()
        visited.add(0)

        @functools.lru_cache(None)
        def dfs(i):
            # print(i)
            if i >= n:
                return 1
            res = 1 + dfs(i + jump[i])
            for j in range(i, min(n - 1, i + jump[i])):
                if j not in visited:
                    visited.add(j)
                    res = min(res, 2 + dfs(j + jump[j]))
            return res

        return dfs(0)

    def minJump(self, jump: List[int]) -> int:
        from collections import deque

        bfs = deque([0])
        end = 0
        dp = [None] * len(jump)
        dp[0] = 0
        while bfs:
            i = bfs.pop()
            for j in range(end + 1, i):
                if dp[j] is None:
                    dp[j] = dis[i] + 1
                    dp.appendleft(j)
            end = i
            j = i + jump[i]
            if j >= n:
                return dp[i] + 1
            if dp[j] is None:
                dp[j] = dp[i] + 1
                bfs.appendleft(j)


a = Solution()
print(a.minJump([2, 5, 1, 1, 1, 1]))
print(a.minJump([1] * (10 ** 6)))
