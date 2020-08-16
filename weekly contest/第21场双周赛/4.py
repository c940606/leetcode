from typing import List


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:

        def dfs(target):
            # print(target)
            if target < 0:
                return float("-inf")
            if target == 0:
                return 0
            res = 0
            cur = 0
            for idx, val in enumerate(cost, 1):
                cur = cur * 10 + idx
                res = max(res, cur + dfs(target - val))
                cur = cur // 10
            return res

        return dfs(target)


a = Solution()
print(a.largestNumber(cost=[4, 3, 2, 5, 6, 7, 2, 5, 5], target=9))
