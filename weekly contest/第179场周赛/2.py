from typing import List

class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        import bisect
        cur_max = 0
        cur = 0
        res = 0
        for idx, val in enumerate(light):
            cur += 1
            cur_max = max(cur_max, val)
            if cur == cur_max:
                res += 1

        return res

a = Solution()
print(a.numTimesAllBlue([2,1,3,5,4]))
print(a.numTimesAllBlue([3,2,4,1,5]))
print(a.numTimesAllBlue([4,1,2,3]))
print(a.numTimesAllBlue( [2,1,4,3,6,5]))
print(a.numTimesAllBlue([1]))