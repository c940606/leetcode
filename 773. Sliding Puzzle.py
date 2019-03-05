class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        row = len(board)
        col = len(board[0])
        er_one = [None] * (row * col)
        # 二维转换一维
        for i in range(row):
            for j in range(col):
                er_one[i * col + j] = board[i][j]
        # 最后跳出循环的条件
        c_loc = [0]*(row*col)
        for i in range(1,row*col):
            c_loc[i-1] = i
        # 步数
        step = 0
        # 方向
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        # 当前情况
        cur = [er_one]
        # 已访问的情况
        visited = set()
        while cur:
            next_time = []
            print(cur)
            for tmp in cur:
                # 当此时的情况和正确的情况一样是,返回步数
                if tmp == c_loc:
                    return step
                # 没有访问过的情况
                if tuple(tmp) not in visited:
                    # 添加到已访问
                    visited.add(tuple(tmp))
                    # 找到一维数组的0的位置
                    zero_loc = tmp.index(0)
                    # 找到对应二维数组的行和列
                    x, y = divmod(zero_loc, col)
                    # 进行上下左右交换
                    for p,q in dirs:
                        tmp_x = x + p
                        tmp_y = y + q
                        if  0<=tmp_x < row and 0<=tmp_y<col:
                            # 要拷贝一份
                            tmp_tmp = tmp[:]
                            tmp_tmp[tmp_x*col+tmp_y],tmp_tmp[zero_loc] = tmp_tmp[zero_loc],tmp_tmp[tmp_x*col+tmp_y]
                            next_time.append(tmp_tmp)
            step += 1
            cur = next_time
        return -1



a = Solution()
print(a.slidingPuzzle(board=[[4, 1, 2], [5, 0, 3]]))
# print(a.slidingPuzzle(board = [[1,2,3],[5,4,0]]))
# print(a.slidingPuzzle(board = [[1,2,3],[4,0,5]]))
# print(a.slidingPuzzle([[6,2,8],[4,5,7],[3,1,0]]))
