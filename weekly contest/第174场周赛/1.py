from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for idx, item in enumerate(mat):
            res.append([sum(item), idx])
        res.sort(key=lambda x:(x[0], x[1]))
        return [item[1] for item in res[:k]]

a = Solution()
print(a.kWeakestRows(mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))
print(a.kWeakestRows(mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2))
print(a.kWeakestRows([], 3))