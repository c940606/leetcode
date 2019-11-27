class Solution:
    def minimumAbsDifference(self, arr) :
        from collections import defaultdict
        res = defaultdict(list)
        arr.sort()
        for i in range(1, len(arr)):
            res[arr[i] - arr[i - 1]].append([arr[i - 1], arr[i ]])

        min_num = min(res.keys())
        return res[min_num]

a = Solution()
print(a.minimumAbsDifference([4,2,1,3]))
print(a.minimumAbsDifference([1,3,6,10,15]))
print(a.minimumAbsDifference(arr = [3,8,-10,23,19,-4,-14,27]))
