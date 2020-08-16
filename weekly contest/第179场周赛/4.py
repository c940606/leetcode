from typing import List


class Solution:
    def generateTheString(self, n: int) -> str:

        if n % 2 == 1:
            tmp = ""
            tmp += "a"
            tmp += "b"
            tmp += "c" * (n - 2)
        else:
            tmp = "a" + "b" * (n - 1)
        return tmp