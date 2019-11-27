from  pprint import pprint
class Solution:
    def canMakePaliQueries1(self, s: str, queries):
        from collections import Counter
        prefix = []
        prefix.append(Counter())
        for a in s:
            tmp = prefix[-1].copy()
            tmp[a] += 1
            prefix.append(tmp)
        res = []
        #print(prefix[11] - prefix[1])
        for left, right, k in queries:
            tmp = sum(1 for val in (prefix[right + 1] - prefix[left]).values() if val % 2 == 1)
            if tmp // 2 <= k:
                res.append(True)
            else:
                res.append(False)
        return res

    def canMakePaliQueries(self, s: str, queries):
        prefix = []
        prefix.append([0] * 26)
        for a in s:
            tmp = prefix[-1].copy()
            tmp[ord(a) - ord("a")] += 1
            prefix.append(tmp)
        res = []
        for left, right, k in queries:
            c = 0
            for x, y in zip(prefix[right+1], prefix[left]):
                if (x - y) % 2 == 1:
                    c += 1
            if c // 2 <= k:
                res.append(True)
            else:
                res.append(False)
        return res



a = Solution()
print(a.canMakePaliQueries(s="abcda", queries=[[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]))
print(a.canMakePaliQueries("xebyvmjqbmbs",
                           [[9, 9, 1], [6, 9, 3], [11, 11, 1], [0, 3, 3], [9, 10, 0], [10, 11, 2], [3, 3, 1],
                            [4, 11, 8], [1, 10, 3], [2, 9, 7], [11, 11, 1]]))
