class Solution:
    def commonChars(self, A) :
        from collections import Counter
        if not A:
            return []
        lookup = Counter(A[0])
        for a in A[1:]:
            tmp = Counter(a)
            c = Counter()
            for t in (tmp & lookup):
                c[t] = min(tmp[t],lookup[t])
            lookup = c
        return list(lookup.elements())

a = Solution()
print(a.commonChars(["bella","label","roller"]))
print(a.commonChars(["cool","lock","cook"]))