from typing import List
import collections


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        n_b = numBottles
        k_b = 0
        res = 0
        while k_b >= numExchange or n_b:
            # print(k_b, n_b)

            while n_b:
               n_b -= 1
               res += 1
               k_b += 1

            while k_b >= numExchange:
                k_b -= numExchange
                n_b += 1
        return res

a = Solution()
print(a.numWaterBottles(9, 3))
