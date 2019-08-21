class Solution:
    def largestRectangleArea2(self, heights) -> int:
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

    def largestRectangleArea3(self, heights) -> int:
        res = float("-inf")
        n = len(heights)
        for i in range(n):
            left = i
            right = i
            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            while right < n and heights[right] >= heights[i]:
                right += 1
            # print(left,i,right,heights[i])
            res = max(res, (right - left - 1) * heights[i])
        return res

    def largestRectangleArea4(self, heights) -> int:
        if not heights:
            return 0
        n = len(heights)
        left_i = [0] * n
        right_i = [0] * n
        left_i[0] = -1
        right_i[-1] = n
        for i in range(1, n):
            tmp = i - 1
            while tmp >= 0 and heights[tmp] >= heights[i]:
                tmp = left_i[tmp]
            left_i[i] = tmp
        for i in range(n - 2, -1, -1):
            tmp = i + 1
            while tmp < n and heights[tmp] >= heights[i]:
                tmp = right_i[tmp]
            right_i[i] = tmp
        # print(left_i)
        # print(right_i)
        res = 0
        for i in range(n):
            res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
        return res

    def largestRectangleArea(self, heights) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


a = Solution()
# [0,2, 1, 5, 6, 2, 3,0]
print(a.largestRectangleArea([2, 1, 5, 6, 2, 3]))
# print(a.largestRectangleArea([1]))
