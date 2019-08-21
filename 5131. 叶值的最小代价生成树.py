class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        self.res = float("inf")

        def helper(arr, tmp):
            if not arr:
                self.res = min(tmp ,self.res)
                return
            for i in range(len(arr) - 1):
                helper(arr[:i] + arr[i+2:], tmp + )