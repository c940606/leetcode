from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:

        visited = set()
        res = 0

        def dfs(open_boxes, close_boxes, k):
            # print(open_boxes, close_boxes, k)
            nonlocal res
            if not open_boxes and not (close_boxes & k): return
            nxt_open_boxes = set()
            nxt_close_boxes = set()
            for b in open_boxes:
                res += candies[b]
                k.update(keys[b])
                for c in containedBoxes[b]:
                    if status[c] == 1:
                        nxt_open_boxes.add(c)
                    else:
                        nxt_close_boxes.add(c)
            for b in close_boxes:
                if b in k:
                    nxt_open_boxes.add(b)
                else:
                    nxt_close_boxes.add(b)
            dfs(nxt_open_boxes, nxt_close_boxes, k)

        open_boxes = set()
        close_boxes = set()
        k = set()
        for b in initialBoxes:
            if status[b] == 1:
                open_boxes.add(b)
            else:
                close_boxes.add(b)

        dfs(open_boxes, close_boxes, k)
        return res


a = Solution()
print(a.maxCandies(status=[1, 0, 1, 0], candies=[7, 5, 4, 100], keys=[[], [], [1], []],
                   containedBoxes=[[1, 2], [3], [], []], initialBoxes=[0]))
print(a.maxCandies(status=[1, 0, 0, 0, 0, 0], candies=[1, 1, 1, 1, 1, 1], keys=[[1, 2, 3, 4, 5], [], [], [], [], []],
                   containedBoxes=[[1, 2, 3, 4, 5], [], [], [], [], []], initialBoxes=[0]
                   ))
print(a.maxCandies(status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1]
))
print(a.maxCandies(status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0]

))
