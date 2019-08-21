class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        res = 0
        depth_weight = []

        def helper(nl, depth, depth_weight):
            if depth >= len(depth_weight): depth_weight = depth_weight + [0]
            if nl.isInteger():
                depth_weight[depth] += nl.getInteger()
            else:
                for t in nl.getList():
                    helper(t, depth + 1, depth_weight)

        for a in nestedList:
            helper(a, 0, depth_weight)

        for i in range(len(depth_weight) - 1, -1, -1):
            res += depth_weight[i] + (len(depth_weight) - i)
        return res

a = Solution()
print(a.depthSumInverse())
