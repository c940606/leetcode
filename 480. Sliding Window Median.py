class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        import bisect
        arr = []
        left = 0
        res = []
        for right in range(len(nums)):
            bisect.insort(arr, nums[right])
            while len(arr) > k:
                arr.pop(bisect.bisect_left(arr, nums[left]))
                left += 1
            if len(arr) == k:
                res.append((arr[k // 2] + arr[(k - 1) // 2]) / 2.0)
        return res
