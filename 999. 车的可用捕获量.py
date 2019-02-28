class Solution:
    def numRookCaptures(self, board: 'List[List[str]]') -> 'int':
        row = len(board)
        col = len(board[0])
        rook_i = None
        rook_j = None
        for i in range(row):
            for j in range(col):
                if board[i][j] == "R":
                    rook_i = i
                    rook_j = j
        # 上
        res = 0
        for s in range(rook_i - 1, -1, -1):
            if board[s][rook_j] == "B":
                break
            elif board[s][rook_j] == "p":
                res += 1
                break
        for x in range(rook_i + 1, row):
            if board[x][rook_j] == "B":
                break
            elif board[x][rook_j] == "p":
                res += 1
                break
        for l in range(rook_j - 1, -1, -1):
            if board[rook_i][l] == "B":
                break
            elif board[rook_i][l] == "p":
                res += 1
                break
        for r in range(rook_j + 1, col):
            if board[rook_i][r] == "B":
                break
            elif board[rook_i][r] == "p":
                res += 1
                break
        return res


a = Solution()
print(a.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
print(a.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                         [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
                         [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
print(a.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
                         [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
print(a.numRookCaptures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", "p", "p", ".", ".", ".", "."], [".", "p", "p", "R", ".", "p", ".", "p"],
                         [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", "p", ".", "."],
                         [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))
