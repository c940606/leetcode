class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last = {c: i for i, c in enumerate(text)}
        res = ""
        left = 0
        while last:
            right = min(last.values())
            c, i = min((text[i], i) for i in range(left, right + 1) if text[i] not in res)
            res += c
            left = i + 1
            last.pop(c)
        return res
