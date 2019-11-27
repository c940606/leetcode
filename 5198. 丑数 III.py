class Solution:
    # def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
    # ugly = [1]
    # ia = ib = ic = 0
    # while len(ugly) < n:
    #     while ugly[ia] * a <= ugly[-1]: ia += 1
    #     while ugly[ib] * b <= ugly[-1]: ib += 1
    #     while ugly[ic] * c <= ugly[-1]: ic += 1
    #     ugly.append(min(ugly[ia] * a, ugly[ib] * b, ugly[ic] * c))
    # print(ugly)
    # return ugly[-1]

    def nthUglyNumber(self, k: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            return x if y == 0 else gcd(y, x % y)

        def lcm(x, y):
            return x * y // gcd(x, y)

        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(a, bc)
        left, right = 1, 2 * (10 ** 9)
        while left < right:
            mid = left + (right - left) // 2
            cnt = mid // a + mid // b + mid // c - mid // ab - mid // bc - mid // ac + mid // abc
            if cnt < k:
                left = mid + 1
            else:
                right = mid
        return left


a = Solution()
print(a.nthUglyNumber(1000000000, a=2, b=217983653, c=336916467))
print(a.nthUglyNumber(k=5, a=2, b=11, c=13))
