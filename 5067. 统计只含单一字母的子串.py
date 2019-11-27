class Solution:
    def countLetters(self, S: str) -> int:
        from itertools import groupby

        res = 0

        def helper(n):
            return (1 + n) * n // 2

        for idx, item in groupby(S):
            res += helper(len(list(item)))

        return res


a = Solution()
print(a.countLetters("aaaba"))
print(a.countLetters("aaaaaaaaaa"))
print(a.countLetters("a"))
