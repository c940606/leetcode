from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        prefix = [[0] * (col + 1) for _ in range(row + 1)]
        res = [[0] * col for _ in range(row)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]

        # print(prefix)
        for i in range(row):
            for j in range(col):
                up_i = i - K
                down_i = i + K
                left_j = j - K
                right_j = j + K
                if up_i < 0: up_i = 0
                if down_i >= row: down_i = row - 1
                if left_j < 0: left_j = 0
                if right_j >= col: right_j = col - 1
                # print(down_i,  right_j , up_i, left_j)
                # res[i][j] = prefix[down_i + 1][right_j + 1] - prefix[down_i + 1][left_j + 1] - prefix[up_i][
                #     right_j + 1] + prefix[up_i][left_j + 1]
                # print(prefix[down_i + 1][right_j + 1])
                # print(prefix[down_i+1][left_j])
                # print(prefix[up_i][right_j + 1])
                # print(prefix[up_i][left_j])
                res[i][j] = prefix[down_i + 1][right_j + 1] - prefix[down_i+1][left_j] - prefix[up_i][right_j + 1] + prefix[up_i][left_j]
        return res


a = Solution()
print(a.matrixBlockSum(mat=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], K=1))
print(a.matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2))
