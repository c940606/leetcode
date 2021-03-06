class Solution(object):
    def numIslands1(self, grid):
        """
        给定一个由 '1'（陆地）和 '0'（水）组成的的二维网格，计算岛屿的数量。
        一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
        你可以假设网格的四个边均被水包围。
        --
        输入:
        ["11110",
        "11010",
        "11000",
        "00000"]
        输出: 1
        ---
        输入:
        11000
        11000
        00100
        00011
        输出: 3
        ---
        思路:
        当遇到"1"把上下左右都变成"0"
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        r = len(grid)
        c = len(grid[0])

        def helper(i, j):
            grid[i][j] = "0"
            if j > 0 and grid[i][j - 1] == "1":
                helper(i, j - 1)
            if j < c - 1 and grid[i][j + 1] == "1":
                helper(i, j + 1)
            if i > 0 and grid[i - 1][j] == "1":
                helper(i - 1, j)
            if i < r - 1 and grid[i + 1][j] == "1":
                helper(i + 1, j)

        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    helper(i, j)
                    count += 1
        return count

    def numIslands4(self, grid):
        r = len(grid)
        c = len(grid[0])

        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for i in range(r):
            for j in range(c):
                if j > 0 and grid[i][j - 1] == "1":
                    union((i, j), (i, j - 1))
                # if j < c - 1 and grid[i][j + 1] == "1":
                # 	union((i, j), (i, j + 1))
                elif i > 0 and grid[i - 1][j] == "1":
                    union((i, j), (i - 1, j))
            # if i < r - 1 and grid[i + 1][j] == "1":
            # 	union((i, j), (i, j - 1))
        s = set()
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    if find((i, j)) not in s:
                        s.add(find((i, j)))
                        res += 1
        return res

    def numIslands2(self, grid):
        row = len(grid)
        col = len(grid[0])
        self.res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    self.res += 1
        f = {}

        def find(x):
            f.setdefault(x, x)
            while x != f[x]:
                x = f[x]
            return f[x]

        def union(i, j):
            findi = find(i)
            findj = find(j)
            if findi != findj:
                f[findi] = findj
                self.res -= 1

        for i in range(row):
            for j in range(col):
                p = i * col + j
                if grid[i][j] == "1":
                    print(i, j)
                    if i > 0 and grid[i - 1][j] == "1":
                        q = p - col
                        union(p, q)
                    if i < row - 1 and grid[i + 1][j] == "1":
                        q = p + col
                        union(p, q)
                    if j > 0 and grid[i][j - 1] == "1":
                        q = p - 1
                        union(p, q)
                    if j < col - 1 and grid[i][j + 1] == "1":
                        q = p + 1
                        union(p, q)
        return self.res

    def numIslands3(self, grid):
        if not grid: return 0
        row = len(grid)
        col = len(grid[0])
        cnt = 0

        def dfs(i, j):
            grid[i][j] = "0"
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                    dfs(tmp_i, tmp_j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i, j)
                    cnt += 1
        return cnt

    def numIslands6(self, grid):
        from collections import deque
        if not grid: return 0
        row = len(grid)
        col = len(grid[0])
        cnt = 0

        def bfs(i, j):
            queue = deque()
            queue.appendleft((i, j))
            grid[i][j] = "0"
            while queue:
                i, j = queue.pop()
                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                        grid[tmp_i][tmp_j] = "0"
                        queue.appendleft((tmp_i, tmp_j))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    bfs(i, j)
                    cnt += 1
        return cnt

    def numIslands(self, grid):
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        if not grid: return 0
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    for x, y in [[-1, 0], [0, -1]]:
                        tmp_i = i + x
                        tmp_j = j + y
                        if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == "1":
                            union(tmp_i * col + tmp_j, i * col + j)
        # print(f)
        res = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    res.add(find((i * col + j)))
        return len(res)


a = Solution()
print(a.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print(a.numIslands(
    [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
