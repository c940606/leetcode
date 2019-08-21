class Solution:
    def addNegabinary(self, arr1, arr2):
        def baseNeg2(x):
            res = []
            while x:
                res.append(x & 1)
                x = -(x >> 1)
            return res[::-1]

        def neg_shi(arr):
            ans = 0
            for idx, val in enumerate(arr[::-1]):
                ans += val * ((-2) ** idx)
            return ans
        print(neg_shi(arr1))
        print(neg_shi(arr2))
        # print(int(neg_shi(arr1)+int(neg_shi(arr2))))
        tmp = int(neg_shi(arr1) + int(neg_shi(arr2)))
        # print(baseNeg2(tmp))
        return baseNeg2(tmp)


a = Solution()
print(a.addNegabinary(arr1=[1, 1, 1, 1, 1], arr2=[1, 0, 1]))
print(a.addNegabinary([0], [1, 0]))
