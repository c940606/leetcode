class Solution:
    def numEnclaves(self, A):
        row = len(A)
        col = len(A[0])
        visited = set()
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            visited.add((i, j))
            A[i][j] = 2
            for x, y in dirs:
                tmp_i = x + i
                tmp_j = y + j
                if 0<=tmp_i < row and 0<=tmp_j<col and A[tmp_i][tmp_j] ==1 and (tmp_i,tmp_j) not in visited:
                    dfs(tmp_i,tmp_j)

        for i in range(row):
            for j in range(col):
                if (i == 0 or j == 0 or i == row - 1 or j == col - 1) and (i,j) not in visited and A[i][j] == 1:
                    #print(i, j)
                    dfs(i, j)
        res = 0
        #print(A)
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1:
                    res += 1
        return res
a = Solution()
print(a.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
print(a.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))

