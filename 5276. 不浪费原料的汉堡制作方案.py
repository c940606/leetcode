from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 != 0: return []
        if tomatoSlices // 2 - cheeseSlices < 0 or 2 * cheeseSlices - tomatoSlices // 2 < 0: return []
        return [tomatoSlices // 2 - cheeseSlices, 2 * cheeseSlices - tomatoSlices // 2]
