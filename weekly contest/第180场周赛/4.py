from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        def check(i, j):
            tmp = matrix[i][j]
            # 行
            row_num = []
            for k in range(col):
                row_num.append(matrix[i][k])
            if min(row_num) != tmp:
                return False
            col_num = []
            for k in range(row):
                col_num.append(matrix[k][j])
            if max(col_num) != tmp:
                return False
            return True

        res = []
        for i in range(row):
            for j in range(col):
                if check(i, j):
                    res.append(matrix[i][j])
        return res