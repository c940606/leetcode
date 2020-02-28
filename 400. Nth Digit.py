class Solution:
    def findNthDigit(self, n: int) -> int:
        cnt = 1
        num = 9
        while n > cnt * num:
            n -= num * cnt
            num *= 10
            cnt += 1
        div, mod = divmod(n - 1, cnt)
        start = str(10 ** (cnt - 1) + div)
        return int(start[mod])


a = Solution()
print(a.findNthDigit(100))
# print(a.findNthDigit(234))
