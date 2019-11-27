class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        from functools import lru_cache
        @lru_cache(None)
        def firstscore(i, j):
            if i >= j: return 0
            if i + 1 == j and j < len(piles): return piles[i]
            # if (i,j) in cache:return cache[i,j]
            res = max(piles[i] + min(firstscore(i + 2, j), firstscore(i + 1, j - 1)),
                      piles[j - 1] + min(firstscore(i + 1, j - 1), firstscore(i, j - 2)))
            # cache[i,j] = res
            return res

        Alex = firstscore(0, len(piles))
        print(Alex)
        lee = sum(piles) - Alex
        return Alex > lee


a = Solution()
print(a.stoneGame([5, 3, 4, 5]))
