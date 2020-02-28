class Solution:
    def validWordAbbreviation1(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        m = len(word)
        n = len(abbr)
        while i < m and j < n:
            if abbr[j].isdigit():
                if abbr[j] == "0": return False
                num = 0
                while j < n and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == m and j == n

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        m = len(word)
        n = abbr
        p = 0
        num = 0
        for a in abbr:
            if a.isdigit():
                if num == 0 and a == "0":
                    return False
                num = num * 10 + int(a)
            else:
                p += num
                #print(p)
                if p > m or word[p] != a:
                    #print(2)
                    return False
                num = 0
                p += 1

        return p + num == m


a = Solution()
print(a.validWordAbbreviation("internationalization", "i12iz4n"))
