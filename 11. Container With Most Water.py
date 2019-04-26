class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0
        right = n - 1
        res = float("-inf")
        while left < right:
            res = max(res, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1
            else:
                left += 1
                right -= 1
        return res


a = Solution()
print(a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
