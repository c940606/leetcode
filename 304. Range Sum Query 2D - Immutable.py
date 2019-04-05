class NumMatrix:

    def __init__(self, matrix):
        row = len(matrix)
        col = len(matrix[0]) if row >  0 else 0
        self.ij_sum = [[0] * (col + 1) for _ in range(row + 1)]
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                self.ij_sum[i][j] = self.ij_sum[i - 1][j] + self.ij_sum[i][j - 1] - self.ij_sum[i - 1][j - 1] + \
                                    matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.ij_sum[row2+1][col2+1] - self.ij_sum[row2+1][col1] - self.ij_sum[row1][col2+1] + self.ij_sum[row1][col1]


a = NumMatrix([
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
])
print(a.sumRegion(1,1,2,2))