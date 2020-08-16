from typing import List
import collections
import heapq
import bisect

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        import string
        if s2 < s1 :return 0
        res  = 0
        mod = 10 ** 9 + 7
        def dfs(cur):
            nonlocal  res


            if len(cur) == n and evil not in cur and s1 <= cur <= s2:
                res += 1
                return
            if len(cur) >= n:
                return
            for tmp in string.ascii_lowercase:
                dfs(cur + tmp)
        dfs("")
        return res % mod

a = Solution()
# print(a.findGoodStrings(n = 2, s1 = "aa", s2 = "da", evil = "b"))
print(a.findGoodStrings(8, "leetcode", "leetgoes", "leet"))