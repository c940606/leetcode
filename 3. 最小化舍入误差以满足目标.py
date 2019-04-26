class Solution:
    def minimizeError(self, prices, target):
        import math
        prices = [float(i) for i in prices]
        data = []
        for p in prices:
            if math.ceil(p) == math.floor(p):
                data.append([math.ceil(p)])
            else:
                data.append([math.ceil(p), math.floor(p)])
        # print(data)
        n = len(prices)
        self.res = None

        def helper(i, cur_sum, t):
            if i == n and cur_sum == 0:
                self.res = t
                return
            if cur_sum < 0 or i >= n:
                return
            for tmp in data[i]:
                if cur_sum > tmp:
                    helper(i + 1, cur_sum - tmp, t + [tmp])

        helper(0, target, [])
        # print(self.res)
        if self.res == None:
            return "-1"
        r = sum([abs(round(a, 3) - b) for a, b in zip(self.res, prices)])
        # ans = str(round(r, 3))
        return "%.3f" % round(r, 3)


a = Solution()
print(a.minimizeError(prices=["0.700", "2.800", "4.900"], target=8))
print(a.minimizeError(prices=["1.500", "2.500", "3.500"], target=10))
print(a.minimizeError(
    ["20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000",
     "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000",
     "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000",
     "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000", "20.000",
     "20.000", "20.000", "20.000", "20.000", "20.000", "20.000"], 999))
print(a.minimizeError(
    ["20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500",
     "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500",
     "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500",
     "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500", "20.500",
     "20.500", "20.500", "20.500", "20.500", "20.500", "20.500"], 999))
