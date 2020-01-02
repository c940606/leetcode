class Solution:
    def isPerfectSquare1(self, num: int) -> bool:
        left = 1
        right = num // 2 + 1
        while left < right:
            print(left, right)
            mid = (left + right) // 2
            if mid * mid < num:
                left = mid + 1
            else:
                right = mid
        return left * left == num

    def isPerfectSquare2(self, num: int, t=1) -> bool:
        if num == 0: return True
        if num < 0: return False
        return self.isPerfectSquare(num - t, t + 2)

    def isPerfectSquare3(self, num: int) -> bool:
        t = 1
        while num > 0:
            num -= t
            t += 2
        return num == 0

    def isPerfectSquare(self, num: int) -> bool:
        x = num
        while x * x > num:
            x = (x + num// x) >> 1
        return x * x == num


a = Solution()
print(a.isPerfectSquare(15))
