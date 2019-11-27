from typing import List
class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        n = len(x)
        if len(x) < 4: return False
        def check(i):
            pre = x[i]
            for j in range(i + 2, n, 2):
                if pre >= x[j]:
                    return False
                pre = x[j]
            return True
        if check(0) and check(1) :
            return False
        return True

a = Solution()
print(a.isSelfCrossing([2,1,1,2]))
print(a.isSelfCrossing([1,2,3,4]))
print(a.isSelfCrossing([1,1,1,1]))
print(a.isSelfCrossing([1,1,2,1,1]))
