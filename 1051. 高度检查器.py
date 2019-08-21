class Solution:
    def heightChecker(self, heights):
        if not heights: return 0
        res = 0
        for x, y in zip(heights, sorted(heights)):
            if x != y:
                res += 1
        return res
