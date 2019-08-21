class Solution:
    def removeVowels(self, S: str) -> str:
        lookup = {"a", "e", "i", "o", "u"}
        res = ""
        for s in S:
            if s not in lookup:
                res += s
        return res
