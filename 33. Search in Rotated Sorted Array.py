from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] < nums[right]:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[left] <= nums[mid]:
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < nums[right]:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
        return -1

if __name__ == '__main__':

    a = Solution()
    print(a.search(nums = [4,5,6,7,0,1,2], target = 3))