class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        return sum((Counter(s) - Counter(t)).values())
a = Solution()
print(a.minSteps(s = "anagram", t = "mangaar"))