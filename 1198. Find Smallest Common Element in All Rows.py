from collections import Counter
from itertools import chain
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        c_mat = list(chain(*mat))
        c = Counter(c_mat)
        for k, v in sorted(c.items()):
            if v == len(mat):
                return k

