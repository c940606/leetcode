class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        if M == 2:
            if Y % 100 == 0:
                if Y % 400 == 0:
                    return 29
                else:
                    return 28
            else:

                if Y % 4 == 0:
                    return 29
                else:
                    return 28
        lookup = {
            1: 31,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        return lookup[M]

a = Solution()
print(a.numberOfDays(1900, 2))
