import functools


class Solution:
    def isMatch1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # if not s or not p:
        # return False
        s_len = len(s)
        p_len = len(p)
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        # print(dp)
        dp[0][0] = True
        for i in range(p_len):
            if p[i] == "*" and dp[0][i - 1]:
                dp[0][i + 1] = True
        # print(dp)
        for i in range(s_len):
            for j in range(p_len):
                if p[j] == s[i] or p[j] == ".":
                    dp[i + 1][j + 1] = dp[i][j]
                if p[j] == "*":
                    if p[j - 1] != s[i] and p[j - 1] != ".":
                        dp[i + 1][j + 1] = dp[i + 1][j - 1]
                    else:
                        dp[i + 1][j + 1] = (dp[i + 1][j] or dp[i + 1][j - 1] or dp[i][j + 1])
        # print(dp)
        return dp[-1][-1]

    @functools.lru_cache(None)
    def isMatch(self, s, p):
        if not p: return not s
        # s 和 p 首位置 匹配, 我们只需比较s的下一位和p 或者p[2:]是否匹配
        if s and len(p) >= 2 and (s[0] == p[0] or p[0] == ".") and p[1] == "*" and (
                self.isMatch(s[1:], p) or self.isMatch(s[1:], p[2:])):
            return True
        # s 和 p 首位置不匹配, 但是p的下个位置是* 所以可以跳到p[2:]
        elif s and len(p) >= 2 and s[0] != p[0] and p[1] == "*" and self.isMatch(s, p[2:]):
            return True
        # s 和 p 首位置匹配, 接着匹配下一个
        elif s and (s[0] == p[0] or p[0] == ".") and self.isMatch(s[1:], p[1:]):
            return True
        # 防止s为空 p还剩 ".*" 这种情况
        elif len(p) >= 2 and p[1] == "*" and self.isMatch(s, p[2:]):
            return True
        return False


if __name__ == '__main__':
    a = Solution()
    # print(a.isMatch(s="aab", p="c*a*b"))
    # print(a.isMatch("ab", ".*"))
    # print(a.isMatch("", ".*"))
    print(a.isMatch("mississippi", "mis*is*ip*."))
