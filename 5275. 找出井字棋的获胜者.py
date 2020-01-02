from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        from collections import defaultdict

        lookup = defaultdict(int)
        player = "A"
        player = str(player)
        for row, col in moves:
            lookup[player + "r" + str(row)] += 1
            lookup[player + "c" + str(col)] += 1
            lookup[player + "r+c" + str(row + col)] += 1
            lookup[player + "r-c" + str(row - col)] += 1
            if max(lookup[player + "r" + str(row)], lookup[player + "c" + str(col)],
                   lookup[player + "r+c" + str(row + col)],
                   lookup[player + "r-c" + str(row - col)]) == 3:
                return player
            if player == "A":
                player = "B"
            else:
                player = "A"
        if len(moves) == 9: return "Draw"
        return "Pending"
a = Solution()