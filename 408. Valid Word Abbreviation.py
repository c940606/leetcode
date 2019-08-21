class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            #print(i, j)
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j].isdigit():
                if abbr[j] == "0": return False
                tmp = ""
                while j < len(abbr) and abbr[j].isdigit():
                    tmp += abbr[j]
                    j += 1
                #print(tmp)
                i += int(tmp)
            else:
                return False

        return i == len(word) and j == len(abbr)


a = Solution()
print(a.validWordAbbreviation("internationalization", "i12iz4n"))
