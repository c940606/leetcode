class Solution:
    def smallestCommonElement(self, mat) -> int:
        row = len(mat)
        col = len(mat[0])
        flag = [0] * row
        while True:
            #print(flag)
            tmp = set()
            for row, f in enumerate(flag):
                if f >= col: return -1
                tmp.add(mat[row][f])
            if len(tmp) == 1:
                return mat[0][flag[0]]
            max_loc = max(tmp)
            for row, f in enumerate(flag):
                if max_loc > mat[row][f]:
                    flag[row] += 1


a = Solution()
print(a.smallestCommonElement([[1, 2, 3, 4, 5], [2, 4, 5, 8, 10], [3, 5, 7, 9, 11], [1, 3, 5, 7, 9]]))
