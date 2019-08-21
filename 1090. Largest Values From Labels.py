class Solution:
    def largestValsFromLabels(self, values, labels, num_wanted: int, use_limit: int) -> int:
        from collections import defaultdict
        sort_arr = []
        for v, l in zip(values, labels):
            sort_arr.append([v, l])
        sort_arr.sort(reverse=True)
        #print(sort_arr)
        i = 0
        n = len(sort_arr)
        lookup = defaultdict(int)
        res = 0
        while num_wanted and i < n:
            if lookup[sort_arr[i][1]] >= use_limit:
                i += 1
            else:
                res += sort_arr[i][0]
                lookup[sort_arr[i][1]] += 1
                i += 1
                num_wanted -= 1
        return res


a = Solution()
print(a.largestValsFromLabels(values=[5, 4, 3, 2, 1], labels=[1, 1, 2, 2, 3], num_wanted=3, use_limit=1))
print(a.largestValsFromLabels( values = [5,4,3,2,1], labels = [1,3,3,3,2], num_wanted = 3, use_limit = 2))
print(a.largestValsFromLabels(values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 1))
print(a.largestValsFromLabels(values = [9,8,8,7,6], labels = [0,0,0,1,1], num_wanted = 3, use_limit = 2))