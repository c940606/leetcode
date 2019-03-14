class Solution(object):
    def maximalSquare(self, matrix):
        """
        在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
        ---
        输入:
        1 0 1 0 0
        1 0 1 1 1
        1 1 1 1 1
        1 0 0 1 0
        输出: 4
        ---
        思路:
        动态规划
        以右下顶点为正方形的
        然后遍历整个矩阵
        遇到0直接退出
        遇到1 首先找到最长变成 里面有0 边长减1
        :type matrix: List[List[str]]
        :rtype: int
        """
        row = len(matrix)
        col = len(matrix[0])
        res = [[0] * col for _ in range(row)]
        print(res)
        max_len = 0
        for i in range(row):
            for j in range(col):
                if i == 0:
                    res[0][j] = int(matrix[0][j])
                elif j == 0:
                    res[i][0] = int(matrix[i][0])
                elif matrix[i][j] == "1":
                    res[i][j] = min(res[i - 1][j], res[i][j - 1], res[i - 1][j - 1]) + 1
                max_len = max(max_len, res[i][j])
        return max_len * max_len


a = Solution()
print(a.maximalSquare(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))
print(a.maximalSquare([["1"]]))
