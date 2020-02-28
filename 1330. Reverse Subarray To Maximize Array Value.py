from typing import List
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:

        _sum = 0
        n = len(nums)
        for i in range(1, n):
            _sum += abs(nums[i] - nums[i - 1])
        print(_sum)
        res = _sum
        for i in range(n):
            if i >= 1:
                res = max(res, _sum + 2 * nums[i - 1] - 2 * nums[i], _sum - 2 * nums[i - 1] + 2 * nums[i])
            if i < n - 1:
                res = max(res, _sum + 2 * nums[i] - 2 * nums[i + 1], _sum - 2 * nums[i] + 2 * nums[i + 1])
        return res

a = Solution()
print(a.maxValueAfterReverse([2,3,1,5,4]))

