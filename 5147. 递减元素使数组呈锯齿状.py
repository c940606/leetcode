class Solution:
    def movesToMakeZigzag(self, nums) -> int:
        # 判断最大值 和 最小值
        n = len(nums)
        res = float("inf")
        # 最大值
        big = [float("-inf")] + nums + [float("-inf")]
        cur = 0
        for i in range(1, n + 1, 2):
            if big[i] > big[i - 1] and big[i] > big[i + 1]:
                continue
            if big[i] <= big[i - 1]:
                cur += (big[i - 1] - big[i] + 1)
                big[i - 1] = big[i] - 1
            if big[i] <= big[i + 1]:
                cur += (big[i + 1] - big[i] + 1)
                big[i + 1] = big[i] - 1
        res = min(res, cur)
        #print(res)
        # 最小值
        small = [float("inf")] + nums + [float("inf")]
        cur = 0
        for i in range(1, n + 1, 2):
            if small[i] < small[i - 1] and small[i] < small[i + 1]:
                continue
            else:
                cur += small[i] - min(small[i - 1], small[i + 1]) + 1
                small[i] = min(small[i - 1], small[i + 1]) - 1
        res = min(res, cur)
        return res


a = Solution()
print(a.movesToMakeZigzag([1, 3, 3]))
print(a.movesToMakeZigzag(nums = [9,6,1,6,2]))
print(a.movesToMakeZigzag([1]))
