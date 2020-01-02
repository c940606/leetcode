from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:

        return sorted(range(1, n + 1), key=lambda x:str(x))

a = Solution()
print(a.lexicalOrder(13))