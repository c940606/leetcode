from typing import List
import collections

class Solution:
    def arrangeWords(self, text: str) -> str:
        if not text: return ""
        
        res = " ".join(sorted(text.split(), key=len))
        return res[0].upper() + res[1:].lower()
        

    
a = Solution()
print(a.arrangeWords("Leetcode is cool"))
print(a.arrangeWords("Keep calm and code on"))