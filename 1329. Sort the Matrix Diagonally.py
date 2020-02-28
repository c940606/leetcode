from typing import List
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]: return []
        row = len(mat)
        col = len(mat[0])
        i = 0
        j = col - 1
        res = [[0] * col for _ in range(row)]
        while j >= 0 and i < row:
            tmp = []
            tmp_i = i
            tmp_j = j
            while tmp_i < row and tmp_j < col:
                tmp.append(mat[tmp_i][tmp_j])
                tmp_i += 1
                tmp_j += 1
            tmp.sort()
            tmp_i = i
            tmp_j = j
            while tmp_i < row and tmp_j < col:
                res[tmp_i][tmp_j] = tmp.pop(0)
                tmp_i += 1
                tmp_j += 1
            j -= 1
            if j == -1:
                j = 0
                i += 1
        return res

a = Solution()
print(a.diagonalSort(mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]))