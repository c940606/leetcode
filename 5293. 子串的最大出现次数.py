class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        for i in range(len(s)):
            for j in range(minSize, min(26, maxSize) + 1):
                if i + j > len(s): break
                tmp = s[i:i + j]
                if len(set(tmp)) > maxLetters: break
                lookup[tmp] += 1
        return max(lookup.values(), default=0)


a = Solution()
print(a.maxFreq(s="aababcaab", maxLetters=2, minSize=3, maxSize=4))
print(a.maxFreq(s="aaaa", maxLetters=1, minSize=3, maxSize=3))
print(a.maxFreq(s="aabcabcab", maxLetters=2, minSize=2, maxSize=3))
print(a.maxFreq(s="abcde", maxLetters=2, minSize=3, maxSize=3))
