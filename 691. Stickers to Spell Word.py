class Solution:
    def minStickers(self, stickers, target):
        from collections import Counter
        import functools
        c_stackers = []
        n = len(stickers)
        # print(n)
        for s in stickers:
            c_stackers.append(Counter(s))
        lookup = {}
        # print(target,c_stackers)
        #@functools.lru_cache(None)
        def backtrack(target):
            if not target:
                return 0
            if target in lookup:return lookup[target]


        backtrack(target)
        return self.res if self.res != float("inf") else -1

    def minStickers1(self, stickers, target):
        from collections import Counter
        stickers = [Counter(s) for s in stickers]
        lookup = {}

        def helper(target):
            if not target: return 0
            if target in lookup: return lookup[target]
            res, cnt = float("inf"), Counter(target)
            for c in stickers:
                if c[target[0]] == 0:continue
                nxt = helper("".join([s * t for (s, t) in (cnt - c).items()]))
                if nxt != -1: res = min(res, nxt + 1)
            lookup[target] = -1 if res == float("inf") else res
            return lookup[target]
        return helper(target)


a = Solution()
print(a.minStickers(["with", "example", "science"], "thehat"))
print(a.minStickers(["notice", "possible"], "basicbasic"))
print(a.minStickers(
    ["control", "heart", "interest", "stream", "sentence", "soil", "wonder", "them", "month", "slip", "table", "miss",
     "boat", "speak", "figure", "no", "perhaps", "twenty", "throw", "rich", "capital", "save", "method", "store",
     "meant", "life", "oil", "string", "song", "food", "am", "who", "fat", "if", "put", "path", "come", "grow", "box",
     "great", "word", "object", "stead", "common", "fresh", "the", "operate", "where", "road", "mean"]
    , "stoodcrease"))
