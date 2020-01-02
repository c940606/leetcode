from typing import List
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        import math
        left = 1
        right = max(nums + [threshold]) + 1

        while left < right:
            mid = (left + right) // 2
            tmp = sum(math.ceil(num / mid) for num in nums)
            if tmp > threshold:
                left = mid + 1
            else:
                right = mid
        return left

a = Solution()
print(a.smallestDivisor(nums = [1,2,5,9], threshold = 6))
print(a.smallestDivisor(nums = [2,3,5,7,11], threshold = 11))
print(a.smallestDivisor(nums = [19], threshold = 5))