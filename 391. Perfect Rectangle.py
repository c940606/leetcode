from typing import List


class Solution:
    def isRectangleCover1(self, rectangles: List[List[int]]) -> bool:
        flag = set()

        left = sorted(rectangles, key=lambda x: x[0])[0][0]
        bottom = sorted(rectangles, key=lambda x: x[1])[0][1]
        right = sorted(rectangles, key=lambda x: x[2], reverse=True)[0][2]
        top = sorted(rectangles, key=lambda x: x[3], reverse=True)[0][3]
        # print(left, bottom, right, top)

        for rectangle in rectangles:
            for i in range(rectangle[0], rectangle[2]):
                for j in range(rectangle[1], rectangle[3]):
                    if (i, j) in flag: return False
                    flag.add((i, j))
        # print(flag)
        for i in range(left, right):
            for j in range(bottom, top):
                if (i, j) not in flag: return False
        return True

    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        lookup = set()
        left = float("inf")
        bottom = float("inf")
        right = float("-inf")
        top = float("-inf")
        area = 0
        for x, y, s, t in rectangles:

            left = min(left, x)
            bottom = min(bottom, y)
            right = max(right, s)
            top = max(top, t)

            area += (t - y) * (s - x)
            if (x, y) not in lookup:
                lookup.add((x, y))
            else:
                lookup.remove((x, y))
            if (x, t) not in lookup:
                lookup.add((x, t))
            else:
                lookup.remove((x, t))

            if (s, y) not in lookup:
                lookup.add((s, y))
            else:
                lookup.remove((s, y))
            if (s, t) not in lookup:
                lookup.add((s, t))
            else:
                lookup.remove((s, t))
            # print(lookup, x, y, s, t)
        # print(lookup, area, left, bottom, right, top)
        if len(lookup) != 4 or (left, bottom) not in lookup or (left, top) not in lookup or (
                right, bottom) not in lookup or (right, top) not in lookup:
            return False

        return (right - left) * (top - bottom) == area


a = Solution()
print(a.isRectangleCover(rectangles=[
    [1, 1, 3, 3],
    [3, 1, 4, 2],
    [3, 2, 4, 4],
    [1, 3, 2, 4],
    [2, 3, 3, 4]
]))
# print(a.isRectangleCover(rectangles = [
#   [1,1,2,3],
#   [1,3,2,4],
#   [3,1,4,2],
#   [3,2,4,4]
# ]))
# print(a.isRectangleCover(rectangles = [
#   [1,1,3,3],
#   [3,1,4,2],
#   [1,3,2,4],
#   [3,2,4,4]
# ]))
print(a.isRectangleCover(rectangles=[
    [1, 1, 3, 3],
    [3, 1, 4, 2],
    [1, 3, 2, 4],
    [2, 2, 4, 4]
]))
print(a.isRectangleCover([[0,0,4,1],[7,0,8,2],[6,2,8,3],[5,1,6,3],[4,0,5,1],[6,0,7,2],[4,2,5,3],[2,1,4,3],[0,1,2,2],[0,2,2,3],[4,1,5,2],[5,0,6,1]]))
