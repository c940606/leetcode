from typing import List
import collections

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]

        max_h = 0
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i - 1])
        max_w = 0
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i - 1])

        return max_h * max_w