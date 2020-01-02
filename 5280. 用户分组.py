class Solution:
    def groupThePeople(self, groupSizes):
        from collections import defaultdict
        lookup = defaultdict(list)
        for idx, v in enumerate(groupSizes):
            lookup[v].append(idx)
        #print(lookup)
        res = []
        for k in lookup:
            for i in range(0, len(lookup[k]), k):
                res.append(lookup[k][i:i + k])
        return res


a = Solution()
print(a.groupThePeople([3, 3, 3, 3, 3, 1, 3]))
print(a.groupThePeople([2,1,3,3,3,2]))
