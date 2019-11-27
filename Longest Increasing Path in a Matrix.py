class Solution(object):
    def __init__(self):
        self.lookup = {}

    def longestIncreasingPath1(self, matrix):
        """
        给定一个整数矩阵，找出最长递增路径的长度。
        对于每个单元格，你可以往上，下，左，右四个方向移动。
        你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
        ---
        输入: nums =
        [
          [9,9,4],
          [6,6,8],
          [2,1,1]
        ]
        输出: 4
        解释: 最长递增路径为 [1, 2, 6, 9]。
        ---
        深度遍历
        要记录
        :type matrix: List[List[int]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = 1

        def dfs(matrix, i, j, row, col):
            if (i, j) in self.lookup:
                return self.lookup[(i, j)]
            ij_max_len = 1
            for dir in dirs:
                x = i + dir[0]
                y = j + dir[1]
                if x < 0 or x >= row or y < 0 or y >= col or matrix[x][y] <= matrix[i][j]:
                    continue
                temp_len = 1 + dfs(matrix, x, y, row, col)
                print(i, j)

                ij_max_len = max(ij_max_len, temp_len)
            self.lookup[(i, j)] = ij_max_len
            print(self.lookup)

            return ij_max_len

        for i in range(row):
            for j in range(col):
                temp = dfs(matrix, i, j, row, col)
                res = max(res, temp)
        # print("------")
        # print(self.lookup)
        return res

    def longestIncreasingPath(self, matrix):
        # from collections import defaultdict
        if not matrix or not matrix[0]: return 0
        # lookup = defaultdict(int)

        row = len(matrix)
        col = len(matrix[0])
        lookup = [[0] * col for _ in range(row)]

        def dfs(i, j):
            if lookup[i][j] != 0:
                return lookup[i][j]
            ## 方法一
            # res = 1
            # for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            #     tmp_i = x + i
            #     tmp_j = y + j
            #     if 0 <= tmp_i < row and 0 <= tmp_j < col and \
            #             matrix[tmp_i][tmp_j] > matrix[i][j]:
            #         res = max(res, 1 + dfs(tmp_i, tmp_j))
            # lookup[(i, j)] = max(res, lookup[(i, j)])
            # 方法二
            # lookup[(i, j)] = 1 + max(
            #     [dfs(i + x, y + j) for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]] \
            #      if 0 <= (i + x) < row and 0 <= (j + y) < col and matrix[i + x][j + y] > matrix[i][j]] or [0]
            # )
            # 方法三
            val = matrix[i][j]
            lookup[i][j] = 1 + max(
                dfs(i + 1, j) if 0 <= i + 1 < row and 0 <= j < col and matrix[i + 1][j] > val else 0,
                dfs(i - 1, j) if 0 <= i - 1 < row and 0 <= j < col and matrix[i - 1][j] > val else 0,
                dfs(i, j + 1) if 0 <= i < row and 0 <= j + 1 < col and matrix[i][j + 1] > val else 0,
                dfs(i, j - 1) if 0 <= i < row and 0 <= j - 1 < col and matrix[i][j - 1] > val else 0,
            )

            return lookup[i][j]

        return max(dfs(i, j) for i in range(row) for j in range(col))


a = Solution()
print(a.longestIncreasingPath([
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]))

print(a.longestIncreasingPath([
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]))
