from typing import List
import collections


class Solution:
    def numSub(self, s: str) -> int:
        from itertools import groupby

        lookup = collections.defaultdict(int)

        for k, v in groupby(s):
            if k == "1":
                lookup[len(list(v))] += 1

        def cal(n):
            return (1 + n) * n // 2


        res = 0
        for k, v in lookup.items():
            res += v * cal(k)
        return res