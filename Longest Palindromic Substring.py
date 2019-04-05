class Solution(object):
    def longestPalindrome(self, s):
        """
        给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
        ----
        输入: "babad"
        输出: "bab"
        注意: "aba"也是一个有效答案。
        ===
        输入: "cbbd"
        输出: "bb"
        --
        思路:

        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 2 or s == s[::-1]:
            return s
        max_len = 1
        start = 0
        for i in range(1, n):
            even = s[i - max_len:i + 1]
            odd = s[i - max_len - 1:i + 1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1
        return s[start:start + max_len]

    def longestPalindrome1(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        max_len = float("-inf")
        res = ""
        for i in range(n):
            # dp[i][i] = 1
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j < 2 or dp[i - 1][j + 1]):
                    dp[i][j] = 1

                if dp[i][j] and i - j + 1 > max_len:
                    # print(222)
                    # print(i,j)
                    max_len = i - j + 1
                    res = s[j:i + 1]
        # print(dp)
        return res

    def longestPalindrome2(self, s):
        self.start = 0
        self.max_len = 0
        n = len(s)
        if n < 2:
            return s

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1

            if self.max_len < j - i - 1:
                # print(i,j)
                self.max_len = j - i - 1
                self.start = i + 1

        for k in range(n):
            # print(k)
            helper(k, k)
            helper(k, k + 1)
        return s[self.start:self.start + self.max_len]
    def longestPalindrome3(self, s):
        lookup = {}

        def helper(i, j):
            if i > j:
                return ""
            if i == j: return s[i]
            if (i, j) in lookup:
                return lookup[(i, j)]
            if s[i] == s[j]:
                lookup[(i, j)] = s[i]+helper(i + 1, j - 1)+s[j]
            else:
                helper(i+1,j)
                helper(i,j-1)

            return lookup[(i, j)]

        return helper(0, len(s) - 1)


a = Solution()
print(a.longestPalindrome3("babad"))
# print(a.longestPalindrome3("babad"))
# print(a.longestPalindrome2(""))
# print(a.longestPalindrome("aa"))
# print(a.longestPalindrome3("cbbd"))
# print(a.longestPalindrome3("aacdefcaa"))
