class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def check_other(x, y):
            return (x - x_center) ** 2 + (y - y_center) ** 2 <= radius ** 2

        # 判断矩形四点在园内

        def check(a1, b1, a2, b2):
            # 上
            if y_center > b2 and a1 <= x_center <= a2:
                return (y_center - b2) <= radius
            if y_center < b1 and a1 <= x_center <= a2:
                return (b1 - y_center) <= radius
            if x_center < a1 and b1 <= y_center <= b2:
                return (a1 - x_center) <= radius
            if x_center > a2 and b1 <= y_center <= b2:
                return (x_center - a2) <= radius
            return False

        if check_other(x1, y1) or check_other(x1, y2) or check_other(x2, y1) or check_other(x2, y2):
            return True
        if check(x1, y1, x2, y2): return True

        # 判断圆心是否在矩形内
        if x1 <= x_center <= x2 and y1 <= y_center <= y2:
            return True
        return False


a = Solution()
print(a.checkOverlap(radius=1, x_center=0, y_center=0, x1=1, y1=-1, x2=3, y2=1))
