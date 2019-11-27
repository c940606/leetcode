class Solution:
    def __init__(self):
        self.count = 0

    def movingCount(self, threshold, rows, cols):
        # write code here
        arr = [[1 for i in range(cols)] for j in range(rows)]
        self.findway(arr, 0, 0, threshold)
        return self.count

    def findway(self, arr, i, j, k):
        if i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0]):
            return
        tmpi = list(map(int, list(str(i))))
        tmpj = list(map(int, list(str(j))))
        if sum(tmpi) + sum(tmpj) > k or arr[i][j] != 1:
            return
        arr[i][j] = 0
        self.count += 1
        self.findway(arr, i + 1, j, k)
        self.findway(arr, i - 1, j, k)
        self.findway(arr, i, j + 1, k)
        self.findway(arr, i, j - 1, k)


a = Solution()
print(a.movingCount(0, 3, 3))
