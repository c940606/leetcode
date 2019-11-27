class Solution:
    def minCostToMoveChips(self, chips) -> int:
        from collections import Counter
        c = Counter(chips)
        print(c)
        k = list(c.keys())
        res = float("inf")
        for i in range(len(k)):
            tmp = 0
            for j in range(len(k)):
                dis = abs(k[i] - k[j]) % 2
                tmp += dis * c[k[j]]
            res = min(res, tmp)
        return res

a = Solution()
print(a.minCostToMoveChips([3,3,1,2,2]))
# print(a.minCostToMoveChips([1,2,3]))
# print(a.minCostToMoveChips(chips = [2,2,2,3,3]))
# print(a.minCostToMoveChips([1]))


