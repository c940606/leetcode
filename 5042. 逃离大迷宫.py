class Solution:
    def isEscapePossible(self, blocked, source, target):
        from collections import deque
        blocked = set(map(tuple, blocked))

        def bfs(source, target):
            queue = deque()
            queue.appendleft((source[0], source[1], 0))
            visited = set()
            visited.add(tuple(source))
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while queue:
                x, y, step = queue.pop()
                if x == target[0] and y == target[1]:
                    return True
                for i, j in dirs:
                    tmp_x = i + x
                    tmp_y = j + y
                    if 0 <= tmp_x < 10 ** 6 and 0 <= tmp_y < 10 ** 6 and \
                            (tmp_x, tmp_y) not in visited and (tmp_x, tmp_y) not in blocked:
                        visited.add((tmp_x, tmp_y))
                        queue.appendleft((tmp_x, tmp_y, step + 1))
                if step == len(blocked): return True
            return False
        return bfs(source, target) and bfs(target, source)


a = Solution()
print(a.isEscapePossible(blocked=[[0, 1], [1, 0]], source=[0, 0], target=[0, 2]))
print(a.isEscapePossible(blocked=[], source=[0, 0], target=[999999, 999999]))
