class Solution:
    def relativeSortArray(self, arr1, arr2):
        from collections import Counter
        c = Counter(arr1)
        p1 = []
        p2 = []

        for a in arr2:
            if a in c:
                p1 += [a] * c[a]

        return p1 + p2


a = Solution()
# print(a.relativeSortArray(arr1=[2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], arr2=[2, 1, 4, 3, 9, 6]))
print(a.relativeSortArray([2, 21, 43, 38, 0, 42, 33, 7, 24, 13, 12, 27, 12, 24, 5, 23, 29, 48, 30, 31],
                          [2, 42, 38, 0, 43, 21]))
