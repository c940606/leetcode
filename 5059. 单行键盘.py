class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        prev = 0
        res = 0
        for w in word:
            loc = keyboard.find(w)
            res += abs(prev - loc)
            prev = loc
        return res

a = Solution()
print(a.calculateTime(keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"))
print(a.calculateTime(keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"))