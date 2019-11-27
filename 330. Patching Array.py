from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        res = 0
        i = 0
        missing = 1
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                res += 1
                missing *= 2
        return res


a = Solution()
print(a.minPatches([1, 3], 6))
print(a.minPatches(nums=[1, 5, 10], n=20))
print(a.minPatches([1,2,6,8,9,100], 100))
print(a.minPatches([], 7))
print(a.minPatches([1,2,31,33],2147483647))
