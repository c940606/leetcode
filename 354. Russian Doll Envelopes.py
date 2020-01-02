from typing import List


class Solution:
    def maxEnvelopes1(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        dp = [1] * len(envelopes)
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[j][0] != envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        import bisect
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        arr = []
        for _, y in envelopes:
            loc = bisect.bisect_left(arr, y)
            arr[loc:loc+1] = [y]
        return len(arr)


a = Solution()
# print(a.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
# print(a.maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]))
# print(a.maxEnvelopes([[1,2],[1,3]]))
# print(a.maxEnvelopes([[1, 3], [3, 5], [6, 7], [6, 8], [8, 4], [9, 5]]))
print(a.maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
print(a.maxEnvelopes([[30, 50], [12, 2], [3, 4], [12, 15]]))
