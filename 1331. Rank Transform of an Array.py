from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        from itertools import groupby
        a = []
        n = len(arr)
        for idx, val in enumerate(arr):
            a.append([val, idx])
        a.sort()
        res = [0] * n
        for rank, item in enumerate(groupby(a, key=lambda x:x[0]),1):
            for val, idx in item[1]:
                res[idx] = rank
        return res


a = Solution()
print(a.arrayRankTransform([40, 20, 10, 30]))
print(a.arrayRankTransform([100, 100, 100, 1]))
