class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


a = Solution()



# print(a.sortByBits([2, 3, 5, 7, 11, 13, 17, 19]))
# dkjfklaj
# asdkljfkj
pass

pass