from typing import List
from collections import defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        if not votes: return ""
        people = len(votes[0])

        lookup = defaultdict(lambda :[0]*people)

        for vote in votes:
            for idx, val in enumerate(vote):
                lookup[val][idx] -= 1

        cons = []
        for k, v in lookup.items():
            tmp = v + [k]
            cons.append(tmp)
        cons.sort()
        res = []
        for c in cons:
            res.append(c[-1])
        return "".join(res)

a = Solution()
print(a.rankTeams(["ABC","ACB","ABC","ACB","ACB"]))
print(a.rankTeams(votes = ["WXYZ","XYZW"]))
print(a.rankTeams(votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))
print(a.rankTeams(votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]))
print(a.rankTeams(votes = ["M","M","M","M"]))