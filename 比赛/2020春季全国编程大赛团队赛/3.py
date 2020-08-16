from typing import List
class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        m, n = len(maze), len(maze[0])
        taro = collections.defaultdict(list)

        po = []
        for x in range(m):
            for y in range(n):
                if maze[x][y] == 'O':
                    po.append((x, y))

        nex = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def BFS(fx, fy):
            vis = [[0] * n for _ in range(m)]
            q = [(fx, fy, 0)]
            vis[fx][fy] = 1

            for x, y, d in q:
                if maze[x][y] == "O":
                    taro[(x, y, fx, fy)] = d
                for nx, ny in nex:
                    xx, yy = nx + x, ny + y
                    if -1 < xx < m and -1 < yy < n and vis[xx][yy] == 0 and maze[xx][yy] != '#':
                        q.append((xx, yy, d + 1))
                        vis[xx][yy] = 1

        fro = []

        for i in range(m):
            for j in range(n):
                if maze[i][j] == 'S' or maze[i][j] == 'M':
                    fro.append((i, j))
                    BFS(i, j)
        le = len(taro)
        print(le)

        dp = [[[float('inf')] * le for _ in range(le)] for _ in range(le)]

        for i in range(2, le):
            for j in range(le):
                for k in range(len(po)):
                    stx, sty = po[k]
                    for f in range(le):
                        if f == j: continue
                        if i == 2:
                            dp[i][j][k] = taro[(stx, sty, fro[i][0], fro[i][1])] + taro[
                                (stx, sty, fro[k][0], fro[k][1])]
                        else:
                            dp[i][j][k] = min(dp[i][j][k],
                                              dp[i - 1][f][k] + taro[(stx, sty, fro[i][0], fro[i][1])] + taro[
                                                  (stx, sty, fro[f][0], fro[f][1])])

        # for i in range(2, le):
        #     for j in range(len(fro)):
        #         for l in range(len(fro)):
        #             if i==l: continue
        #             x, y = fro[j]
        #             x1, y1 = fro[l]
        #             if i==2:
        #                 for k in range(len(po)):
        #                     stx, sty = po[k]
        #                     if i==2:
        #                         dp[i][j][l][k] = taro[(stx, sty, x, y)]+taro[(stx, sty, x1, y1)]
        #             else:
        #                 for m in range(len(fro)):
        #                     if m==j or m==l: continue
        #                     dp[i][j][l] = min(dp[i][j][l], dp[i-1][m][l]+taro[()])

        for i in dp[2]: print(i)


a = Solution()
print(a.)
a = Solution()
print(a.)
