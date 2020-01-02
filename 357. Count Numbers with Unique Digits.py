import functools
import operator
from itertools import accumulate


class Solution:
    def countNumbersWithUniqueDigits1(self, n: int) -> int:
        return sum(accumulate([81] + list(range(8, 10 - n, -1)), func=operator.mul)) + 10 if n > 1 else [1, 10][n]

    def countNumbersWithUniqueDigits(self, n: int) -> int:

        visited = set()

        @functools.lru_cache(None)
        def helper(d):
            if d == n: return 1
            res = 1
            for i in range(1 if d == 0 else 0, 10):
                if i not in visited:
                    visited.add(i)
                    res += helper(d + 1)
                    visited.remove(i)

            return res

        return helper(0)


a = Solution()
# print(a.countNumbersWithUniqueDigits(2))
print(a.countNumbersWithUniqueDigits(10))
