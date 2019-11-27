from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        lookup = {0: -1}
        cur = 0
        res = 0
        for idx, val in enumerate(nums):
            cur += val
            if cur - k in lookup:
                res = max(res, idx - lookup[cur - k])
            if cur not in lookup:
                lookup[cur] = idx
        # print(lookup)
        return res


a = Solution()
print(a.maxSubArrayLen(nums=[1, -1, 5, -2, 3], k=3))
print(a.maxSubArrayLen(nums=[-2, -1, 2, 1], k=1))
