class Solution:
    def assignBikes1(self, workers, bikes) -> int:
        from itertools import permutations
        n = len(workers)
        res = float("inf")
        print(workers, bikes)

        def cal(work, bike):
            print(work, bike)
            return abs(work[0] - bike[0]) + abs(work[1] - bike[1])

        for tmp in permutations(range(n), n):
            print(tmp)
            tmp_res = 0
            for i in range(n):
                tmp_res += cal(workers[tmp[i]], bikes[i])
            res = min(res, tmp_res)
        return res

    def assignBikes(self, workers, bikes) -> int:
        from functools import lru_cache
        n = len(workers)
        def cal(work, bike):
            # print(work, bike)
            return abs(work[0] - bike[0]) + abs(work[1] - bike[1])

        @lru_cache(None)
        def helper(p, visited):
            # print(p,visited)
            if p == n:
                return 0
            tmp = float("inf")
            for j in range(n):
                if visited[j] == 0:
                    tmp = min(tmp, cal(bikes[j], workers[p]) + helper(p + 1, visited[:j] + (1,) + visited[j + 1:]))
            return tmp

        return helper(0, (0,) * n)


a = Solution()
print(a.assignBikes([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]],
                    [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999], [5, 999], [6, 999], [8, 999], [9, 999]]))
print(a.assignBikes(workers=[[0, 0], [2, 1]], bikes=[[1, 2], [3, 3]]))
# print(a.assignBikes(workers=[[0, 0], [1, 1], [2, 0]], bikes=[[1, 0], [2, 2], [2, 1]]))
# print(a.assignBikes([[239, 904], [191, 103], [260, 117], [86, 78], [747, 62]],
#                     [[660, 8], [431, 772], [78, 576], [894, 481], [451, 730], [155, 28]]))
# print(a.assignBikes([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]],
#                     [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999], [5, 999], [6, 999], [7, 999], [8, 999]]))
# print(a.assignBikes([[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]],
#                     [[0, 999], [1, 999], [2, 999], [3, 999], [4, 999], [5, 999], [6, 999], [7, 999], [8, 999],
#                      [9, 999]]))
