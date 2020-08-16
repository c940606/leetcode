from typing import List
import collections


class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        cur = set([s[-1]])
        dp[-1] = 1
        for i in range(n - 2, -1, -1):
            if s[i] in cur:
                dp[i] = dp[i + 1]
            else:
                dp[i] = dp[i + 1] + 1
                cur.add(s[i])
        # print(dp)
        cur = set()
        tmp = 0
        res = 0
        for i in range(n - 1):
            # print(i, cur, tmp, dp[i])
            if s[i] not in cur:
                cur.add(s[i])
                tmp += 1
            if tmp == dp[i + 1]:
                res += 1
        return res
                



a = Solution()
# print(a.numSplits("aa"))
print(a.numSplits("aacaba"))
            