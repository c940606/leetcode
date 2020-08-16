class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        loc = {(0, 0, 0, 0, 0): -1}
        res = 0
        for i in range(len(s)):
            lookup[s[i]] += 1
            tmp = [0] * 5
            for idx, a in enumerate("aeiou"):
                if lookup[a] % 2 == 1:
                    tmp[idx] = 1
            # print(tmp)
            if tuple(tmp) in loc:
                print(i, loc[tuple(tmp)])
                res = max(res, i - loc[tuple(tmp)])
            if tuple(tmp) not in loc:
                loc[tuple(tmp)] = i
        return res


a = Solution()
print(a.findTheLongestSubstring("eleetminicoworoep"))
print(a.findTheLongestSubstring("leetcodeisgreat"))
