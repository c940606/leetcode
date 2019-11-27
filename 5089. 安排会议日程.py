from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        s1 = 0
        s2 = 0

        while s1 < len(slots1) and s2 < len(slots2):
            if slots1[s1][0] >= slots2[s2][1]:
                s2 += 1
            elif slots2[s2][0] >= slots1[s1][1]:
                s1 += 1
            elif slots1[s1][1] >= slots2[s2][1]:
                tmp1 = max(slots1[s1][0], slots2[s2][0])
                if slots2[s2][1] - tmp1 >= duration:
                    return [tmp1, tmp1 + duration]
                s2 += 1
            elif slots2[s2][1] >= slots1[s1][1]:
                tmp1 = max(slots1[s1][0], slots2[s2][0])
                if slots1[s1][1] - tmp1 >= duration:
                    return [tmp1, tmp1 + duration]
                s1 += 1
        return []

a = Solution()
print(a.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8))
print(a.minAvailableDuration(slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12))