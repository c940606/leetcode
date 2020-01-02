from typing import List


class Solution:
    def minDistance1(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        lookup = {}

        def cal(squirrel, tree, nut):

            return abs(nut[0] - squirrel[0]) + abs(nut[1] - squirrel[1]) + abs(tree[0] - nut[0]) + abs(tree[1] - nut[1])

        res = float("inf")
        for idx, nut1 in enumerate(nuts):
            tmp = cal(squirrel, tree, nut1)
            for idy, nut2 in enumerate(nuts):
                if idx == idy: continue
                if idy not in lookup:
                    lookup[idy] = cal(tree, tree, nut2)
                tmp += lookup[idy]
            res = min(res, tmp)
        return res

    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def cal1(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        def cal(squirrel, tree, nut):
            return abs(nut[0] - squirrel[0]) + abs(nut[1] - squirrel[1]) + abs(tree[0] - nut[0]) + abs(tree[1] - nut[1])

        res = 0
        cur = 0
        for idx, nut in enumerate(nuts):
            tn = cal1(tree, nut)
            sn = cal1(squirrel, nut)
            cur = min(cur, sn - tn)
            res += 2 * tn
        return res  
        # all_sum = 0
        # res = float("inf")
        # for nut in nuts:
        #     all_sum += cal(tree, tree, nut)
        # for idx, nut in enumerate(nuts):
        #     cur = cal(squirrel, tree, nut) + all_sum - cal(tree, tree, nuts[idx])
        #     res = min(res, cur)
        #
        # return res


a = Solution()
# print(a.minDistance(5, 7, [2, 2], [4, 4], [[3, 0], [2, 5]]))
print(a.minDistance(5, 5, [3, 2], [0, 1],
                    [[2, 0], [4, 1], [0, 4], [1, 3], [1, 0], [3, 4], [3, 0], [2, 3], [0, 2], [0, 0], [2, 2], [4, 2],
                     [3, 3], [4, 4], [4, 0], [4, 3], [3, 1], [2, 1], [1, 4], [2, 4]]))
