class Solution:
    def hasPath(self, maze, start, destination) -> bool:
        import functools
        row = len(maze)
        col = len(maze[0])
        visited = set()

        # print(visited)
        @functools.lru_cache(None)
        def dfs(i, j):
            if i == destination[0] and j == destination[1]:
                return True
            visited.add((i, j))
            for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                tmp_i = i
                tmp_j = j
                while 0 <= tmp_i + x < row and 0 <= tmp_j + y < col \
                        and maze[tmp_i + x][tmp_j + y] == 0:
                    tmp_i += x
                    tmp_j += y
                #print(tmp_i,tmp_j)
                if tmp_i == i and tmp_j == j: continue
                if (tmp_i,tmp_j) not in visited:
                    if dfs(tmp_i,tmp_j):
                        return True
            return False
        return dfs(start[0], start[1])


a = Solution()
print(a.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [4, 4]))
print(a.hasPath([[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]], [0, 4], [3, 2]))
