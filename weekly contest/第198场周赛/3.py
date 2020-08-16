import collections
from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        import string
        loc = collections.defaultdict(list)
        for a in string.ascii_lowercase:
            left = s.find(a)
            right = s.rfind(a)
            if left == -1: continue
            loc[a].append(left)
            loc[a].append(right)

        nxt_loc = []
        for left, right in loc.values():
            while 1:

                tmp_left, tmp_right = left, right
                for t in set(s[left:right+1]):
                    tmp_left = min(tmp_left, loc[t][0])
                    tmp_right = max(tmp_right, loc[t][1])
                if [tmp_left, tmp_right] == [left, right]: break
                left, right = tmp_left, tmp_right

            nxt_loc.append([left, right])

        sorted_loc = sorted(nxt_loc, key=lambda x: x[1] - x[0])
        cur = [0] * len(s)
        res = []
        for left, right in sorted_loc:
            flag = False
            for i in range(left, right + 1):
                if cur[i]:
                    flag = True
            if flag: continue
            for i in range(left, right + 1):
                cur[i] = 1
            res.append(s[left:right + 1])

        return res


a = Solution()
print(a.maxNumOfSubstrings(s="adefaddaccc"))
print(a.maxNumOfSubstrings("abbaccd"))
print(a.maxNumOfSubstrings("abab"))
