from typing import List
import collections

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        lookup = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                lookup[i+j].append(nums[i][j])
        res = []
        for k, v in sorted(lookup.items()):
            res.extend(v[::-1])
        return res









a = Solution()
print(a.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]))
print(a.findDiagonalOrder([[1,2,3],[4],[5,6,7],[8],[9,10,11]]))
print(a.findDiagonalOrder([[1,2,3,4,5,6]]))