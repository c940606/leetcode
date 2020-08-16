from typing import List
import collections

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float("-inf")
        for idx1, num1 in enumerate(nums):
            for idx2, num2 in enumerate(nums):
                if idx1 == idx2: continue
                res = max((num1- 1) * (num2 - 1), res)
        return res