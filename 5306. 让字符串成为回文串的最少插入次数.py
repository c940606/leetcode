class Solution:
    def minInsertions(self, s: str) -> int:
        from functools import lru_cache
        text1 = s
        text2 = s[::-1]
        @lru_cache(None)
        def helper(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                return 1 + helper(i + 1, j + 1)
            return max(helper(i + 1, j), helper(i, j + 1))
        # print(helper(0, 0))
        return len(s) - helper(0, 0)

a = Solution()
print(a.minInsertions("leetcode"))
print(a.minInsertions("mbadm"))
print(a.minInsertions("zzazz"))
