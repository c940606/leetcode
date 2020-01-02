# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        pass


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:

        def helper(bootomLeft, topRight):

            if not sea.hasShips(topRight, bootomLeft): return 0
            if topRight.x == bootomLeft.x and topRight.y == bootomLeft.y: return 1

            mid_x = (topRight.x + bootomLeft.x) // 2
            mid_y = (topRight.y + bootomLeft.y) // 2
            if mid_x == topRight.x:
                sub = [[bootomLeft, Point(mid_x, mid_y)], [Point(mid_x, mid_y + 1), topRight]]
            elif mid_y == topRight.y:
                sub = [[bootomLeft, Point(mid_x, mid_y)], [Point(mid_x + 1, mid_y), topRight]]
            else:
                sub = [
                    [bootomLeft, Point(mid_x, mid_y)],
                    [Point(mid_x + 1, mid_y + 1), topRight],
                    [Point(bootomLeft.x, mid_y + 1), Point(mid_x, topRight.y)],
                    [Point(mid_x + 1, bootomLeft.y), Point(topRight.x, mid_y)],

                ]

            return sum(helper(x[0], x[1]) for x in sub)

        return helper(bottomLeft, topRight)
