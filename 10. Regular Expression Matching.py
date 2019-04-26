class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #if not s or not p:
            #return False
        s_len = len(s)
        p_len = len(p)
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        #print(dp)
        dp[0][0] = True
        for i in range(p_len):
            if p[i] == "*" and dp[0][i - 1]:
                dp[0][i + 1] = True
        #print(dp)
        for i in range(s_len):
            for j in range(p_len):
                if p[j] == s[i] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == "*":
                    if p[j-1] != s[i] and p[j-1] != ".":
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = (dp[i+1][j] or dp[i+1][j-1] or dp[i][j+1])
        #print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    a = Solution()
    print(a.isMatch(s="aab", p="c*a*b"))
    print(a.isMatch("ab",".*"))
    print(a.isMatch("",".*"))
