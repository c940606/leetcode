from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        if len(coordinates) == 2: return True
        x1 = coordinates[0][0]
        y1 = coordinates[0][1]
        x2 = coordinates[1][0]
        y2 = coordinates[1][1]
        for i in range(2, len(coordinates)):
            if (coordinates[i][1] - y1) * (x2 - x1) - (y2 - y1) * (coordinates[i][0] - x1) != 0:
                return False
        return True
a = Solution()
print(a.checkStraightLine([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(a.checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))