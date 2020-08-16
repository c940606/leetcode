from typing import List
import collections


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        import  functools

        lookup = collections.defaultdict(dict)
        num = {0: nums1, 1:nums2}
        for idx, tmp in enumerate(nums1):
            lookup[0][tmp] = idx
        for idx, tmp in enumerate(nums2):
            lookup[1][tmp] = idx
        # print(lookup, num)
        @functools.lru_cache(None)
        def dfs(flag, loc):
            # print(flag, loc)
            if loc == len(num[flag]):
                return 0
            val = num[flag][loc]
            res = val + dfs(flag, loc + 1)
            if val in lookup[1-flag]:
                res = max(res, val + dfs(1 - flag, lookup[1-flag][val] + 1))
            return res

        return max(dfs(1, 0), dfs(0, 0))
    
a = Solution()
print(a.maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]))
print(a.maxSum(nums1 = [1,3,5,7,9], nums2 = [3,5,100]))
