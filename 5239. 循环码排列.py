from typing import  List
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = [start]
        for i in range(n):
            for j in range(len(res)- 1, -1, -1):
                res.append(res[j] ^ (1 << i))
        return res

a = Solution()
print(a.circularPermutation(2 ,3))
print(a.circularPermutation(3, 2))

# 010
# 011
# 001
# 000
# 100
# 101
# 111
# 110