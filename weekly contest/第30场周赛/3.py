from typing import List
import collections


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3: return 0

        nums.sort()
        # print(nums)
        res = float("inf")

        res = min(res, nums[-1] - nums[3], nums[-4] - nums[0],
                  nums[-3] - nums[1], nums[-2] - nums[2]

                  )
        return res

a = Solution()
print(a.minDifference([6,6,0,1,1,4,6]))
print(a.minDifference([82,81,95,75,20])) # 1


