class Solution:
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        lookup = {}
        def helper(target,coins):
            if target == amount:
                return 1
            if target > amount:
                return 0
            # if target in lookup:
            #     return lookup[target]
            res = 0
            for idx,coin in enumerate(coins):
                res += helper(target+coin,coins[idx:])
            # lookup[target] = res
            # #             # print(lookup)
            # print(lookup)
            return res

        return helper(0,coins)


a = Solution()
print(a.change(5,[1,2,5]))