from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []
        n = len(colsum)
        res = [[0] * n for _ in range(2)]
        t = []
        for i, c in enumerate(colsum):
            if c == 1:
                t.append(i)
            if c == 2:
                res[0][i] = 1
                res[1][i] = 1

        tmp1 = sum(res[0])
        tmp2 = sum(res[1])
        # print(tmp1, tmp2, t)
        if tmp1 > upper or tmp2 > lower:
            return []
        for _ in range(upper - tmp1):
            res[0][t.pop()] = 1
        for _ in range(lower - tmp2):
            res[1][t.pop()] = 1
        return res


a = Solution()
# print(a.reconstructMatrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]))
# print(a.reconstructMatrix(upper = 2, lower = 1, colsum = [1,1,1]))
print(a.reconstructMatrix(9, 2, [0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2]))
