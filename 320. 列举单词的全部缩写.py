from typing import List


class Solution:
    def generateAbbreviations1(self, word: str):
        res = []
        n = len(word)

        def helper(idx, tmp_str):
            if idx == n:
                res.append(tmp_str)
                return
            for j in range(idx, n ):
                num = str(j - idx) if j - idx > 0 else ""
            
                helper(j + 1, tmp_str + num + word[j])
            helper(n, tmp_str + str(n - idx))

        helper(0, "")
        return res

    def generateAbbreviations2(self, word: str) -> List[str]:
        """
        0000 word
        0001 wor1
        0011 wo2
        0101 w1r1
        :param word:
        :return:
        """
        n = len(word)
        res = []
        for i in range(2 ** n):
            tmp = ""
            one_cnt = 0
            for w, f in zip(word, bin(i)[2:].rjust(n, "0")):
                if f == "0":
                    if one_cnt > 0:
                        tmp += str(one_cnt)
                        one_cnt = 0
                    tmp += w
                else:
                    one_cnt += 1
            if one_cnt > 0:
                tmp += str(one_cnt)
            res.append(tmp)
        return res

    def generateAbbreviations(self, word: str) -> List[str]:
        n = len(word)
        res = []
        for i in range(2 ** n):
            tmp = ""
            one_cnt = 0
            for w in word:
                if i & 1 == 1:
                    one_cnt += 1
                else:
                    if one_cnt > 0:
                        tmp += str(one_cnt)
                        one_cnt = 0
                    tmp += w
                i >>= 1
            if one_cnt > 0:
                tmp += str(one_cnt)
            res.append(tmp)
        return res


a = Solution()
print(a.generateAbbreviations1(word="word"))
