import copy


class Solution:
    def setZeroes1(self, matrix):
        """
        给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        def setZer0(i, j):
            for k in range(n):
                matrix[i][k] = 0
            for k in range(m):
                matrix[k][j] = 0

        new_matrix = copy.deepcopy(matrix)
        for i in range(m):
            for j in range(n):
                if new_matrix[i][j] == 0:
                    setZer0(i, j)
        return matrix

    def setZeroes2(self, matrix):
        flag_col = False
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            if matrix[i][0] == 0: flag_col = True
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        print(matrix)
        for i in range(row - 1, -1, -1):
            for j in range(col - 1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            if flag_col == True: matrix[i][0] = 0
        print(matrix)

    def setZeroes(self, matrix):
        row = len(matrix)
        col = len(matrix[0])
        row0_flag = False
        col0_flag = False
        # 找第一行是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True
                break
        # 第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break

        # 把第一行或者第一列作为 标志位
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        print(matrix,row0_flag,col0_flag)
        # 置0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0
        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0
        print(matrix)


a = Solution()
obj = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
# print(a.setZeroes(obj))
print(a.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
print(a.setZeroes([[1, 0]]))
