class Solution:
    def findOcurrences(self, text: str, first: str, second: str):
        res = []
        f = 0
        s = 1
        text = text.split()
        n = len(text)
        while s < n - 1:
            if text[f] == first and text[s] == second:
                res.append(text[s + 1])
            f += 1
            s += 1
        return res


a = Solution()
print(a.findOcurrences(text="we will we will rock you", first="we", second="will"))
print(a.findOcurrences(text="alice is a good girl she is a good student", first="a", second="good"))
