# -*- coding:utf-8 -*-

class Flip:
    def flipChess(self, A, f):
        # write code here
        row = len(A)
        col = len(A[0])
        for i, j in f:
            for x, y in [[-1,0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = i + x - 1
                tmp_j = j + y - 1
                if 0<=tmp_i < row and 0 <= tmp_j < col:
                    A[tmp_i][tmp_j] = 1 - A[tmp_i][tmp_j]
        return A

a = Flip()
print(a.flipChess([[0,0,1,1],[1,0,1,0],[0,1,1,0],[0,0,1,0]],[[2,2],[3,3],[4,4]]))