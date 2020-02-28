class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []

        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == "#":
                res.append(s[i:i+2])
                i += 3
            else:
                res.append(s[i])
                i += 1
        lookup = {}
        j = 1
        for a in range(ord("a"), ord('z') + 1):
            lookup[str(j)] = chr(a)
            j += 1
        ans = ""
        for b in res:
            ans += lookup[b]
        return ans
a = Solution()
print(a.freqAlphabets("1"))
print(a.freqAlphabets(s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))