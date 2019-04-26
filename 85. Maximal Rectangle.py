class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])

        height = [0] * col
        res = float("-inf")
        for i in range(0, row):
            for j in range(0, col):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            left = [0] * col
            right = [0] * col
            left[0] = 0
            for i in range(1, col):
                if height[i] > height[left[i - 1]]:
                    left[i] = i
                else:
                    if height[i - 1] == 0:
                        left[i] = i
                    else:
                        left[i] = left[i - 1]
            right[-1] = col - 1
            for j in range(col - 2, -1, -1):
                if height[j] > height[right[j + 1]]:
                    right[j] = j
                else:
                    if height[j + 1] == 0:
                        right[j] = j
                    else:
                        right[j] = right[j + 1]
            print(height)
            print(left)
            print(right)

            for t in range(col):
                res = max(res, height[t] * (right[t] - left[t] + 1))
            print(res)
            print("--------")
        return res

    def maximalRectangle1(self, matrix):
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        height = [0] * col
        self.res = 0

        def monotonic_stack(height):
            stack = []
            height = [0] + height + [0]
            for k in range(col + 2):
                while stack and (height[stack[-1]] > height[k]):
                    t = stack.pop()
                    self.res = max(self.res, (k - stack[-1] - 1) * height[t])
                stack.append(k)

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            monotonic_stack(height)

        return self.res


a = Solution()
print(a.maximalRectangle([
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]))
print(a.maximalRectangle(
    [["1", "1"]]))
