from typing import List


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        row_A = len(A)
        col_A = len(A[0])
        row_B = len(B)
        col_B = len(B[0])
        res = [[0] * col_B for _ in range(row_A)]

        for idx, x in enumerate(A):
            for idy, y in enumerate(zip(*B)):
                res[idx][idy] = sum(i * j for i, j in zip(x, y))
        return res


a = Solution()
print(a.multiply(A=[
    [1, 0, 0],
    [-1, 0, 3]
],

    B=[
        [7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
))
