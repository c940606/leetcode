class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 or (n >= 3 and n % 3 != 0):
            return False
        if n == 1:
            return True
        return self.isPowerOfThree(abs(n) // 3)

a = Solution()
# print(a.isPowerOfThree(27))
# print(a.isPowerOfThree(45))
print(a.isPowerOfThree(-3))