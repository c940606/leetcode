class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        magazine_c = Counter(magazine)
        ransomNote_c = Counter(ransomNote)
        # ransomNote_c.subtract(magazine_c)
        print(ransomNote_c - magazine_c)
        return all(True if v >= 0 else False for k, v in ransomNote_c.items())

        # print(ransomNote_c)
        # for r in ransomNote:
        #     if ransomNote_c[r] > magazine_c[r]:
        #         return False
        # return True


a = Solution()
print(a.canConstruct("aac", "aab"))
