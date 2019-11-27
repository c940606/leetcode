class Solution:
    def encode(self, num: int) -> str:
        import math
        if num == 0:
            return ""
        n = int(math.log2(num + 1))

        return bin(num - (2 ** n - 1))[2:].rjust(n, "0")

a = Solution()
print(a.encode(3))
print(a.encode(107))
print(a.encode(4))
# print(a.encode(1))