from typing import List
import collections

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        import functools
        row, col = len(grid), len(grid[0])
        @functools.lru_cache(None)
        def dfs(r1, c1, r2, c2):
            if r1 == row or r2 == row or c1 < 0 or c1 == col or c2 <0 or c2 == col:
                return 0
            if r1 == r2 and c1 == c2:
                return grid[r1][c1] + max(dfs(r1 + 1, c1 - 1, r2 + 1, c2), dfs(r1 + 1,c1, r2 + 1, c2 + 1))
            return grid[r1][c1] + grid[r2][c2] + max(
                dfs(r1 + 1, c1 - 1, r2 + 1, c2 - 1),
                dfs(r1 + 1, c1 - 1, r2 + 1, c2),
                dfs(r1 + 1, c1 - 1, r2 + 1, c2 + 1),
                dfs(r1 + 1, c1, r2 + 1, c2 - 1),
                dfs(r1 + 1, c1, r2 + 1, c2),
                dfs(r1 + 1, c1, r2 + 1, c2 + 1),
                dfs(r1 + 1, c1 + 1, r2 + 1, c2 - 1),
                dfs(r1 + 1, c1 + 1, r2 + 1, c2),
                dfs(r1 + 1, c1 + 1, r2 + 1, c2 + 1)
            )
        return dfs(0, 0, 0, col - 1)
        
a = Solution()
print(a.cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
print(a.cherryPickup(grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))
print(a.cherryPickup([[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]))
print(a.cherryPickup(grid = [[1,1],[1,1]]))
