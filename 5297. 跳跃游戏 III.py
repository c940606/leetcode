from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        def dfs(i):
            if i < 0 or i >= len(arr) or i in visited: return False
            if arr[i] == 0:
                return True
            visited.add(i)
            if dfs(i + arr[i]) or dfs(i - arr[i]): return True
            return False

        return dfs(start)


a = Solution()
print(a.canReach(arr=[3, 0, 2, 1, 2], start=2))
print(a.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))
print(a.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0))
