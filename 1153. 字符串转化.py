class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2: return True
        lookup = {}
        for x, y in zip(str1, str2):
            if x not in lookup:
                lookup[x] = y
            else:
                if lookup[x] != y:
                    return False
        return len(set(str2)) < 26
