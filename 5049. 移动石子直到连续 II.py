class Solution:
    def numMovesStonesII(self, stones):
        res = []
        n = len(stones)
        stones.sort()

        # 连续
        def helper1(stones):
            i = 0
            while i < n - 1 and stones[i] + 1 == stones[i + 1]:
                i += 1
            if i == n:
                return True
            else:
                return False

        def helper2(stones):
            tmp = 0
            for i in range(1, n):
                tmp += (stones[i] - stones[i - 1] - 1)
            if tmp == 1:
                return True
            else:
                return False

        if helper1(stones):
            res[0] = 0
        elif helper2(stones):
            res[0] = 1

    def numMovesStonesII1(self, stones):
        stones.sort()
        n = len(stones)
        res = [n, 0]
        i = 0
        for j in range(n):
            # 维护n大小的窗口
            while stones[j] - stones[i] >= n:
                i += 1
            # 考虑边界情况
            if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                res[0] = min(res[0], 2)
            else:
                res[0] = min(res[0], n - (j - i + 1))
        res[1] = max(stones[n - 1] - n + 2 - stones[1], stones[n - 2] - stones[0] - n + 2)
        return res
