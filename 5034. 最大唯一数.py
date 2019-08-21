class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        from collections import Counter
        c = Counter(A)
        for x, y in sorted(c.items())[::-1]:
            if y == 1:
                return x