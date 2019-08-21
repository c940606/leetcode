class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        lookup = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                lookup[board[i][j]] = (i, j)

        def helper(begin, end):

            res = ""
            if begin == end:
                res += "!"
                return res
            row_c = begin[0] - end[0]

            if row_c > 0:
                res += "U" * row_c
            else:

                res += ("D" * (-row_c))

            col_c = begin[1] - end[1]
            if col_c > 0:
                res += "L" * col_c
            else:
                res += "R" * int(-col_c)
            res += "!"
            return res

        res = ""
        begin = (0, 0)
        for t in target:
            loc = lookup[t]
            if begin == loc:
                res += "!"
            elif t == "z":
                res += helper(begin, (4, 0))
                res = res[:-1]
                res += "D"
                res += "!"
            else:

                res += helper(begin, loc)

            begin = loc

        return res


a = Solution()
# print(a.alphabetBoardPath("leet"))
# print(a.alphabetBoardPath("code"))
print(a.alphabetBoardPath("zdz"))
print(a.alphabetBoardPath("zz"))
