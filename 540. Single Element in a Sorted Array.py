from typing import List


class Solution:
	def singleNonDuplicate(self, nums: List[int]) -> int:
		left, right = 0, len(nums) - 1
		while left <= right:
			mid = (left + right) // 2
			if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
				tmp_right = mid - 2
				tmp_left = mid + 1
				if (tmp_right - left + 1) % 2 == 0:
					left = tmp_left
				else:
					right = tmp_right
			elif mid + 1 < len(nums) and nums[mid + 1] == nums[mid]:
				tmp_left = mid + 2
				tmp_right = mid - 1
				if (tmp_right - left + 1) % 2 == 0:
					left = tmp_left
				else:
					right = tmp_right
			else:
				return nums[mid]


a = Solution()
print(a.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(a.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
print(a.singleNonDuplicate([1, 1, 2, 2, 10, 11, 11]))
