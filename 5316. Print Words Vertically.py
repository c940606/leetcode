from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        from itertools import zip_longest
        res = []
        #print(s.split())
        for item in zip_longest(*s.split(), fillvalue=" "):
            print(item)
            res.append("".join(item).rstrip())
        return res
a = Solution()
print(a.printVertically("HOW ARE YOU"))