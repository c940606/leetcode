from pprint import  pprint
class Solution(object):
    def longestPalindromeSubseq5(self, s):
        """
        给定一个字符串s，找到其中最长的回文子序列。可以假设s的最大长度为1000。
        --

        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        # print(dp)
        return dp[0][n - 1]

    def longestPalindromeSubseq1(self, s):
        lookup = {}

        def helper(i, j):
            if i > j:
                return 0
            if i == j: return 1
            if (i, j) in lookup:
                return lookup[(i, j)]
            if s[i] == s[j]:
                lookup[(i, j)] = helper(i + 1, j - 1) + 2
            else:
                lookup[(i, j)] = max(helper(i + 1, j), helper(i, j - 1))
            return lookup[(i, j)]

        return helper(0, len(s) - 1)

    def longestPalindromeSubseq2(self, s):
        s_resver = s[::-1]
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s_resver[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]

    def longestPalindromeSubseq3(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]

    def longestPalindromeSubseq4(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i - 1][j + 1] + 2
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i - 1][j])
        return dp[n - 1][0]

    def longestPalindromeSubseq(self, s):
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        #pprint(dp)
        l = len(s)
        k = 0
        while k != len(s):
            for i in range(l):
                x = i
                y = x + k
                if k == 0:
                    dp[x][y] = 1
                else:
                    if s[x] == s[y]:
                        dp[x][y] = 2 + dp[x + 1][y - 1]
                    else:
                        dp[x][y] = max(dp[x][y - 1], dp[x + 1][y])
            l -= 1
            k += 1
            #pprint(dp)
        return dp[0][-1]


a = Solution()
print(a.longestPalindromeSubseq("bbbab"))
print(a.longestPalindromeSubseq1("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"))
# print(a.longestPalindromeSubseq2("cbbd"))
