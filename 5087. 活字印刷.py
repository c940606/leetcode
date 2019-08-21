class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from itertools import permutations
        res = set()
        n = len(tiles)
        for i in range(1, n + 1):
            for tmp in permutations(tiles, i):
                res.add(tmp)
        return len(res)


a = Solution()
print(a.numTilePossibilities("AAB"))
print(a.numTilePossibilities("AAABBCR"))
