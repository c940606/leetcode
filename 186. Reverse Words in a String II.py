class Solution:
    def reverseWords(self, str) -> None:
        """
        Do not return anything, modify str in-place instead.
        """

        str[:] = list(" ".join("".join(str).split()[::-1]))
        print(str)


a = Solution()
print(a.reverseWords(["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]))
