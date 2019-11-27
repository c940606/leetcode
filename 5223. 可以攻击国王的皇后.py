class Solution:
    def queensAttacktheKing(self, queens, king):
        queens = {tuple(queen) for queen in queens}
        # 上 [3, 3]
        row = king[0]
        res = []
        while row >= 0:
            if (row, king[1]) in queens:
                res.append([row, king[1]])
                break
            else:
                row -= 1
        # 下
        row = king[0]
        while row < 8:
            if (row, king[1]) in queens:
                res.append([row, king[1]])
                break
            else:
                row += 1
        # 左
        col = king[1]
        while col >= 0:
            if (king[0], col) in queens:
                res.append([king[0], col])
                break
            else:
                col -= 1
        # 右
        col = king[1]
        while col < 8:
            if (king[0], col) in queens:
                res.append([king[0], col])
                break
            else:
                col += 1

        # 左上
        row = king[0]
        col = king[1]
        while row >= 0 and col >= 0:
            if (row, col) in queens:
                res.append([row, col])
                break
            else:
                row -= 1
                col -= 1
        # 右下
        row = king[0]
        col = king[1]
        while row < 8 and col < 8 :
            if (row, col) in queens:
                res.append([row, col])
                break
            else:
                row += 1
                col += 1
        # 右上
        row = king[0]
        col = king[1]
        while row >= 0 and col < 8:
            if (row, col) in queens:
                res.append([row, col])
                break
            else:
                row -= 1
                col += 1
        # zuoxia
        row = king[0]
        col = king[1]
        while row < 8 and col >= 0:
            if (row, col) in queens:
                res.append([row, col])
                break
            else:
                row += 1
                col -= 1
        return res

a = Solution()
print(a.queensAttacktheKing([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]],  [0,0]))
print(a.queensAttacktheKing(queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]))
print(a.queensAttacktheKing(queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]))
