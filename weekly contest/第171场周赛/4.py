class Solution:
    def minimumDistance(self, word: str) -> int:
        from functools import lru_cache
        def cal(f, tmp):
            a, b = divmod(f, 6)
            c, d = divmod(tmp, 6)
            return abs(a - c) + abs(b - d)

        @lru_cache(None)
        def helper(f1, f2, loc):
            if loc == len(word):
                return 0
            tmp = ord(word[loc]) - ord("A")
            return min(cal(f1, tmp) + helper(tmp, f2, loc + 1), cal(f2, tmp) + helper(f1, tmp, loc + 1))

        res = float("inf")
        for i in range(1, len(word)):
            res = min(res, helper(ord(word[0]) - 65, ord(word[i]) - 65, 1))

        return res

a = Solution()
print(a.minimumDistance(word = "CAKE"))
print(a.minimumDistance(word = "HAPPY"))
print(a.minimumDistance(word = "NEW"))
print(a.minimumDistance(word = "YEAR"))
