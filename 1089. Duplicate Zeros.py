class Solution:
    def duplicateZeros1(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        res = []
        n = len(arr)
        for a in arr:
            if a == 0:
                res.append(0)
                res.append(0)
            else:
                res.append(a)
        arr[:] = res[:n]
        print(arr)

    def duplicateZeros(self, arr) -> None:
        n = len(arr)
        j = 0
        for i in range(n):
            if arr[i] == 0:
                j += 1
            j += 1
        print(j)
        for i in range(n - 1, -1, -1):
            pass


a = Solution()
print(a.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
