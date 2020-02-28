from typing import List
from collections import defaultdict, deque
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        max_num = max(target)
        def dfs()