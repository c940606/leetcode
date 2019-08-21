class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i = 0
        j = 0
        start = -1
        match = 0
        while i < len(s):
            if j < len(p) and (p[j] == "?" or s[i] == p[j]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                start = j
                match = i
                i += 1
            elif start != -1:
                j = start + 1
                match += 1
                i = match
            else:
                return False
        return all(x == "*" for x in p[j:])

    def isMatch1(self, s, p):
        # afafaf
        # *f
        i = 0
        j = 0
        start = -1
        match = 0
        while i < len(s):
            print(i, j)
            if j < len(p) and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                start = j
                match = i
                j += 1
            elif start != -1:
                j = start + 1
                match += 1
                i = match
            else:
                return False
        return all(x == "*" for x in p[j:])

    def isMatch2(self, s, p):
        sn = len(s)
        pn = len(p)
        dp = [[False] * (pn + 1) for _ in range(sn + 1)]
        dp[0][0] = True
        for j in range(1, pn + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, sn + 1):
            for j in range(1, pn + 1):
                if (s[i - 1] == p[j - 1] or p[j - 1] == "?"):
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]


a = Solution()
print(a.isMatch2("afafaf", "*f"))
