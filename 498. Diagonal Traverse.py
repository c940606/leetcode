
from typing import List
import collections
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        lookup = collections.defaultdict(list)
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                lookup[j + i].append(matrix[i][j])
        print(lookup)

        res = []
        flag = True
        for k, v in sorted(lookup.items()):
            if flag:
                res.extend(v[::-1])
            else:
                res.extend(v)
            flag = not flag

        return res

a = Solution()
print(a.findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))


