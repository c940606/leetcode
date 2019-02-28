class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        n = len(fronts)
        res = 2001
        for i in range(n):
            tmp1 = fronts[:]
            tmp2 = backs[:]
            print("qian:",tmp1,tmp2)
            tmp1[i],tmp2[i] = tmp2[i],tmp1[i]
            print(tmp1,tmp2)
            lookup = set(tmp1)
            for j in range(n):
                if tmp2[j] not in lookup:
                    res = min(res,tmp2[j])

        if res == 2001:
            return 0
        return res

a = Solution()
# print(a.flipgame([1,2,4,4,7],[1,3,4,1,3]))
print(a.flipgame([1,1],[2,1]))
