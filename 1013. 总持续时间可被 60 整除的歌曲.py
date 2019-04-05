class Solution:
    def numPairsDivisibleBy60(self, time) -> int:
        from collections import Counter
        time_count = Counter(time)
        res = 0
        lookup = {i * 60 for i in range(1, 17) if i * 60 < 1001}
        for t in time:
            for k in lookup:
                tmp = k - t
                if tmp == t:
                    res += (time_count[tmp] - 1)
                else:
                    res += time_count[tmp]
        return res // 2

    def numPairsDivisibleBy601(self, time) -> int:
        from collections import Counter
        c = Counter()
        res = 0
        for t in time:
            res += c[60 - t % 60]
            c[t % 60] += 1
        return res


a = Solution()
print(a.numPairsDivisibleBy601([30, 20, 150, 100, 40]))
print(a.numPairsDivisibleBy60([60, 60, 60]))
