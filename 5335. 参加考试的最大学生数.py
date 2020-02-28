class Solution:
    def maxStudents1(self, seats) -> int:
        row = len(seats)
        col = len(seats[0])
        self.res = 0

        def helper(i, j, tmp, visited):
            # print(i, j, tmp, visited)
            if i == row:
                # print(i, tmp, visited)
                self.res = max(self.res, tmp)
                return
            # print("1", i, j, col)
            if j == col:
                helper(i + 1, 0, tmp, visited)
                return

            # print("2", i, j)
            if seats[i][j] == "." and \
                    (j - 1 < 0 or (seats[i][j - 1] == "#" or (i, j - 1) not in visited)) and \
                    (j + 1 >= col or (seats[i][j + 1] == "#" or (i, j + 1) not in visited)) and \
                    ((i - 1 < 0 or j - 1 < 0) or (
                            seats[i - 1][j - 1] == "#" or (i - 1, j - 1) not in visited)) and \
                    ((i - 1 < 0 or j + 1 >= col) or (seats[i - 1][j + 1] == "#" or (i - 1, j + 1) not in visited)):
                # helper(i , j + 1, tmp, visited)
                helper(i, j + 1, tmp + 1, visited | {(i, j)})

            helper(i, j + 1, tmp, visited)

        helper(0, 0, 0, set())
        return self.res

    def maxStudents(self, seats) -> int:
        from functools import lru_cache
        s = "".join("".join(tmp) for tmp in seats)
        row = len(seats)
        col = len(seats[0])
        @lru_cache(None)
        def helper(s):
            res = 0
            s = list(s)
            for i in range(row):
                for j in range(col):

                    if s[i * col + j] == ".":
                        s[i * col + j] = "X"
                        res = max(res, helper("".join(s)))
                        if j - 1 >= 0:
                            if (i + 1) < row and s[(i + 1) * col + j - 1] == ".":
                                s[(i + 1) * col + j - 1] = "X"
                            if s[i * col + j - 1] == ".":
                                s[i * col + j - 1] = "X"
                        if j + 1 < col:
                            if s[i * col + j + 1] == ".":
                                s[i * col + j + 1] = "X"
                            if i + 1 < row and s[(i + 1) * col + j + 1] == ".":
                                s[(i + 1) * col + j + 1] = "X"

                        res = max(res, 1 + helper("".join(s)))
            return res

        return helper(s)


a = Solution()
print(a.maxStudents(seats=[["#", ".", "#", "#", ".", "#"],
                           [".", "#", "#", "#", "#", "."],
                           ["#", ".", "#", "#", ".", "#"]]))
print(a.maxStudents([[".", ".", ".", ".", "#", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "#", "."],
                     [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", "#", ".", ".", ".", ".", "."],
                     [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "#", ".", ".", "#", "."]]))
print(a.maxStudents([[".","#","#","."],[".",".",".","#"],[".",".",".","."],["#",".","#","#"]]))