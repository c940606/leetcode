class Solution:
    def connectSticks(self, sticks) -> int:
        import heapq
        n = len(sticks)
        if n == 0: return 0
        if n == 1: return 0
        res = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            tmp1 = heapq.heappop(sticks)
            tmp2 = heapq.heappop(sticks)
            res += (tmp1 + tmp2)
            heapq.heappush(sticks, tmp1 + tmp2)
        return res


a = Solution()
print(a.connectSticks([2, 4, 3]))
#
print(a.connectSticks([1, 8, 3, 5]))

print(a.connectSticks(
    [1175, 8967, 1382, 8748, 8612, 7067, 5979, 8237, 9691, 389, 5801, 7387, 8620, 6674, 1610, 7444, 6969, 970, 9463,
     7727, 5044, 1834, 3426, 3192, 9473, 2300, 3647, 6492, 3166, 3486, 454, 6077, 670, 4929, 1266, 8288, 8554, 8432,
     4724, 8553, 2442, 1776, 2704, 1276, 2933, 3376, 8259, 8548, 1563, 3884]))
