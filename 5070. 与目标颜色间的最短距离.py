class Solution:
    def shortestDistanceColor2(self, colors, queries):
        from collections import defaultdict
        import bisect
        color_loc = defaultdict(list)
        for i, color in enumerate(colors):
            color_loc[color].append(i)
        # print(color_loc)
        res = []
        for x, y in queries:
            loc = color_loc[y]
            if not loc:
                res.append(-1)
                continue
            l = bisect.bisect_left(loc, x)
            # print(x, y , loc, l)
            tmp = float("inf")
            if l < len(loc):
                tmp = min(tmp, abs(loc[l] - x))
            if l + 1 < len(loc):
                tmp = min(tmp, abs(loc[l + 1] - x))
            if l - 1 >= 0:
                tmp = min(tmp, abs(loc[l - 1] - x))
            if l == len(loc):
                tmp = min(tmp, abs(loc[l - 1] - x))
            res.append(tmp)

        return res

    def shortestDistanceColor(self, colors, queries):
        n = len(colors)
        left_dp = [[float("inf"), float("inf"), float("inf")]]
        left_dp[0][colors[0] - 1] = 0
        for i in range(1, n):
            tmp = left_dp[-1].copy()
            for j in range(3):
                if tmp[j] != float("inf"):
                    tmp[j] += 1
            tmp[colors[i - 1] - 1] = 1
            tmp[colors[i ] - 1] = 0
            left_dp.append(tmp)
        right_dp = [[float("inf"), float("inf"), float("inf")]]
        right_dp[0][colors[-1] - 1] = 0
        for i in range(n - 2, -1, -1):
            tmp = right_dp[-1].copy()
            for j in range(3):
                if tmp[j] != float("inf"):
                    tmp[j] += 1
            tmp[colors[i + 1] - 1] = 1
            tmp[colors[i] - 1] = 0
            right_dp.append(tmp)
        right_dp = right_dp[::-1]
        ##print(right_dp)
        res = []
        for x, y in queries:
            left = left_dp[x][y - 1]
            right = right_dp[x][y - 1]
            if left != float("inf") and right != float("inf"):
                res.append(min(left, right))
            elif left != float("inf") :
                res.append(left)
            elif right != float("inf"):
                res.append(right)
            else:
                res.append(-1)
        return res



a = Solution()
print(a.shortestDistanceColor(colors=[1, 1, 2, 1, 3, 2, 2, 3, 3], queries=[[1, 3], [2, 2], [6, 1]]))
print(a.shortestDistanceColor(colors=[1, 2], queries=[[0, 3]]))
print(a.shortestDistanceColor([3, 2, 2, 1, 3, 1, 1, 1, 3, 1],
                              [[4, 1], [9, 2], [4, 2], [8, 1], [0, 3], [2, 1], [2, 3], [6, 3], [4, 1], [1, 2]]))
