from typing import List
from collections import defaultdict, deque

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        lookup = defaultdict(list)
        digits.sort(reverse=True)
        res = []
        for d in digits:
            lookup[d % 3].append(d)
       # print(lookup)
        res.extend(lookup[0])
        cur = len(lookup[1]) * 1 + len(lookup[2]) * 2
        if cur % 3 == 1:
            if lookup[1]:
                lookup[1].pop()
            else:
                lookup[2].pop()
                lookup[2].pop()
        if cur % 3 == 2:
            if  lookup[2]:
                lookup[2].pop()
            else:
                lookup[1].pop()
                lookup[1].pop()
        res.extend(lookup[1])
        res.extend(lookup[2])

        if not res:
            return ""
        #print(res)
        res.sort(reverse=True)
        if res[0] == 0: return "0"
        return "".join(map(str, res))

a = Solution()
print(a.largestMultipleOfThree([8,6,7,1,0]))
print(a.largestMultipleOfThree(digits = [8,1,9]))
print(a.largestMultipleOfThree([1,1,1]))
print(a.largestMultipleOfThree([1,1,1,2]))
print(a.largestMultipleOfThree([2,2,1,1,1]))
print(a.largestMultipleOfThree([5,8]))