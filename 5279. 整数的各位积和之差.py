from functools import reduce
import operator
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = [int(i) for i in str(n)]
        return reduce(operator.mul, n) - reduce(operator.add, n)

a = Solution()
print(a.subtractProductAndSum(10000))
