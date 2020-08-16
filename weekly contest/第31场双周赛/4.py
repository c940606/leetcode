from typing import List
import collections


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = 0
        while target:
            tmp = min(target)
            res += tmp
            nxt_target = []
            for t in target:
                if t - tmp == 0: continue
                nxt_target.append(t - tmp)
            target =  nxt_target
        return res