class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        lookup = {i: chr(i + 64) for i in range(1, 27)}
        res = ""
        while n:
            n, b = divmod(n, 26)
            if b == 0:
                b = 26
                n -= 1
            res = lookup[b] + res

        return res


a = Solution()
print(a.convertToTitle(1878784678478))
