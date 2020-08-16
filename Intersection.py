from typing import List


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        # 求出一般直线方程
        def equ(start, end):
            A = end[1] - start[1]
            B = start[0] - end[0]
            C = end[0] * start[1] - start[0] * end[1]
            return A, B, C

        # 检测点是否在线段上
        def check(point, start, end):
            if min(start[0], end[0]) <= point[0] <= max(start[0], end[0]) and \
                    min(start[1], end[1]) <= point[1] <= max(start[1], end[1]):
                return True
            return False

        A1, B1, C1 = equ(start1, end1)
        A2, B2, C2 = equ(start2, end2)
        m = A1 * B2 - A2 * B1
        if m == 0:
            # 平行
            if C1 != C2: return []
            # 共线
            res = []
            if check(start1, start2, end2):
                res.append(start1)
            if check(start2, start1, end1):
                res.append(start2)
            if check(end1, start2, end2):
                res.append(end1)
            if check(end2, start1, end1):
                res.append(end2)
            if not res: return []
            return sorted(res)[0]
        else:
            # 交点坐标
            x = (C2 * B1 - C1 * B2) / m
            y = (C1 * A2 - C2 * A1) / m
            if check([x, y], start1, end1) and check([x, y], start2, end2):
                return [x, y]
            return []


a = Solution()
print(a.intersection([0, 0],
                     [3, 3],
                     [1, 1],
                     [2, 2]))
print(a.intersection([0, 0],
                     [1, -1],
                     [0, 0],
                     [-1, 1]))
print(a.intersection([-10, 48],
                     [-43, 46],
                     [-16, 59],
                     [-1, 85]))
