class Solution:
    def validWordSquare(self, words):
        from itertools import zip_longest
        for idx, word in enumerate(zip_longest(*words)):
            if words[idx] != "".join(a for a in word if a != None):
                return False
        return True


a = Solution()
print(a.validWordSquare([
    "abcd",
    "bnrt",
    "crmy",
    "dtye"
]))
print(a.validWordSquare([
    "abcd",
    "bnrt",
    "crm",
    "dt"
]))
