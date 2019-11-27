import functools


class Solution:
    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]


    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @functools.lru_cache(None)
        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + helper(i + 1, j + 1)
            return max(helper(i + 1, j), helper(i, j + 1))
        return helper(0, 0)


a = Solution()
print(a.longestCommonSubsequence(text1="abcde", text2="ace"))
print(a.longestCommonSubsequence(text1="abc", text2="def"))
