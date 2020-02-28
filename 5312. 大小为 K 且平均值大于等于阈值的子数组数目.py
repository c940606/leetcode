from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        left = 0
        n = len(arr)
        if n < k:
            return 0
        cur = 0
        res = 0
        for right in range(n):
            while right - left + 1 > k:
                cur -= arr[left]
                left += 1
            cur += arr[right]
            if right - left + 1 == k and cur / k >= threshold:
                res += 1
        return res
a = Solution()
print(a.numOfSubarrays(arr = [1,1,1,1,1], k = 1, threshold = 0))
print(a.numOfSubarrays(arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5))
print(a.numOfSubarrays(arr = [7,7,7,7,7,7,7], k = 7, threshold = 7))
print(a.numOfSubarrays(arr = [4,4,4,4], k = 4, threshold = 1))