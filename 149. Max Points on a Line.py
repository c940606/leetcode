class Solution:
    def maxPoints1(self, points):
        from collections import defaultdict

        n = len(points)

        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        # print(gcd(10, 120))
        res = 0

        for i in range(n):
            lookup = defaultdict(lambda: 1)
            duplicate = 0
            tmp_max = 0
            for j in range(i + 1, n):
                x = points[i][0] - points[j][0]
                y = points[i][1] - points[j][1]
                if x == 0 and y == 0:
                    duplicate += 1
                    continue
                # print(x, y)
                # g = gcd(x, y)
                # if g != 0:
                #     x /= g
                #     y /= g
                if x == 0:
                    lookup[str(y) + "#"] += 1
                    tmp_max = max(tmp_max, lookup[str(y) + "#"])
                else:
                    tmp = y * 1000 / x * 1000
                    lookup[tmp] += 1
                    tmp_max = max(tmp_max, lookup[tmp])
            res = max(res, tmp_max + duplicate + 1)
        return res

    def maxPoints(self, points):
        from collections import Counter, defaultdict
        # 所有点统计
        points_dict = Counter(tuple(point) for point in points)
        # 把唯一点列举出来
        not_repeat_points = list(points_dict.keys())
        n = len(not_repeat_points)
        if n == 1: return points_dict[not_repeat_points[0]]
        res = 0
        # 求最大公约数
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)

        for i in range(n - 1):
            # 点1
            x1, y1 = not_repeat_points[i][0], not_repeat_points[i][1]
            # 斜率
            slope = defaultdict(int)
            for j in range(i + 1, n):
                # 点2
                x2, y2 = not_repeat_points[j][0], not_repeat_points[j][1]
                dy, dx = y2 - y1, x2 - x1
                # 方式一 利用公约数
                g = gcd(dy, dx)
                if g != 0:
                    dy //= g
                    dx //= g
                slope["{}/{}".format(dy, dx)] += points_dict[not_repeat_points[j]]
                # --------------------
                # 方式二, 利用除法(不准确, 速度快)
                # if dx == 0:
                #     tmp = "#"
                # else:
                #     tmp = dy * 1000 / dx * 1000
                # slope[tmp] += points_dict[not_repeat_points[j]]
                #------------------------------
            res = max(res, max(slope.values()) + points_dict[not_repeat_points[i]])

        return res


a = Solution()
print(a.maxPoints([[1, 1], [2, 2], [3, 3]]))
