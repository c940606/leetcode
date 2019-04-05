class Solution:
    def largestRectangleArea(self, heights) -> int:
        res = 0
        n = len(heights)
        # if n == 1:return heights[0]
        for i in range(n):
            if i < n - 1 and heights[i] <= heights[i + 1]:
                continue
            minH = heights[i]
            for j in range(i, -1, -1):
                minH = min(heights[j], minH)
                area = minH * (i - j + 1)
                res = max(area, res)
        return res

    def largestRectangleArea1(self, heights) -> int:
        stack = []
        heights = [0] + heights + [0]
        n = len(heights)
        res = 0
        for i in range(n):
            # print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                cur = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[cur])
            stack.append(i)
        return res


a = Solution()
print(a.largestRectangleArea1([2, 1, 5, 6, 2, 3]))
print(a.largestRectangleArea([1]))
