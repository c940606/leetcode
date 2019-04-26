class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        from collections import defaultdict
        f = {}

        def find(x):
            f.setdefault(x, x)
            while f[x] != x:
                x = f[x]
            return x

        def union(x, y):
            a = find(x)
            b = find(y)
            if a != b:
                f[find(y)] = find(x)

        for a, b in zip(A, B):
            union(a,b)
        #print(f)
        # print((set(map(find,f))))p =
        lookup = defaultdict(list)
        for alp in set(A+B):
            lookup[find(alp)].append(alp)
        for key, val in lookup.items():
            val.sort()

        #print(lookup)
        res = ""
        for i in S:
            tmp  = lookup[find(i)]
            #print(tmp)
            if  tmp:
                res += tmp[0]
            else:
                res += i

        return res


a = Solution()
print(a.smallestEquivalentString(A = "parker", B = "morris", S = "parser"))
print(a.smallestEquivalentString(A = "hello", B = "world", S = "hold"))
print(a.smallestEquivalentString(A = "leetcode", B = "programs", S = "sourcecode"))
print(a.smallestEquivalentString("dfeffdfafbbebbebacbbdfcfdbcacdcbeeffdfebbdebbdafff",
                                 "adcdfabadbeeafeabbadcefcaabdecabfecffbabbfcdfcaaae",
                                 "myickvflcpfyqievitqtwvfpsrxigauvlqdtqhpfugguwfcpqv"))
