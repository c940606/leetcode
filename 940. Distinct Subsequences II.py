class Solution:
    def distinctSubseqII(self, S: str) -> int:
        n = len(S)
        M = 1000000007
        res = 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if S[i] != S[j]:
                    dp[i] += dp[j]
                    dp[i] %= M
            res += dp[i]
            res %= M
        return res

    def distinctSubseqII1(self, S: str) -> int:
        from  collections import defaultdict
        cou = defaultdict(int)
        n = len(S)
        dp = [1] * n
        res = 0
        M = 1000000007
        for  i in range(n):
            dp[i] += res - cou[S[i]]
            res = res + dp[i]
            cou[S[i]] = dp[i] + cou[S[i]]
        return res %  M

a = Solution()
print(a.distinctSubseqII1("abc"))