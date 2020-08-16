from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:
                tmp = nums[i]
                loc = nums[i] - 1
                nums[i] = nums[nums[i] - 1]
                nums[loc] = tmp
            # if nums[nums[i] - 1] == nums[i]:
            #     res.append(i + 1)
        for idx, val in enumerate(nums, 1):
            if val != idx:
                res.append(idx)
        return res


a = Solution()
print(a.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
