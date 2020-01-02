from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        M = 1337

        def cal(a, b):
            return a ** b % M

        def helper(a, b):
            if not b: return 1
            tmp = b.pop(-1)
            return cal(helper(a, b), 10) * cal(a, tmp)

        return helper(a, b) % M


a = Solution()
print(a.superPow(2, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
