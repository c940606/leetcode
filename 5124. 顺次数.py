from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []

        def dfs(i, t):
            # print(i, t)
            if low <= t <= high:
                res.append(t)
            if i > 9 or t > high:
                return

            dfs(i + 1, t * 10 + i)

        for i in range(1, 10):
            dfs(i, 0)
        return sorted(res)

a  = Solution()
print(a.sequentialDigits(low = 10, high = 1000000000))
# print(a.sequentialDigits(low = 1000, high = 13000))

