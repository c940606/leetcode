class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)

        def lcm(x, y):
            return x * y // gcd(x, y)

        AB = lcm(A, B)
        left = 2
        right = (40000) * (10 ** 9)
        while left < right:
            mid = left + (right - left) // 2
            cnt = mid // A + mid // B - mid // AB
            # print("cnt", cnt)
            if cnt < N:
                left = mid + 1
            else:
                right = mid
        return left % (10 ** 9 + 7)


a = Solution()
print(a.nthMagicalNumber(1000000000, 40000, 40000))
