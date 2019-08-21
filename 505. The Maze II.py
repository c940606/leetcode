class Solution:
    def shortestDistance(self, maze, start, destination):
        from collections import defaultdict
        row = len(maze)
        col = len(maze[0])

        lookup = defaultdict(lambda: float("inf"))
        lookup[(start[0], start[1])] = 0

        def dfs(i, j):
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                res = 0
                tmp_i = i
                tmp_j = j
                while 0 <= tmp_i + x < row and 0 <= tmp_j + y < col \
                        and maze[tmp_i + x][tmp_j + y] == 0:
                    tmp_i += x
                    tmp_j += y
                    res += 1
                # print(tmp_i,tmp_j)
                if tmp_i == i and tmp_j == j: continue
                # if (tmp_i, tmp_j) not in visited:
                if lookup[(i, j)] + res < lookup[(tmp_i, tmp_j)]:
                    lookup[(tmp_i, tmp_j)] = lookup[(i, j)] + res
                    dfs(tmp_i, tmp_j)

        dfs(start[0], start[1])
        return lookup[(destination[0], destination[1])] if lookup[(destination[0], destination[1])] != float(
            "inf") else -1


a = Solution()
print(a.shortestDistance([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4],
                         [4, 4]))
