class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        res = 6 ** n
        for r in rollMax:
            