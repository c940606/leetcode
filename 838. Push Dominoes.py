class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        dominoes = dominoes
        n = len(dominoes)
        right = [float("inf")] * n
        left = [float("inf")] * n
        i = 0
        while i < n:
            if dominoes[i] == "R":
                right[i] = 1
                while i + 1 < n and dominoes[i + 1] != "R":
                    right[i + 1] = right[i] + 1
                    i += 1
                    if i < n and dominoes[i] == "L":
                        break
            i += 1
        i = n - 1
        while i >= 0:
            if dominoes[i] == "L":
                left[i] = 1
                while i - 1>=0 and dominoes[i-1] != "L":
                    left[i-1] = left[i] + 1
                    i -= 1
                    if i >= 0 and dominoes[i] == "R":
                        break
            i -= 1
        res = ""
        print(right)
        print(left)
        for x,y in zip(right,left):
            if x - y < 0:
                res += "R"
            elif x - y > 0:
                res += "L"
            else:
                res += "."
        return res

a = Solution()
print(a.pushDominoes(".L.R...LR..L.."))
print(a.pushDominoes("RR.L"))
