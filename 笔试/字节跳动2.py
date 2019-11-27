from collections import deque
import sys

bucket1, bucket2, bucket3, target = map(int, input().split())
# bucket1 = 3
# bucket2 = 5
# bucket3 = 8
# target = 4
visited = set()
queue = deque()
queue.extendleft([[bucket1, 0, 0], [0, bucket2, 0], [0, 0, bucket3]])
visited.add((bucket1, 0, 0))
visited.add((0, bucket2, 0))
visited.add((0, 0, bucket3))
step = 0
while queue:
    step += 1
    n = len(queue)
    for _ in range(n):
        x, y, z = queue.pop()
        if target in (x, y, z):
            print(step)
            sys.exit()
        # 一个桶 倒满
        if (bucket1, y, z) not in visited:
            visited.add((bucket1, y, z))
            queue.appendleft([bucket1, y, z])
        if (x, bucket2, z) not in visited:
            visited.add((x, bucket2, z))
            queue.appendleft([x, bucket2, z])
        if (x, y, bucket3) not in visited:
            visited.add((x, y, bucket3))
            queue.appendleft([x, y, bucket3])
        # 一个桶 清空
        if (0, y, z) not in visited:
            visited.add((0, y, z))
            queue.appendleft([0, y, z])
        if (x, 0, z) not in visited:
            visited.add((x, 0, z))
            queue.appendleft([0, y, z])
        if (x, y, 0) not in visited:
            visited.add((x, y, 0))
            queue.appendleft([x, y, 0])
        # 两个桶
        # x -> y
        all_sum = x + y
        # 到 x
        if all_sum >= bucket1:
            if (bucket1, all_sum - bucket1, z) not in visited:
                visited.add((bucket1, all_sum - bucket1, z))
                queue.appendleft([bucket1, all_sum - bucket1, z])
        else:
            if (all_sum, 0, z) not in visited:
                visited.add((all_sum, 0, z))
                queue.appendleft([all_sum, 0, z])
        # 到 y
        if all_sum >= bucket2:
            if (all_sum - bucket2, bucket2, z) not in visited:
                visited.add((all_sum - bucket2, bucket2, z))
                queue.appendleft([all_sum - bucket2, bucket2, z])
        else:
            if (0, all_sum, z) not in visited:
                visited.add((0, all_sum, z))
                queue.appendleft([0, all_sum, z])
        # x -> z
        all_sum = x + z
        # 到x
        if all_sum >= bucket1:
            if (bucket1, y, all_sum - bucket1) not in visited:
                visited.add((bucket1, y, all_sum - bucket1))
                queue.appendleft([bucket1, y, all_sum - bucket1])
        else:
            if (all_sum, y, 0) not in visited:
                visited.add((all_sum, y, 0))
                queue.appendleft([all_sum, y, 0])
        # 到z
        if all_sum >= bucket3:
            if (all_sum - bucket3, y, bucket3) not in visited:
                visited.add((all_sum - bucket3, y, bucket3))
                queue.appendleft([all_sum - bucket3, y, bucket3])
        else:
            if (0, y, all_sum) not in visited:
                visited.add((0, y, all_sum))
                queue.appendleft([0, y, all_sum])
        # y -> z
        all_sum = y + z
        # 到y
        if all_sum >= bucket2:
            if (x, bucket2, all_sum - bucket2) not in visited:
                visited.add((x, bucket2, all_sum - bucket2))
                queue.appendleft([x, bucket2, all_sum - bucket2])
        else:
            if (x, all_sum, 0) not in visited:
                visited.add((x, all_sum, 0))
                queue.appendleft([x, all_sum, 0])
        # 到z
        if all_sum >= bucket3:
            if (x, all_sum - bucket3, bucket3) not in visited:
                visited.add((x, all_sum - bucket3, bucket3))
                queue.appendleft([x, all_sum - bucket3, bucket3])
        else:
            if (x, 0, all_sum) not in visited:
                visited.add((x, 0, all_sum))
                queue.appendleft([x, 0, all_sum])
print(-1)
