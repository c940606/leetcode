from typing import List
from collections import defaultdict, deque

class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        res = [float("-inf"), float("inf")]
        for n in range(int(num ** 0.5) + 1, 0, -1):
            div1, mod1 = divmod(num + 1, n)
            div2, mod2 = divmod(num + 2, n)
            if mod1 == 0:
                if abs(res[0] - res[1]) > abs(n - div1):
                    res[0] = n
                    res[1] = div2
            if mod2 == 0:
                if abs(res[0] - res[1]) > abs(n - div1):
                    res[0] = n
                    res[1] = div2
        return res

a = Solution()
print(a.closestDivisors(8))
print(a.closestDivisors(999))