from typing import List


class Solution:
    def wordsTyping1(self, sentence: List[str], rows: int, cols: int) -> int:
        n = len(sentence)
        lookup = {}

        def cal(i):
            res = 0
            for j in range(i, n):
                res += len(sentence[j]) + 1
            return res

        # @lru_cache(None)
        def helper(i, j, loc):
            print(i, j, loc)
            if (j, loc) in lookup:
                return lookup[(j, loc)]
            if i == rows:
                return 0
            if loc == 0:
                l = cal(loc)
                if j + l <= cols:
                    div, mod = divmod(cols - j, l)
                    tmp5 = div + helper(i, j + l * div, 0)
                    lookup[(j, loc)] = tmp5
                    return tmp5
                else:
                    tmp6 = helper(i, j + len(sentence[loc]) + 1, loc + 1)
                    lookup[(j, loc)] = tmp6
                    return tmp6
            elif j + len(sentence[loc]) <= cols:
                if loc == n - 1:
                    tmp1 = 1 + helper(i, j + len(sentence[loc]) + 1, 0)
                    lookup[(j, loc)] = tmp1
                    return tmp1
                else:
                    if loc + 1 < n:
                        tmp2 = helper(i, j + len(sentence[loc]) + 1, loc + 1)
                        lookup[(j, loc)] = tmp2
                        return tmp2
                    else:
                        tmp3 = helper(i, j + len(sentence[loc]) + 1, 0)
                        lookup[(j, loc)] = tmp3
                        return tmp3
            else:
                tmp4 = helper(i + 1, 0, loc)
                lookup[(j, loc)] = tmp4
                return tmp4

        return helper(0, 0, 0)

    def wordsTyping2(self, sentence: List[str], rows: int, cols: int) -> int:

        ln = [len(s) for s in sentence]
        n = len(ln)
        all_len = sum(ln) + n
        idx = 0
        res = 0
        for i in range(rows):
            remain_col = cols
            while remain_col > 0 :
                if ln[idx] <= remain_col:
                    remain_col -= ln[idx]
                    if remain_col > 0: remain_col -= 1
                    idx += 1
                    if idx == n:
                        div, mod = divmod(remain_col, all_len)
                        res += div + 1
                        remain_col = mod
                        idx = 0
                else:
                    break
        return res

    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        whole = " ".join(sentence)
        whole += " "
        totalNum = 0
        for i in range(rows):
            totalNum += cols
            if whole[totalNum % len(whole)] == " ":
                totalNum += 1
            else:
                while whole[(totalNum - 1) % len(whole)] != " ":
                    totalNum -= 1
        return totalNum // len(whole)



a = Solution()
# print(a.wordsTyping(rows=2, cols=8, sentence=["hello", "world"]))
# print(a.wordsTyping(rows=3, cols=6, sentence=["a", "bcd", "e"]))
# print(a.wordsTyping(rows=4, cols=5, sentence=["I", "had", "apple", "pie"]))
print(a.wordsTyping(["try", "to", "be", "better"], 10000, 9001))
print(a.wordsTyping(["a"], 10000, 10000))
print(a.wordsTyping(
    ["qdhoisr", "icivteb", "zgspbcmqdb", "uazq", "spqsygodx", "tldsg", "qrjyhvpd", "kimynyepn", "mix", "cvexqqb"]
    , 6073
    , 1378))
print(a.wordsTyping(["sdcryxmeru","mybompgk","orqxcs","zaclfpaynj","eyvbg","nnlgawwnll","rjeuw","bicrgi","bduijxi","pqhcvredwg","mimafalo","qnkwhljp","svol","libzh","kittf","yrmnkcls","yr","zwi","eexde","jjnewbw","jctpr","tkzs","ipqzpg","jjm","t","h","sew","drbm","fwlqi","rvupujcri","l","nhiy","eu","xappthq","smhzlkci","pnyjqj","tfei","hvcjei","bk","owzvradvgz","ekjlri","mdex","itqqs","mmsqtzizwa","c","mhhfwcndp","w","szwjvnzfos","jnsgvkyetx","glngaxuh","jmwk","ca","ucee","mfqoxzmsa","agzq","cq","xv","ysvyh","iqdaui","unay","cqx","vgzbxhv","bmc","axouywtu","bqjawvcpd","hq","gmtrrfzd","tytnig","wlowagrxsf","xnxsba","us","xgdyno","pyeh","xzzhjtotsf","bvvyfzo","spdojvolrh","rxe","iwsznu","vu","vdgfukmjbj","vw","qkbnu","mresigfpho","awvibdxn","xazqiedtwf","rlxdyrtryb","uanmajo","kudcyedndg","xrml","ykziwb","a","ka","sr","rkshgye","m","pdoi","zlqjut","ftjrv","ocvctao"]
,15382
,19573))
print(a.wordsTyping(["ihfdkhq","d","fksjwvl","mp","csdbpd","zonhte","fngva","wtzjnlu","wmgmejk","axnoj"]
,7203
,3526))