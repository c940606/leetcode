class Solution:
    def smallestStringWithSwaps(self, s: str, pairs) -> str:
        from collections import defaultdict
        f = {}

        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        lookup = defaultdict(list)
        for x, y in pairs:
            union(x, y)
        for i in range(len(s)):
            lookup[find(i)].append(s[i])

        for k in lookup.keys():
            lookup[k].sort(reverse=True)

        res = ""
        for i in range(len(s)):
            res += lookup[find(i)].pop()
        # print(lookup)
        return res


a = Solution()
print(a.smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]))
