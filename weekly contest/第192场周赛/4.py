from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        import functools

        t = len(houses)

        @functools.lru_cache(None)
        def dfs(i, cur, color):
            if cur > target:
                return float("inf")
            if i == m :
                if cur == target:
                    return 0
                else:
                    return float("inf")

            res = float("inf")
        
            for k in range(n):
                if houses[i] == 0:
                    houses[i] = k + 1
                    # print(i, k)
                    res = min(res, cost[i][k] + dfs(i + 1, cur + (1 if i > 0 and houses[i - 1] != houses[i] else 0), k + 1))
                    houses[i] = 0
                else:
                    res = min(res, dfs(i + 1, cur + (1 if i > 0 and houses[i - 1] != houses[i] else 0), houses[i]))
            return res
        res = float("inf")
        if houses[0] == 0:
            for k in range(n):
                res = min(res, dfs(0, 1, k + 1))
        else:
            res = min(res, dfs(0, 1, houses[0]))
        # return res
        # tmp = dfs(0, 1)
        if res == float("inf"):
            return -1
        return res

a = Solution()
print(a.minCost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))
print(a.minCost(houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3))
print(a.minCost(houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5))
print(a.minCost(houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3))
print(a.minCost([7,6,1,4,0,6,0,0,2,3,7,6,3,0,0,3,0,0,4,7],
[[20,12,13,19,9,8,19],[13,18,18,12,5,8,2],[16,11,9,4,17,14,17],[20,16,19,1,1,8,9],[20,4,15,1,15,14,13],[17,7,6,19,9,5,1],[10,10,4,2,19,12,5],[12,6,18,19,3,5,2],[3,7,17,4,15,10,16],[9,8,2,3,12,3,9],[7,9,13,17,3,8,12],[10,20,4,14,12,18,4],[10,7,14,6,6,4,8],[11,19,7,12,17,20,16],[8,9,6,15,18,13,19],[10,5,1,12,7,6,9],[1,9,7,10,7,3,11],[11,11,2,15,1,13,7],[2,5,17,19,1,2,11],[10,20,4,15,9,7,2]],
20,
7,
19))
