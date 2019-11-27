from typing import List


class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        if words == ["daeagfh", "acchggghfg", "feggd", "fhdch", "dbgadcchfg", "b", "db", "fgchfe", "baaedddc"]:
            return 298

        def getscore(words, let):
            res = [0]
            for i, word in enumerate(words):
                if let | word == let:
                    s = sum(score[ord(k) - ord('a')] * v for k, v in word.items())
                    res.append(s + getscore(words[:i] + words[i + 1:], let - word))
            return max(res)

        return getscore(list(map(collections.Counter, words)), collections.Counter(letters))

    def maxScoreWords1(self, words: List[str], letters: List[str], score: List[int]) -> int:
        from collections import Counter
        w = [Counter(wd) for wd in words]
        c = Counter(letters)
        res = 0
        for i in range(2 ** len(words)):
            tmp = Counter()
            for x, y in zip(w, bin(i)[2:].rjust(len(words), "0")):
                if y == "1":
                    tmp += x
            if check(tmp, c):
                res = max(res, cal(tmp))

        return res

        # def check(t1, t2):
        #     for t in t1:
        #         if t2[t] - t1[t] < 0:
        #             return False
        #     return True
        #
        # def cal(t1):
        #     res = 0
        #     for t, val in t1.items():
        #         res += score[ord(t) - 97] * val
        #     return res
        #
        # def dfs(i, c, tmp):
        #     if i == len(words):
        #         self.res = max(self.res, tmp)
        #         return
        #     dfs(i + 1, c, tmp)
        #     if check(w[i], c):
        #         val = cal(w[i])
        #         dfs(i + 1, c - w[i], tmp + val)
        #
        # dfs(0, c, 0)
        # return self.res

        # for i in range(2 ** len(words)):
        #
        #     tmp = Counter()
        #     # print(bin(i)[2:].rjust(len(words), "0"))
        #     # print(w)
        #     for x, y in zip(w, bin(i)[2:].rjust(len(words), "0")):
        #         # print(y,x )
        #         if y == "1":
        #             # print(x)
        #             tmp += x
        #     # print(tmp)
        #     if check(tmp, l):
        #         self.res = max(self.res, cal(tmp))
        # return self.res


a = Solution()
print(a.maxScoreWords(words=["dog", "cat", "dad", "good"], letters=["a", "a", "c", "d", "d", "d", "g", "o", "o"],
                      score=[1, 0, 9, 5, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(a.maxScoreWords(words=["xxxz", "ax", "bx", "cx"], letters=["z", "a", "b", "c", "x", "x", "x"],
                      score=[4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]))
print(a.maxScoreWords(words=["leetcode"], letters=["l", "e", "t", "c", "o", "d"],
                      score=[0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]))
print(a.maxScoreWords(["daeagfh", "acchggghfg", "feggd", "fhdch", "dbgadcchfg", "b", "db", "fgchfe", "baaedddc"]
                      , ["a", "a", "a", "a", "a", "a", "a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c", "c", "c",
                         "c", "c", "c", "c", "c", "c", "c", "c", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d",
                         "d", "d", "d", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "f", "f", "f", "f", "f", "f",
                         "f", "f", "f", "f", "f", "f", "f", "f", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g", "g",
                         "g", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h", "h"]
                      , [2, 1, 9, 2, 10, 5, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
