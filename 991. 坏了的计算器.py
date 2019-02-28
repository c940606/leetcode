class Solution:
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        opt = 0
        while Y > X:
            if Y % 2 == 1:
                opt += 1
                Y += 1
            else:
                opt += 1
                Y //= 2
        return opt + X - Y


if __name__ == '__main__':
    a = Solution()
    print(a.brokenCalc(2, 3))
