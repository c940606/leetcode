class Solution:
    def minimalsteps(self, maze) -> int:
        from collections import  deque
        start_i, start_j = -1, -1
        end_i, end_j = -1, -1
        machine_operated = []
        stones = []
        row, col = len(maze), len(maze[0])

        for i in range(row):
            for j in range(col):
                if maze[i][j] == "S":
                    start_i = i
                    start_j = j
                if maze[i][j] == "T":
                    end_i, end_j = i, j
                if maze[i][j] == "M":
                    machine_operated.append([i, j])
                if maze[i][j] == "O":
                    stones.append([i, j])

        def bfs(x, y):
            res = [[-1] * col for _ in range(row)]

            queue = deque([[x, y]])
            res[x][y] = 0
            while queue:
                curx, cury = queue.pop()
                for i, j in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    nxtx, nxty = curx + i, cury + j
                    if 0 <= nxtx < row and 0 <= nxty < col and maze[nxtx][nxty] != "#" and res[nxtx][nxty] == -1:
                        res[nxtx][nxty] = res[curx][cury] + 1
                        queue.appendleft([nxtx, nxty])

            return res

        nb = len(machine_operated)
        ns = len(stones)
        start_dist = bfs(start_i, start_j)
        print(start_dist)
        if nb == 0:
            return start_dist[end_i][end_j]
        dist = [[-1] * (nb + 2) for _ in range(nb)]
        intermediate_results = {}
        for i in range(nb):
            d = bfs(machine_operated[i][0], machine_operated[i][1])
            intermediate_results[i] = d
            dist[i][nb + 1] = d[end_i][end_j]

        print(intermediate_results)
        for i in range(nb):
            tmp = -1
            for k in range(ns):
                mid_x, mid_y = stones[k][0], stones[k][1]
                if intermediate_results[i][mid_x][mid_y] != -1 and start_dist[mid_x][mid_y] != -1:
                    if tmp == -1 or tmp > intermediate_results[i][mid_x][mid_y] + start_dist[mid_x][mid_y]:
                        tmp = intermediate_results[i][mid_x][mid_y] + start_dist[mid_x][mid_y]
            dist[i][nb] = tmp
            for j in range(i + 1, nb):
                mn = -1
                for k in range(ns):
                    mid_x, mid_y = stones[k][0], stones[k][1]
                    if intermediate_results[i][mid_x][mid_y] != -1 and intermediate_results[j][mid_x][mid_y] != -1:
                        if mn == -1 or mn > intermediate_results[i][mid_x][mid_y] + intermediate_results[j][mid_x][mid_y]:
                            mn = intermediate_results[i][mid_x][mid_y] + intermediate_results[j][mid_x][mid_y]
                dist[i][j] = mn
                dist[j][i] = mn

        for i in range(nb):
            if dist[i][nb] == -1 or dist[i][nb + 1] == -1:
                return -1
        dp = [[-1] * nb for _ in range(1 << nb)]
        for i in range(nb):
            dp[1 << i][i] = dist[i][nb]

        for mask in range(1, 1 << nb):
            for i in range(nb):
                if mask & (1 << i) != 0:
                    for j in range(nb):
                        if mask & (1 << j) == 0:
                            nxt = mask | (1 << j)
                            if dp[nxt][j] == -1 or dp[nxt][j] > dp[mask][i] + dist[i][j]:
                                dp[nxt][j] = dp[mask][i] + dist[i][j]

        res = -1
        endmask = (1 << nb) - 1
        for i in range(nb):
            if res == -1 or res > dp[endmask][i] + dist[i][nb + 1]:
                res = dp[endmask][i] + dist[i][nb + 1]
        return res

a = Solution()
print(a.minimalsteps(["S#O", "M..", "M.T"]))
print(a.minimalsteps(["S#O", "M.T", "M.."]))
print(a.minimalsteps(["S#O", "M.#", "M.T"]))
print(a.minimalsteps(["...O.",".S#M.","..#T.","....."]))