class Solution:
    def maxAbsValExpr(self, arr1, arr2):

        n = len(arr1)
        res = float("-inf")
        for i in range(n):
            for j in range(n):
                res = max(res, abs(arr1[i] - arr2[j]) + abs(arr1[j] - arr2[i]) + abs(i - j))
        return res


a = Solution()
print(a.maxAbsValExpr(arr1=[1, 2, 3, 4], arr2=[-1, 4, 5, 6]))
print(a.maxAbsValExpr(
    [854632, 428107, -704467, 832706, -319640, -365224, -947863, 729070, -312850, 36528, 311684, -100859, -177471,
     -558426, -661854, 668679, -87676, -646544, 30934, -349421, 165215, -183902, 417453, 86953, 388125, -797836, 115123,
     156068, -479616, 313614]))
