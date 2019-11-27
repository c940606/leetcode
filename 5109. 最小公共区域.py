from pprint import pprint
from typing import List


class Solution:
    def findSmallestRegion1(self, regions: List[List[str]], region1: str, region2: str) -> str:
        f = {}
        tree = f
        loc = {}
        for item in regions:
            if item[0] in loc:
                tree = loc[item[0]]
            else:
                tree.setdefault(item[0], {})
                tree = tree[item[0]]
            for tmp in item[1:]:
                if tmp not in tree:
                    tree[tmp] = {}
                    loc[tmp] = tree[tmp]
        pprint(f)

        def dfs(r1, r2, ans, f):
            if not f:
                return
            for item in f:
                if r1 in f[item] or r2 in f[item]:
                    return item
            res = []
            for tmp in f[ans]:
                pass

    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        f = {}
        for region in regions:
            for re in region[1:]:
                f[re] = region[0]

        # print(f)

        def find_ans(r):
            res = [r]
            while r in f:
                res.append(f[r])
                r = f[r]
            return res

        tmp1 = find_ans(region1)
        tmp2 = find_ans(region2)
        res = None

        while tmp1 and tmp2 and tmp1[-1] == tmp2[-1]:
            res = tmp1.pop()
            tmp2.pop()
        return res


a = Solution()
print(a.findSmallestRegion(regions=[["Earth", "North America", "South America"],
                                    ["North America", "United States", "Canada"],
                                    ["United States", "New York", "Boston"],
                                    ["Canada", "Ontario", "Quebec"],
                                    ["South America", "Brazil"]],
                           region1="Quebec",
                           region2="New York"))
print(a.findSmallestRegion([["Earth", "North America", "South America"],["North America", "United States", "Canada"],["United States", "New York", "Boston"],["Canada", "Ontario", "Quebec"],["South America", "Brazil"]]
,"Canada"
,"Quebec"))
