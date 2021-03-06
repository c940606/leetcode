class Solution(object):
    def isSubsequence1(self, s, t):
        """
        给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
        你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
        字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。
        （例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
---
        示例 1:
        s = "abc", t = "ahbgdc"
        返回 true.
        ---
        示例 2:
        s = "axc", t = "ahbgdc"
        返回 false.


        :type s: str
        :type t: str
        :rtype: bool
        """
        # b.issubset(a)
        if not set(s).issubset(set(t)):
            return False
        for i in s:
            idx = t.find(i)
            if idx == -1:
                return False
            else:
                t = t[idx + 1:]
        return True

    def isSubsequence(self, s, t):
        from collections import defaultdict
        import bisect

        lookup = defaultdict(list)
        for idx, val in enumerate(t):
            lookup[val].append(idx)
        loc = -1
        for a in s:
            j = bisect.bisect_left(lookup[a], loc + 1)
            if loc >= len(lookup[a]): return False
            loc = lookup[a][j]
        return True
