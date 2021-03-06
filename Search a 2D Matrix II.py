class Solution(object):
    def searchMatrix2(self, matrix, target):
        """
        编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
        每行的元素从左到右升序排列。
        每列的元素从上到下升序排列。
        示例:
        现有矩阵 matrix 如下：
            [
              [1,   4,  7, 11, 15],
              [2,   5,  8, 12, 19],
              [3,   6,  9, 16, 22],
              [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]
            ]
        ---
        方法1:
         每行用一次二分查找
        方法2:
        左下角
        行 如果左下角的值>目标值 去掉行
        列 如果左下角的值<目标值 去掉列
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        print(row, col)
        for i in range(row):
            # print(i)
            left = 0
            right = col - 1
            while left <= right:
                mid = (left + right) // 2
                print(i, left, right)
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

    def searchMatrix1(self, matrix, target):
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])
        i = row - 1
        j = 0
        while i > -1 and j < col:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                i -= 1
            if matrix[i][j] < target:
                j += 1
        return False

    def searchMatrix(self, matrix, target):
        row = len(matrix)
        col = len(matrix[0])

        def helper(left_r, left_c, right_r, right_c):
            if left_r > right_r or left_c > right_c or \
                    left_r >= row or left_c >= col:
                return False
            if left_r == right_r and left_c == right_c:
                return matrix[left_r][left_c] == target
            mid_r = (left_r + right_r) // 2
            mid_c = (left_c + right_c) // 2
            tmp = matrix[mid_r][mid_c]
            if tmp == target:
                return True
            # 在 1 2, 3
            elif tmp > target:
                return helper(left_r, left_c, mid_r, mid_c) or \
                       helper(left_r, mid_c + 1, mid_r, right_c) or \
                       helper(mid_r + 1, left_c, right_r, mid_c)
            # 在 2, 3, 4
            else:
                return helper(left_r, mid_c + 1, mid_r, right_c) or \
                       helper(mid_r + 1, left_c, right_r, mid_c) or \
                       helper(mid_r + 1, mid_c + 1, right_r, right_c)

        return helper(0, 0, row - 1, col - 1)


a = Solution()
print(a.searchMatrix([
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
], 7))
print(
    a.searchMatrix([[1, 4, 7, 11, 15],
                    [2, 5, 8, 12, 19],
                    [3, 6, 9, 16, 22],
                    [10, 13, 14, 17, 24],
                    [18, 21, 23, 26, 30]]
                   , 20))
