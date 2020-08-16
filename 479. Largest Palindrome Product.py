class Solution:
    def largestPalindrome(self, n: int) -> int:
        max_num = 10 ** n - 1
        min_num = max_num // 10
        for num in range(max_num, min_num, -1):
            palindrom = int(str(num) + str(num)[::-1])
            for mul in range(max_num, min_num, -1):
                div, mod = divmod(palindrom, mul)
                if div > mul: break
                if mod == 0:
                    return palindrom % 1337
        return 9
a = Solution()
print(a.largestPalindrome(5))
