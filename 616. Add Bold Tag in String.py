class Solution:
    def addBoldTag(self, s: str, dict):
        lookup = set()
        for d in dict:
            left = 0
            while True:
                loc = s.find(d, left)
                if loc == -1:
                    break
                for i in range(loc, loc + len(d)):
                    lookup.add(i)
                left = loc + 1
        # print(lookup)
        res = ""
        i = 0
        while i < len(s):
            left = i
            while i < len(s) and i in lookup:
                i += 1
            # print(left, i)
            if left == i:
                res += s[i]
                i += 1
            else:
                res += "<b>"
                for j in range(left, i):
                    res += s[j]
                res += "</b>"
        return res


a = Solution()
print(a.addBoldTag(s="abcxyz123", dict=["abc", "123"]))
print(a.addBoldTag(s="aaabbcc", dict=["aaa", "aab", "bc"]))
print(a.addBoldTag("dfad", ["d"]))
