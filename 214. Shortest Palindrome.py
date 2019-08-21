class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        # 返回两个单相同的前缀长度
        def helper(s1, s2):
            tmp = 0
            for idx, val in enumerate(zip(s1[::-1], s2), 0):
                # print(idx, val)
                if val[0] == val[1]:
                    tmp += 1
            return tmp

        # print(helper("aacecaaa", ""))
        n = len(s)
        # res = ""
        max_len = 0
        even_max_loc = None
        odd_max_loc = None
        for idx, alp in enumerate(s[:n // 2 + 1]):
            if idx >= 1 and s[idx] == s[idx - 1]:
                t = helper(s[:idx - 1], s[idx + 1:])
                if t >= max_len:
                    max_len = t
                    even_max_loc = idx
            t = helper(s[:idx], s[idx + 1:])
            print(t)
            if t > max_len:
                max_len = t
                odd_max_loc = idx
        print(even_max_loc, odd_max_loc)
        if even_max_loc and odd_max_loc:
            if n - even_max_loc - 1 <= n - odd_max_loc - 1:
                return s[even_max_loc + 1:][::-1] + s[even_max_loc] * 2 + s[even_max_loc + 1:]
            else:
                return s[odd_max_loc + 1:][::-1] + s[odd_max_loc] + s[odd_max_loc + 1:]
        if odd_max_loc:
            return s[odd_max_loc + 1:][::-1] + s[odd_max_loc] + s[odd_max_loc + 1:]
        if even_max_loc:
            return s[even_max_loc + 1:][::-1] + s[even_max_loc] * 2 + s[even_max_loc + 1:]
        return s[1:][::-1] + s[0] + s[1:]

    def shortestPalindrome1(self, s: str) -> str:
        n = len(s)
        i = n // 2
        while i >= 0:
            # 奇
            tmp1 = s[:i]
            tmp2 = s[i + 1:]
            # print(tmp1,tmp2)
            if tmp2.find(tmp1[::-1]) == 0:
                return s[i + 1:][::-1] + s[i] + s[i + 1:]
            # 偶
            if i > 0 and s[i - 1] == s[i]:
                tmp1 = s[:i - 1]
                tmp2 = s[i + 1:]
                if tmp2.find(tmp1[::-1]) == 0:
                    return s[i + 1:][::-1] + s[i] + s[i] + s[i + 1:]
            i -= 1

    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1: return s
        def helper(i, j):
            return s[j:].startswith(s[:i + 1][::-1])

        for i in range((n - 1) // 2, -1, -1):
            # 偶数
            if s[i] == s[i + 1] and helper(i, i + 1):
                return s[i + 1:][::-1] + s[i + 1:]
            if helper(i, i):
                # print(i)
                return s[i + 1:][::-1] + s[i:]



a = Solution()
print(a.shortestPalindrome("aacecaaa"))
print(a.shortestPalindrome("abcd"))
print(a.shortestPalindrome("ab"))
print(a.shortestPalindrome("aba"))
print(a.shortestPalindrome("aabba"))
