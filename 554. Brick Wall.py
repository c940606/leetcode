from typing import List 
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        
        for i in range(len(wall)):
            cur = 0
            for j in range(len(wall[i])):
                if j == len(wall[i]) - 1: break
                cur += wall[i][j]
                lookup[cur] += 1

        return len(wall) - max(lookup.values())
    
a = Solution()
print(a.leastBricks([[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]))