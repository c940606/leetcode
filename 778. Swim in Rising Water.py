class Solution:
    def swimInWater(self, grid):
        """
        二分法
        1. 找到最大最小值
        2. dfs
        :param grid:
        :return:
        """
        left = grid[0][0]
        right = grid[0][0]
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] > right:
                    right = grid[i][j]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def helper(mid, i, j, visited):
            visited.add((i, j))
            for x, y in dirs:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col \
                        and (tmp_i, tmp_j) not in visited and grid[tmp_i][tmp_j] <= mid:
                    if tmp_i == row - 1 and tmp_j == col - 1:
                        return True
                    if helper(mid, tmp_i, tmp_j, visited):
                        return True
            return False

        while left < right:
            mid = left + (right - left) // 2
            if not helper(mid, 0, 0, set()):
                left = mid + 1
            else:
                right = mid
        return left

    def swimInWater1(self, grid):
        left = grid[0][0]
        right = grid[0][0]
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] > right:
                    right = grid[i][j]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def helper(mid, i, j, visited):
            print(i,j)
            if i == row - 1 and j == col - 1:
                return True
            for x, y in dirs:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col \
                        and (tmp_i, tmp_j) not in visited and grid[tmp_i][tmp_j] <= mid:
                    if helper(mid, tmp_i, tmp_j, visited | {(tmp_i, tmp_j)}):
                        return True
            return False

        while left < right:
            mid = left + (right - left) // 2
            if not helper(mid, 0, 0, {(0, 0)}):
                left = mid + 1
            else:
                right = mid
        return left


a = Solution()
# print(a.swimInWater([[0, 2], [1, 3]]))
# print(
#     a.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]))
# print(a.swimInWater([[3, 2], [0, 1]]))
print(a.swimInWater1([[26, 99, 80, 1, 89, 86, 54, 90, 47, 87], [9, 59, 61, 49, 14, 55, 77, 3, 83, 79],
                     [42, 22, 15, 5, 95, 38, 74, 12, 92, 71], [58, 40, 64, 62, 24, 85, 30, 6, 96, 52],
                     [10, 70, 57, 19, 44, 27, 98, 16, 25, 65], [13, 0, 76, 32, 29, 45, 28, 69, 53, 41],
                     [18, 8, 21, 67, 46, 36, 56, 50, 51, 72], [39, 78, 48, 63, 68, 91, 34, 4, 11, 31],
                     [97, 23, 60, 17, 66, 37, 43, 33, 84, 35], [75, 88, 82, 20, 7, 73, 2, 94, 93, 81]]))
