class Solution:
    def countCharacters(self, words, chars: str) -> int:
        from collections import Counter
        c = Counter(chars)
        res = 0
        for word in words:
            w = Counter(word)
            if all(map(lambda x : c[x] >= w[x], word)):
                # print(c)
                # c -= w
                # print(c)
                res += len(word)
        return res

a = Solution()
print(a.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
print(a.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))
print(a.countCharacters())