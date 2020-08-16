from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        from collections import deque
        queue = deque()
        for i in range(len(nums)):
            nums[i] += queue[0] if queue else 0
            while queue and queue[-1] < nums[i]:
                queue.pop()
            if nums[i] > 0:
                queue.append(nums[i])
            if i >= k and queue and queue[0] == nums[i - k]:
                queue.popleft()
        return max(nums)


a = Solution()
print(a.constrainedSubsetSum(nums=[10, 2, -10, 5, 20], k=2))
print(a.constrainedSubsetSum(nums=[-1, -2, -3], k=1))
print(a.constrainedSubsetSum(nums=[10, -2, -10, -5, 20], k=2))
print(a.constrainedSubsetSum([-8269, 3217, -4023, -4138, -683, 6455, -3621, 9242, 4015, -3790], 1))  # 16091
