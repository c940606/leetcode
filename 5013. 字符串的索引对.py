class Solution:
    def indexPairs(self, text: str, words):
        res = []
        for word in words:
            loc = text.find(word)
            while loc != -1:
                res.append([loc, loc + len(word) - 1])
                loc = text.find(word, loc + 1)
        return sorted(res)
a = Solution()
print(a.indexPairs(text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]))
print(a.indexPairs(text = "ababa", words = ["aba","ab"]))
print(a.indexPairs("",[]))

