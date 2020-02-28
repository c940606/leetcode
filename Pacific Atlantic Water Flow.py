class Solution:
    def pacificAtlantic1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix: return []
        step = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = []
        row = len(matrix)
        col = len(matrix[0])
        q_flag = [[False] * col for _ in range(row)]
        a_flag = [[False] * col for _ in range(row)]

        def dfs(i, j, visited):
            visited[i][j] = True
            for x, y in step:
                tmp_i, tmp_j = i + x, j + y
                if tmp_i < 0 or tmp_j < 0 or tmp_i >= row or tmp_j >= col or matrix[tmp_i][tmp_j] < matrix[i][
                    j] or visited[tmp_i][tmp_j]:
                    continue
                dfs(tmp_i, tmp_j, visited)

        for m in range(row):
            dfs(m, 0, q_flag)
            dfs(m, col - 1, a_flag)
        for n in range(col):
            dfs(0, n, q_flag)
            dfs(row - 1, n, a_flag)
        for i in range(row):
            for j in range(col):
                if q_flag[i][j] and a_flag[i][j]:
                    res.append([i, j])
        return res

    def pacificAtlantic(self, matrix):
        if not matrix or not matrix[0]: return []
        res1 = set()
        res2 = set()
        row = len(matrix)
        col = len(matrix[0])

        def dfs(i, j, cur, res):
            if i < 0 or i >= row or j < 0 or j >= col or matrix[i][j] < cur or (i, j) in res:
                return
            res.add((i, j))
            tmp = matrix[i][j]
            dfs(i + 1, j, tmp, res)
            dfs(i - 1, j, tmp, res)
            dfs(i, j + 1, tmp, res)
            dfs(i, j - 1, tmp, res)

        for i in range(row):
            dfs(i, 0, 0, res1)
        for j in range(col):
            dfs(0, j, 0, res1)
        for i in range(row):
            dfs(i, col - 1, 0, res2)
        for j in range(col):
            dfs(row - 1, j, 0, res2)

        return res1 & res2


a = Solution()
# print(a.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
print(a.pacificAtlantic([[1, 1], [1, 1], [1, 1]]))
print(a.pacificAtlantic([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 12],
                         [39, 72, 73, 74, 75, 76, 77, 78, 79, 50, 13], [38, 71, 96, 97, 98, 99, 100, 101, 80, 51, 14],
                         [37, 70, 95, 112, 113, 114, 115, 102, 81, 52, 15],
                         [36, 69, 94, 111, 120, 121, 116, 103, 82, 53, 16],
                         [35, 68, 93, 110, 119, 118, 117, 104, 83, 54, 17],
                         [34, 67, 92, 109, 108, 107, 106, 105, 84, 55, 18],
                         [33, 66, 91, 90, 89, 88, 87, 86, 85, 56, 19], [32, 65, 64, 63, 62, 61, 60, 59, 58, 57, 20],
                         [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21]]))
