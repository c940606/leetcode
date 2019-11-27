from collections import deque

target_x, target_y, n = map(int, input().split())
obstacles = set()
for _ in range(n):
    obstacles.add(tuple(map(int, input().split())))
# target_x, target_y = 2, 0
# obstacles = {(1, 0), (1, 1), (1, -1)}
# print(target_x, target_y, obstacles)


def bfs(i, j):
    queue = deque()
    visited = set()
    queue.appendleft((i, j))
    visited.add((i, j))
    step = 0
    while queue:
        n = len(queue)
        for _ in range(n):
            i, j = queue.pop()
            if (i, j) == (target_x, target_y):
                return step
            for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if -500 <= tmp_i <= 500 and -500 <= tmp_j <= 500 and \
                        (tmp_i, tmp_j) not in visited and (tmp_i, tmp_j) not in obstacles:
                    visited.add((tmp_i, tmp_j))
                    queue.appendleft([tmp_i, tmp_j])
        step += 1


print(bfs(0, 0))
