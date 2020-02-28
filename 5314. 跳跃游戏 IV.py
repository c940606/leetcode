from typing import List


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        from collections import defaultdict
        from collections import  deque
        loc = defaultdict(list)
        for idx, val in enumerate(arr):
            if len(loc[val]) > 1 and loc[val][-1] + 1 == idx:
                loc[val].pop()
            loc[val].append(idx)
        print(loc)
        visited = {0}
        queue = deque([0])
        step = 0
        l = len(arr)
        while queue:
            n = len(queue)
            print(queue)
           # print(visited)
            for i in range(n):
                idx = queue.pop()
                if idx == l - 1:
                    return step

                for j in [idx - 1, idx + 1] + loc[arr[idx]]:
                    if 0 <= j < l and j not in visited:
                        visited.add(j)
                        queue.appendleft(j)
            step += 1


a = Solution()
# print(a.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
# print(a.minJumps( [11,22,7,7,7,7,7,7,7,22,13]))
# print(a.minJumps([7,6,9,6,9,6,9,7]))
# print(a.minJumps([6,1,9]))
# print(a.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
# print(a.minJumps([7,7,7,7,7,7,7,12]))
print(a.minJumps([7,6,9,6,9,6,9,7]))