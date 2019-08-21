class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(str1, str2):
            n, m = len(str1), len(str2)
            dp = [[""] * (m + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if str1[i - 1] == str2[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], key=len)
            # print(dp)
            return dp[-1][-1]

        # print(lcs(str1, str2))
        res = ""
        i = 0
        j = 0
        for c in lcs(str1, str2):
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i += 1
            j += 1
        return res + str1[i:] + str2[j:]


a = Solution()
print(a.shortestCommonSupersequence("abac", "cab"))
