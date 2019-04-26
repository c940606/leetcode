class Solution:
    def validTicTacToe(self, board):
        """
        1. "O"个数大于"X" turn > 1 错
        2. X个数超过2个大于O 错
        3. turn == 0 Xwin 不可能
        4. turn == 1 Owin 不可能
        :param board:
        :return:
        """
        turn = 0

        def helper(flag):
            # 行
            for i in range(3):
                if board[i][0] == flag and board[i][1] == flag \
                        and board[i][2] == flag:
                    return True
            # 列
            for i in range(3):
                if board[0][i] == flag and board[1][i] == flag \
                        and board[2][i] == flag:
                    return True
            if board[0][0] == flag and board[1][1] == flag \
                    and board[2][2] == flag:
                return True
            if board[0][2] == flag and board[1][1] == flag \
                    and board[2][0] == flag:
                return True
            return False

        Xwin = helper("X")
        Owin = helper("O")
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    turn += 1
                elif board[i][j] == "O":
                    turn -= 1
        if turn > 1 or turn < 0 or (turn == 0 and Xwin) or (turn == 1 and Owin):
            return False
        return True
