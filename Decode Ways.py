import functools


class Solution:
    def numDecodings1(self, s):
        """
        一条包含字母 A-Z 的消息通过以下方式进行了编码：
            'A' -> 1
            'B' -> 2
            ...
            'Z' -> 26
            给定一个只包含数字的非空字符串，请计算解码方法的总数
        :type s: str
        :rtype: int
        """
        n = len(s)
        lookup = [0] * n
        if not s or s[0] == "0":
            return 0
        lookup[0] = 1
        if n == 1: return 1
        if n >= 1 and s[1] != "0" and s[0] + s[1] <= "26":
            lookup[1] = 2
        elif s[1] == "0" and s[0] >= "3":
            lookup[1] = 0
        else:
            lookup[1] = 1
        # return lookup
        temp = 2
        while temp < n:
            if s[temp] == "0":
                if s[temp - 1] == "0" or s[temp - 1] >= "3":
                    return 0
                if s[temp - 1] + s[temp] <= "26":
                    lookup[temp] = lookup[temp - 2]
                    temp += 1
                    continue
            if s[temp] != "0":
                if s[temp - 1] == "0":
                    lookup[temp] = lookup[temp - 1]
                    temp += 1
                    continue
                if s[temp - 1] + s[temp] <= "26":
                    lookup[temp] = lookup[temp - 1] + lookup[temp - 2]
                    temp += 1
                    continue
                else:
                    lookup[temp] = lookup[temp - 1]
                    temp += 1
        return lookup

    @functools.lru_cache(None)
    def numDecodings2(self, s):
        if not s:
            return 1
        ans = 0
        if len(s) >= 1 and s[0] != '0':
            ans += self.numDecodings(s[1:])
        if len(s) >= 2 and s[0] != '0' and int(s[:2]) <= 26:
            ans += self.numDecodings(s[2:])
        return ans

    def numDecodings(self, s):
        dp = [0] * len(s)
        # 考虑第一个字母
        if s[0] == "0":
            return 0
        else:
            dp[0] = 1
        if len(s) == 1: return dp[-1]
        # 考虑第二个字母

        if s[1] != "0":
            dp[1] += 1
        if 10 <= int(s[:2]) <= 26:
            dp[1] += 1
        for i in range(2, len(s)):

            if s[i - 1] + s[i] == "00": return 0
            if s[i] != "0":
                dp[i] += dp[i - 1]
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]


a = Solution()
s = "301"
print(a.numDecodings(s))
print(a.numDecodings("123"))
