from typing import List

class Solution:
    def reformat(self, s: str) -> str:
        a = []
        b = []
        for v in s:
            if v.isdigit():
                a.append(v)
            else:
                b.append(v)
        if abs(len(b) - len(a)) > 1: return ""
        if len(b) > len(a):
            a, b = b, a
        res = ""
        for i, j in zip(a, b):
            res += i + j
        if len(a) > len(b):
            res += a[-1]
        return res
a = Solution()
print(a.reformat("abcde123"))