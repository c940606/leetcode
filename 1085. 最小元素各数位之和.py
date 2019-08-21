class Solution:
    def sumOfDigits(self, A) -> int:
        num = min(A)
        t = 0
        for a in str(num):
            t += int(a)
        return t % 2 == 0