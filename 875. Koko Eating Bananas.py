class Solution:
    def minEatingSpeed(self, piles, H):
        import math
        left = math.ceil(sum(piles)/H)
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            need_time = 0
            # print(mid)
            for pile in piles:
                need_time += math.ceil(pile / mid)
            if need_time > H:
                left = mid + 1
            else:
                right = mid
        return left


a = Solution()
print(a.minEatingSpeed(piles=[3, 6, 7, 11], H=8))
print(a.minEatingSpeed( piles = [30,11,23,4,20], H = 5))
print(a.minEatingSpeed(piles=[30, 11, 23, 4, 20], H=6))
print(a.minEatingSpeed([312884470], 968709470))
