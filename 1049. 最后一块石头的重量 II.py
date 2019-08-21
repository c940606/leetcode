class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import bisect
        stones.sort()
        while len(stones) > 1:
            tmp = []
            for i in range(len(stones) - 1):
                tmp.append(stones[i + 1] - stones[i])
           # print(tmp)
            idx = tmp.index(min(tmp))
            stones = stones[:idx] + stones[idx + 2:]

            if min(tmp) != 0:
                bisect.insort_left(stones, min(tmp))
        print(stones)

    def lastStoneWeightII1(self, stones):
        from  collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 1
        sum_s = 0
        for stone in stones:
            sum_s += stone
            for i in dp:
                if i - stone >= 0:
                    dp


a = Solution()
print(a.lastStoneWeightII([2,7,4,1,8,1]))
