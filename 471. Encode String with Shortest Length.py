import functools


class Solution:
    @functools.lru_cache(None)
    def encode2(self, s: str) -> str:
        res = s
        for i in range(1, len(s) + 1):
            tmp = s[:i]
            res = min(res, tmp + self.encode(s[i:]))
            cnt = 1
            j = i
            while s[j:].find(tmp) == 0:
                cnt += 1
                j += len(tmp)
                res = min(res, str(cnt) + "[" + self.encode(tmp) + "]" + self.encode(s[j:]), key=len)
        return res

    @functools.lru_cache(None)
    def encode1(self, s: str) -> str:
        res = s
        if len(s) < 5: return res
        loc = (s + s).find(s, 1)
        if loc < len(s):
            res = str(len(s) // loc) + "[" + self.encode(s[:loc]) + "]"
        for i in range(1, len(s)):
            left = self.encode(s[:i])
            right = self.encode(s[i:])
            res = min(res, left + right, key=len)
        return res

    def encode(self, s: str) -> str:

        dp = {}
        for step in range(1, len(s) + 1):
            for j in range(len(s) - step + 1):
                tmp = s[j:j + step]

                dp.setdefault(tmp, tmp)
                if len(dp[tmp]) < len(tmp): continue
                loc = (tmp + tmp).find(tmp, 1)
                if loc < len(tmp):
                    dp.setdefault(tmp[:loc], tmp[:loc])
                    dp[tmp] = min(dp[tmp], str(len(tmp) // loc) + "[" + dp[tmp[:loc]] + "]", key=len)



                for k in range(1, len(tmp)):
                    left = dp.setdefault(tmp[:k], tmp[:k])
                    right = dp.setdefault(tmp[k:], tmp[k:])
                    dp[tmp] = min(dp[tmp], left + right, key=len)
        # print(dp)
        return dp[s]


a = Solution()
print(a.encode("aaaaa"))

# print(a.encode("aaaaaaaaaa"))
print(a.encode("abbbabbbcabbbabbbc"))
# print(a.encode("aabcaabcd"))
# print(a.encode("a" * 160))
# print(a.encode("aabcccccddd"))
# print(a.encode("aaaaaaaaaaaabbb"))
# print(a.encode("aaaaaaaaaabbbaaaaabbb"))
print(a.encode1("aaaaaaaaaabbbaaaaabbb"))
