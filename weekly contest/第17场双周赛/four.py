class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:

        n = len(text)
        res = set()
        s =  text
        for i in range(n):
            for j in range(i, n):
                # print(i, j)
                tmp = s[i:j + 1]

                if s[j+1:].startswith(tmp):
                    res.add(tmp*2)

        #print(res)
        return len(res)

a = Solution()
print(a.distinctEchoSubstrings(text = "abcabcabc"))
print(a.distinctEchoSubstrings(text = "leetcodeleetcode"))
