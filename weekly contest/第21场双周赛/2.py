from typing import List
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        import math

        res = set()
        for i in range(2, n + 1):
            for j in range(1, i):
                k = math.gcd(i, j)
                res.add(str(j//k)+"/"+str(i//k))
        return res

a = Solution()
print(a.simplifiedFractions(4))