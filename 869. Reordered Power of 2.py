class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        from collections import Counter
        c = Counter(str(N))
        return any(c == Counter(str(1 << i)) for i in range(32))


a = Solution()
print(a.reorderedPowerOf2(16))
