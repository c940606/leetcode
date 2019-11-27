from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = len(citations)
        while left < right:
            # print(left, right)
            mid = left + (right - left) // 2
            if citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid
        if left < n and citations[left] >= n - left: return n - left
        return 0


a = Solution()
print(a.hIndex([0, 1, 3, 5, 6]))
