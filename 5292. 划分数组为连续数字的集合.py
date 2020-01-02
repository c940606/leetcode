from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        from collections import Counter
        c = Counter(nums)

        for ky in sorted(c.keys()):

            if c[ky] != 0:
                tmp = c[ky]

                for i in range(k):
                    if c[ky + i] < tmp: return False
                    c[ky + i] -= tmp
            # print(c)
            # break
        return True


a = Solution()
print(a.isPossibleDivide(nums=[1, 2, 3, 3, 4, 4, 5, 6], k=4))
print(a.isPossibleDivide(nums=[3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], k=3))
print(a.isPossibleDivide(nums=[1, 2, 3, 4], k=3))
