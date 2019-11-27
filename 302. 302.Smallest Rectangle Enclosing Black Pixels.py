from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        row = [float("inf"), float("-inf")]
        col = [float("inf"), float("-inf")]

        for i, s in enumerate(image):
            for j, a in enumerate(s):
                if a == "1":
                    row[0] = min(i, row[0])
                    row[1] = max(i, row[1])
                    col[0] = min(j, col[0])
                    col[1] = max(j, col[1])
        return (row[1] - row[0] + 1) * (col[1] - col[0] + 1)


a = Solution()
print(a.minArea([
    "0010",
    "0110",
    "0100"
], 0, 2))
