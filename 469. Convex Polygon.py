class Solution:
    def isConvex(self, points):
        n = len(points)
        pre = 0
        for i in range(n):
            x1 = points[(i + 1) % n][0] - points[i][0]
            x2 = points[(i + 2) % n][0] - points[i][0]
            y1 = points[(i + 1) % n][1] - points[i][1]
            y2 = points[(i + 2) % n][1] - points[i][1]
            cur = x1 * y2 - x2 * y1
            if cur != 0:
                if cur * pre < 0:
                    return False
                else:
                    pre = cur
        return True
