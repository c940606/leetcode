class Solution:
    def trap(self, height):
        stack = []
        res = 0

        for i in range(len(height)):
            print(stack)
            while stack and height[stack[-1]] < height[i]:

                cur = stack.pop()
                if not stack: break
                res += (min(height[stack[-1]], height[i]) - height[cur]) * (i - stack[-1] - 1)
            stack.append(i)
        return res

    def trap1(self, height):
        n = len(height)
        dp_left = [0] * n
        dp_left[0] = height[0]
        for i in range(1, n):
            dp_left[i] = max(dp_left[i - 1], height[i])
        tmp = 0
        res = 0
        for i in range(n - 1, -1, -1):
            dp_left[i] = min(dp_left[i], tmp)
            tmp = max(tmp, height[i])
            if dp_left[i] > height[i]:
                res += dp_left[i] - height[i]
        return res


a = Solution()
# print(a.trap1([0, 1, 0, 2]))
print(a.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
