from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        M = 10 ** 9 + 7
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        # res = 0
        l = []
        n = len(prefix)
        for i in range(1, n):
            for j in range(i):
                tmp = prefix[i] - prefix[j]
                l.append(tmp)

        return sum(sorted(l)[left-1:right]) % M
a = Solution()
print(a.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 5))
print(a.rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 10))