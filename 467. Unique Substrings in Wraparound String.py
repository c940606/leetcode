class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        dp[p[0]], curMaxLen = 1, 1
        for idx in range(1, len(p)):
            if (ord(p[idx]) - ord(p[idx - 1])) % 26 == 1:
                curMaxLen += 1
            else:
                curMaxLen = 1
            dp[p[idx]] = max(dp[p[idx]], curMaxLen)
        return sum(dp.values())

    def findSubstringInWraproundString1(self, p: str) -> int:
        from collections import defaultdict
        dp = defaultdict(int)
        dp[p[0]], curMaxLen = 1, 1
        for prev, nxt in zip(p, p[1:]):
            curMaxLen = curMaxLen + 1 if (ord(nxt) - ord(prev)) % 26 == 1 else 1
            dp[nxt] = max(dp[nxt], curMaxLen)
        return sum(dp.values())


a = Solution()
print(a.findSubstringInWraproundString("zab"))
print(a.findSubstringInWraproundString("cofzxdlhnf"))
