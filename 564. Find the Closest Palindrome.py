class Solution:
    def nearestPalindromic(self, n: str) -> str:

        n = int(n)
        i = 1
        while True:
            if str(n-i) == str(n-i)[::-1]:
                return str(n-i)
            if str(n+i) == str(n+i)[::-1]:
                return str(n+i)
            i += 1

a = Solution()
print(a.nearestPalindromic("1000"))
# print(12932, 99800, 12120)
print(a.nearestPalindromic("12932"))
print(a.nearestPalindromic("1986281891"))