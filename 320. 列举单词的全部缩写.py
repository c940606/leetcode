class Solution:
    def generateAbbreviations(self, word: str):
        res = []
        n = len(word)

        def helper(idx, tmp_str):
            if idx == n:
                res.append(tmp_str)
                return
            for j in range(idx, n):
                num = str(j - idx) if j - idx > 0 else ""
                helper(j + 1, tmp_str + num + word[j])
            helper(n, tmp_str + str(n - idx))

        helper(0, "")
        return res


a = Solution()
print(a.generateAbbreviations(word="word"))
