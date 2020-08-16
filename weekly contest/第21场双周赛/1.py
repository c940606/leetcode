class Solution:
    def maxPower(self, s: str) -> int:

        import itertools
        res = 0
        for k, item in itertools.groupby(s):
            res = max(res, len(list(item)))
        return res