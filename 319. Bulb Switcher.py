class Solution:
    def bulbSwitch1(self, n: int) -> int:
        bulb = [0] * n
        cnt = 1
        while cnt <= n:
            for i in range(cnt - 1, n, cnt):
                bulb[i] ^= 1
            cnt += 1
        return sum(bulb)

    def bulbSwitch(self, n: int) -> int:
        from math import sqrt
        return round(1 + (1 / 2) * (-3 + sqrt(n) + sqrt(1 + n)))

    def A000196(self, n):
        if n < 0:
            raise ValueError('only defined for non-negative n')
        if n == 0:
            return 0
        a, b = divmod(n.bit_length(), 2)
        j = 2 ** (a + b)
        while True:
            k = (j + n // j) // 2
            if k >= j:
                return j
            j = k


a = Solution()
# print(a.bulbSwitch(3))
print(a.A000196(5))
print(a.bulbSwitch(5))
# ans = []
# for i in range(1, 100):
#     t = a.bulbSwitch(i)
#     ans.append(sum(t))
#
# print(ans)
