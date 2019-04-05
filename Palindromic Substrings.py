class Solution(object):
    def countSubstrings(self, s):
        """
        给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
        具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。
        --
        输入: "abc"
        输出: 3
        解释: 三个回文子串: "a", "b", "c".
        ---
        输入: "aaa"
        输出: 6
        说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
        ---
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        n = len(s)
        i = 0
        res = []
        while i < n:
            j = 0
            temp = 0
            while j <= i:
                if s[i - j:i + 1] == s[i - j:i + 1][::-1]:
                    temp += 1
                j += 1
            res.append(temp)
            i += 1
            print(res)
        return sum(res)

    def countSubstrings1(self, s):
        n = len(s)
        self.res = 0

        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                self.res += 1
                i -= 1
                j += 1

        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return self.res

    def countSubstrings2(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(n):
            for j in range(i, -1, -1):
                if s[i] == s[j] and (i - j + 1 <= 2 or dp[i - 1][j + 1]):
                    #print(i,j)
                    dp[i][j] = 1
                if dp[i][j]:res += 1
        return res


a = Solution()
print(a.countSubstrings2("aba"))
