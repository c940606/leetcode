from typing import List


class Solution:
    def numTeams1(self, rating: List[int]) -> int:

        if len(rating) <= 2: return 0
        n = len(rating)

        def helper(nums):
            res = 0
            for i in range(n):
                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        if nums[i] < nums[j] < nums[k]:
                            res += 1
            return res

        return helper(rating) + helper(rating[::-1])

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0
        for i in range(1, n - 1):
            less, great = [0] * 2, [0] * 2
            for j in range(n):
                if rating[i] > rating[j]:
                    less[j > i] += 1
                if rating[i] < rating[j]:
                    great[j > i] += 1
            res += less[0] * great[1] + less[1] * great[0]
        return res


a = Solution()
print(a.numTeams(rating=[2, 5, 3, 4, 1]))
