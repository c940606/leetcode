from typing import List


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        import bisect
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        for left in range(col):
            _sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]

                #print(_sum)
                arr = [0]
                cur = 0
                for tmp in _sum:
                    cur += tmp
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):res = max(cur - arr[loc], res)


                    #print(res, _sum, arr)
                    bisect.insort(arr, cur)
        return res


a = Solution()
print(a.maxSumSubmatrix(matrix=[[1, 0, 1], [0, -2, 3]], k=2))
print(a.maxSumSubmatrix([[2, 2, -1]], 0))
print(a.maxSumSubmatrix([[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]], 10))
print(a.maxSumSubmatrix([[-9, -6, -1, -7, -6, -5, -4, -7, -6, 0], [-4, -9, -4, -7, -7, -4, -4, -6, -6, -6],
                         [-2, -2, -6, -7, -7, 0, -1, -1, -8, -2], [-5, -3, -1, -6, -1, -1, -6, -3, -4, -8],
                         [-4, -1, 0, -8, 0, -9, -8, -7, -2, -4], [0, -3, -1, -7, -2, -5, -5, -5, -8, -7],
                         [-2, 0, -8, -2, -9, -2, 0, 0, -9, -6], [-3, -4, -3, -7, -2, -1, -9, -5, -7, -2],
                         [-8, -3, -2, -8, -9, 0, -7, -8, -9, -3], [-7, -4, -3, -3, -3, -1, 0, -1, -8, -2]], -321))
