class Solution:
    def numSmallerByFrequency(self, queries, words) :
        from collections import  Counter
        #print(sorted(Counter("aaa").items())[0][1])
        q = [ sorted(Counter(item).items())[0][1] for  item in queries]
        w = [ sorted(Counter(item).items())[0][1] for  item in words]
        #print(w, q)
        res = [0] * len(q)
        for i, v in enumerate(q):
            for k in w:
                if k > v:
                    res[i] += 1
        return res

a = Solution()
print(a.numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))