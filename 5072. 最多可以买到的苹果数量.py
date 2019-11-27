class Solution:
    def maxNumberOfApples(self, arr) -> int:
        arr.sort()
        res = 0
        for num , a in enumerate(arr, 1):
            #print(num , a)
            res += a
            if res > 5000:
                return num - 1
        return len(arr)

a = Solution()
print(a.maxNumberOfApples([100,200,150,1000]))
print(a.maxNumberOfApples([900,950,800,1000,700,800]))
print(a.maxNumberOfApples([]))
