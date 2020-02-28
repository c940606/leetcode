from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) <= 2: return max(nums)
        first = float("-inf")
        second = float("-inf")
        three = float("-inf")
        for num in nums:
            if num > first:
                first, second, three = num, first, second
            elif num > second:
                second, three = num, second
            elif num > three:
                three = num
            # print(first, second, three)

        return three


a = Solution()
print(a.thirdMax([1, 2,2]))
# print(a.thirdMax([3, 3, 1]))
# print(a.thirdMax([3, 2, 1]))
# print(a.thirdMax([2, 2, 3, 1]))
# print(a.thirdMax([1, 2]))
