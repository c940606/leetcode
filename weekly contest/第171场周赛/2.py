class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a_bin = bin(a)[2:].rjust(32, "0")
        b_bin = bin(b)[2:].rjust(32, "0")
        c_bin = bin(c)[2:].rjust(32, "0")
        print(a_bin, b_bin, c_bin)
        res = 0
        for x, y, z in zip(a_bin, b_bin, c_bin):
            if int(x) | int(y) == int(z):continue
            if int(z) == 1:
                # if int(x) == 0 and
                res += 1
            if int(z) == 0:
                if int(x) == 1 and int(y) == 1:
                    res += 2
                else:
                    res += 1
        return res

a = Solution()
# print(a.minFlips(a = 2, b = 6, c = 5))
# print(a.minFlips(a = 4, b = 2, c = 7))
# print(a.minFlips(a = 1, b = 2, c = 3))
# print(a.minFlips(8, 3, 5)) # 3
print(a.minFlips(6,783,863))