class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ""
        if A > B:
            while A or B:
                if A > 0:
                    res += "a"
                    A -= 1
                if A > B:
                    res += "a"
                    A -= 1
                if B > 0:
                    res += "b"
                    B -= 1
        else:
            while A or B:
                if B > 0:
                    res += "b"
                    B -= 1
                if B > A:
                    res += "b"
                    B -= 1
                if A > 0:
                    res += "a"
                    A -= 1
        return res


a = Solution()
print(a.strWithout3a3b(4, 1))
print(a.strWithout3a3b(1, 2))
print(a.strWithout3a3b(2, 2))
print(a.strWithout3a3b(3,3))
print(a.strWithout3a3b(2,5))
print(a.strWithout3a3b(4,4))
print(a.strWithout3a3b(5, 5))
