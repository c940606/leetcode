class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        len_s = len(s)
        dp = [[0] * len_s for _ in range(len_s)]
        # base case 每个字符可以是一个回文串
        for i in range(len_s):
            dp[i][i] = 1
        for i in range(len_s - 1, -1, -1):
            for j in range(i + 1, len_s):
                # 长度加2
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return len(s) - dp[0][-1] <= k

a = Solution()
print(a.isValidPalindrome(s = "abcdeca", k = 2))
