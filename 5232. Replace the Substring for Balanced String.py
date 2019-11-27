class Solution:
    def balancedString1(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        target = len(s) // 4
        res = float("inf")
        left = right = 0
        while left < len(s):
            while right < len(s) and (c["Q"] > target or c["W"] > target or
                                      c["E"] > target or c["R"] > target):
                c[s[right]] -= 1
                right += 1
            if c["Q"] <= target and c["W"] <= target and c["E"] <= target and c["R"] <= target:
                res = min(res, right - left)
            c[s[left]] += 1
            left += 1
        return res

    def balancedString(self, s: str) -> int:
        from collections import Counter
        c = Counter(s)
        target = len(s) // 4
        res = float("inf")
        left = 0
        for right in range(len(s)):
            if sum(c.values()) - 4 * target

a = Solution()
print(a.balancedString(s="QWER"))
print(a.balancedString(s="QQWE"))
print(a.balancedString(s="QQQQ"))
print(a.balancedString(s="QQQW"))
print(a.balancedString("QWERQQQQ"))
