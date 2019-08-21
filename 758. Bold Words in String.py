class Solution:
    def boldWords(self, words, S: str) -> str:
        n = len(S)
        s = [False] * n

        for word in words:
            left = 0
            while True:
                idx = S.find(word, left)
                if idx == -1:
                    break
                else:
                    for i in range(len(word)):
                        s[idx + i] = True
                    left = idx + 1
        res = ""
        i = 0
        while i < n:
            while i < n and s[i] == False:
                res += S[i]
                i += 1
            if i == n:
                break
            res += "<b>"
            while i < n and s[i] == True:
                res += S[i]
                i += 1
            res += "</b>"
        return res


a = Solution()
print(a.boldWords(words=["ab", "bc"], S="aabcd"))
