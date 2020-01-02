from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        res = 0
        left = 0
        zero_num = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_num += 1
            while zero_num > 1:
                if nums[left] == 0:
                    zero_num -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
a = Solution()
print(a.findMaxConsecutiveOnes([1,0,1,1,0]))