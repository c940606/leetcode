import collections
from typing import List

class Solution:
    def processQueries1(self, queries: List[int], m: int) -> List[int]:
        dp = list(range(1, m + 1))
        # print(dp)
        res = []
        for q in queries:
            loc = dp.index(q)
            res.append(loc)
            dp.insert(0, dp.pop(loc))
            # print(dp)
        return res

    def processQueries(self, queries: List[int], m: int) -> List[int]:
        from 数据结构.树状数组 import  BinaryIndexedTree
        BIT = BinaryIndexedTree([0] * (2 * m))
        lookup = {}
        for i in range(1, m + 1):
            BIT.updata(i + m, 1)
            lookup[i] = i + m
        res = []
        for q in queries:
            res.append(BIT.prefix(lookup[q] - 1))
            BIT.updata(lookup[q], -1)
            BIT.updata(m, 1)
            lookup[q] = m
            m -= 1
        return res
a = Solution()
print(a.processQueries(queries = [3,1,2,1], m = 5))
print(a.processQueries(queries=range(1, 10**3), m = 10**3))
print(a.processQueries(queries = [4,1,2,2], m = 4))
print(a.processQueries(queries = [7,5,5,8,3], m = 8))