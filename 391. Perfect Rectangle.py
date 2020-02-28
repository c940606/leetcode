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
        # 最大矩形的 左下角 右上角
        x1 = float("inf")
        y1 = float("inf")
        x2 = float("-inf")
        y2 = float("-inf")
        area = 0
        for x, y, s, t in rectangles:

            x1 = min(x1, x)
            y1 = min(y1, y)
            x2 = max(x2, s)
            y2 = max(y2, t)

            area += (t - y) * (s - x)
            # 每个矩形的四个点
            for item in [(x, y), (x, t), (s, y), (s, t)]:
                if item not in lookup:
                    lookup.add(item)
                else:
                    lookup.remove(item)
        # 只剩下四个点并且是最大矩形的左下角和右上角
        if len(lookup) != 4 or \
                (x1, y1) not in lookup or (x1, y2) not in lookup or (x2, y1) not in lookup or (x2, y2) not in lookup:
            return False
        # 面积是否满足
        return (x2 - x1) * (y2 - y1) == area


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
print(a.isRectangleCover(
    [[0, 0, 4, 1], [7, 0, 8, 2], [6, 2, 8, 3], [5, 1, 6, 3], [4, 0, 5, 1], [6, 0, 7, 2], [4, 2, 5, 3], [2, 1, 4, 3],
     [0, 1, 2, 2], [0, 2, 2, 3], [4, 1, 5, 2], [5, 0, 6, 1]]))
