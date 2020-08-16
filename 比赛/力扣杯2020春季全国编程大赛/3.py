from typing import List
import collections

class Solution:
    def getTriggerTime(self, increase: List[List[int]], requirements: List[List[int]]) -> List[int]:
        import bisect
        C = [0]
        R = [0]
        H = [0]
        n = len(increase) + 1
        for c, r, h in increase:
            C.append(C[-1] + c)
            R.append(R[-1] + r)
            H.append(H[-1] + h)
        res = []
        for c, r, h in requirements:
            loc1 = bisect.bisect_left(C, c)
            if loc1 == n:
                res.append(-1)
                continue
            loc2 = bisect.bisect_left(R, r)
            if loc2 == n:
                res.append(-1)
                continue
            loc3 = bisect.bisect_left(H, h)
            if loc3 == n:
                res.append(-1)
                continue
            res.append(max(loc1, loc2, loc3))
        return res


a = Solution()
print(a.getTriggerTime(increase = [[2,8,4],[2,5,0],[10,9,8]], requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]))
print(a.getTriggerTime(increase = [[0,4,5],[4,8,8],[8,6,1],[10,10,0]], requirements = [[12,11,16],[20,2,6],[9,2,6],[10,18,3],[8,14,9]]))
print(a.getTriggerTime(increase = [[1,1,1]], requirements = [[0,0,0]]))