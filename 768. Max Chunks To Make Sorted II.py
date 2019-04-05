class Solution:
    def maxChunksToSorted(self, arr):
        from collections import Counter
        arr_copy = arr[:]
        arr_copy.sort()
        # print(arr_copy)
        n = len(arr)
        #left = 0
        res = 0
        arr_copy_Counter = Counter()
        arr_Counter = Counter()
        for i in range(n):
            #right = i + 1
            arr_copy_Counter[arr_copy[i]] += 1
            arr_Counter[arr[i]] += 1
            if arr_Counter == arr_copy_Counter:
                res += 1
                arr_copy_Counter.clear()
                arr_Counter.clear()
        return res

    def maxChunksToSorted1(self, arr):
        n = len(arr)
        left_max = [0]*n
        right_min = [0]*n
        left_max[0] = arr[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],arr[i])
        right_min[-1] = arr[-1]
        for i in range(n-2,-1,-1):
            right_min[i] = min(right_min[i+1],arr[i])
        res = 1
        for i in range(n-1):
            if left_max[i] <= right_min[i+1]:
                res += 1
        return res


a = Solution()
print(a.maxChunksToSorted1([5, 4, 3, 2, 1]))
print(a.maxChunksToSorted1([2, 1, 3, 4, 4]))
