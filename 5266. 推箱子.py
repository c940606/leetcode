class Solution:
    def minPushBox1(self, grid) -> int:
        from collections import deque
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        row = len(grid)
        col = len(grid[0])
        queue = deque()
        visited = set()

        # pprint(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "B":
                    grid[i][j] = "."
                    box = [i, j]
                elif grid[i][j] == "T":
                    grid[i][j] = "."
                    target = [i, j]
                elif grid[i][j] == "S":
                    grid[i][j] = "."
                    person = [i, j]
        # print(box, target, person)
        if box == target:
            return 0

        def check(person, target_person, box, visited):
            # print(person, target_person, box, visited)
            if grid[person[0]][person[1]] == "#" or (person[0] == box[0] and person[1] == box[1]):
                return False
            if person[0] == target_person[0] and person[1] == target_person[1]:
                return True
            visited.add(tuple(person))
            for x, y in dirs:
                tmp_p1 = person[0] + x
                tmp_p2 = person[1] + y
                if 0 <= tmp_p1 < row and 0 <= tmp_p2 < col and grid[tmp_p1][tmp_p2] == "." and \
                        (tmp_p1, tmp_p2) not in visited \
                        and check([tmp_p1, tmp_p2], target_person, box, visited):
                    return True
            return False

        def nxt_loc(box, person):
            for x, y in dirs:
                nxt_box = [box[0] + x, box[1] + y]
                target_person = [box[0] - x, box[1] - y]
                if 0 <= nxt_box[0] < row and 0 <= nxt_box[1] < col and grid[nxt_box[0]][nxt_box[1]] == "." \
                        and 0 <= target_person[0] < row and 0 <= target_person[1] < col and grid[target_person[0]][
                    target_person[1]] == "." \
                        and (nxt_box[0], nxt_box[1], box[0], box[1]) not in visited \
                        and check(person, target_person, box, {tuple(person)}):
                    queue.appendleft((nxt_box[0], nxt_box[1], box[0], box[1]))
                    visited.add((nxt_box[0], nxt_box[1], box[0], box[1]))

        nxt_loc(box, person)
        # print(queue,visited)
        step = 1
        while queue:
            # print(queue)
            n = len(queue)
            for _ in range(n):
                b1, b2, p1, p2 = queue.pop()
                if b1 == target[0] and b2 == target[1]:
                    return step
                nxt_loc([b1, b2], [p1, p2])
            step += 1
        return -1

    def minPushBox(self, grid) -> int:
        import heapq
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        row = len(grid)
        col = len(grid[0])
        person = None
        box = None
        target = None
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "S":
                    person = [i, j]
                    grid[i][j] = "."
                elif grid[i][j] == "T":
                    target = [i, j]
                    grid[i][j] = "."
                elif grid[i][j] == "B":
                    box = [i, j]
                    grid[i][j] = "."
        visited = set([(*person, *box)])
        queue = [[0, *person, *box]]
        while queue:
            step, p1, p2, b1, b2 = heapq.heappop(queue)
            for x, y in dirs:
                nxt_person = [p1 + x, p2 + y]
                if nxt_person[0] < 0 or nxt_person[0] >= row or nxt_person[1] < 0 or nxt_person[1] >= col or \
                        grid[nxt_person[0]][nxt_person[1]] == "#":
                    continue
                nxt_box = [b1, b2]
                nxt_step = step
                if nxt_box == nxt_person:
                    nxt_box[0] += x
                    nxt_box[1] += y
                    if nxt_box[0] < 0 or nxt_box[0] >= row or nxt_box[1] < 0 or nxt_box[1] >= col or grid[nxt_box[0]][
                        nxt_box[1]] == "#":
                        continue
                    nxt_step += 1
                if nxt_box == target:
                    return nxt_step
                if (*nxt_person, *nxt_box) in visited:
                    continue
                heapq.heappush(queue, (nxt_step, *nxt_person, *nxt_box))
                visited.add((*nxt_person, *nxt_box))
        return -1

a = Solution()
print(a.minPushBox(grid=[["#", "#", "#", "#", "#", "#"],
                         ["#", "T", "#", "#", "#", "#"],
                         ["#", ".", ".", "B", ".", "#"],
                         ["#", ".", "#", "#", ".", "#"],
                         ["#", ".", ".", ".", "S", "#"],
                         ["#", "#", "#", "#", "#", "#"]]))
print(a.minPushBox([["#", "#", "#", "#", "#", "#"],
                    ["#", "T", "#", "#", "#", "#"],
                    ["#", ".", ".", "B", ".", "#"],
                    ["#", "#", "#", "#", ".", "#"],
                    ["#", ".", ".", ".", "S", "#"],
                    ["#", "#", "#", "#", "#", "#"]]))
print(a.minPushBox(grid=[["#", "#", "#", "#", "#", "#"],
                         ["#", "T", ".", ".", "#", "#"],
                         ["#", ".", "#", "B", ".", "#"],
                         ["#", ".", ".", ".", ".", "#"],
                         ["#", ".", ".", ".", "S", "#"],
                         ["#", "#", "#", "#", "#", "#"]]))
print(a.minPushBox(grid=[["#", "#", "#", "#", "#", "#", "#"], ["#", "S", "#", ".", "B", "T", "#"],
                         ["#", "#", "#", "#", "#", "#", "#"]]))
print(a.minPushBox([[".", ".", "#", ".", ".", ".", ".", "#"], [".", "B", ".", ".", ".", ".", ".", "#"],
                    [".", ".", "S", ".", ".", ".", ".", "."], [".", "#", ".", ".", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "T", ".", ".", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", "#"], [".", "#", ".", ".", ".", ".", ".", "."]]))
