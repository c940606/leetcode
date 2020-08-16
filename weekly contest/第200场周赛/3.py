from typing import List
import collections


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:

        n = len(grid)
        lookup = set()
        cur = []
        for i in range(n):
            zero = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1: break
                if grid[i][j] == 0:
                    zero += 1
            while zero in lookup:
                zero -= 1
            if zero == -1: return -1

            lookup.add(zero)

            cur.append(n - 1 - zero)


        # print(cur)
        def check(cur):
            s_cur = sorted([n - 1 - c for c in cur])
            tmp = 0
            for t in s_cur:
                if tmp > t:
                    return False
                tmp += 1
            return True

        if not check(cur): return -1

        res = 0
        for i in range(n - 1, -1, -1):

            for j in range(i):
                if cur[j] > cur[j + 1]:
                    cur[j], cur[j + 1] = cur[j + 1], cur[j]
                    res += 1
        return res

a = Solution()
print(a.minSwaps([[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]))
# [[0,0,1],[1,1,0],[1,0,0]]
# [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
# [[1,0,0],[1,1,0],[1,1,1]]
# [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
# [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
print(a.minSwaps([[0,0,1],[1,1,0],[1,0,0]]))
print(a.minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]))
print(a.minSwaps([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]))
