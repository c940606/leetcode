class Solution(object):
    def isPowerOfTwo2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.isPowerOfTwo(n // 2)
        return False

    def isPowerOfTwo1(self, n):
        return n > 0 and n & (n - 1) == 0

    def isPowerOfTwo(self, n):
        return n > 0 and bin(n).count("1") == 1


a = Solution()
print(a.isPowerOfTwo1(1024))
