class Solution:
    def orangesRotting(self, grid: 'List[List[int]]') -> 'int':
        from collections import deque
        row = len(grid)
        col = len(grid[0])
        q = deque()
        time = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        xinxian = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.appendleft((i,j))
                if grid[i][j] == 1:
                    xinxian.append((i,j))
        if not xinxian:
            return 0
        while q:
            next_time = deque()
            while q:
                loc = q.pop()
                for x,y in directions:
                    tmp_i = x+loc[0]
                    tmp_j = y+loc[1]
                    if 0<=tmp_i< row and 0<=tmp_j < col and grid[tmp_i][tmp_j]==1:
                        grid[tmp_i][tmp_j] = 2
                        xinxian.remove((tmp_i,tmp_j))
                        next_time.appendleft((x+loc[0],y+loc[1]))
            time += 1
            if not xinxian:
                return time
            q = next_time
        return -1
        # if xinxian:
        #     return -1
        # return time
a = Solution()
print(a.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(a.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(a.orangesRotting([[0,2]]))


