class Solution:
    def largestSumAfterKNegations(self, A, K):

        A.sort()
        res = sum(A)
        f = []
        z = []
        for a in A:
            if a < 0:
                f.append(a)
            else:
                z.append(a)
        i = 0
        # print(f, z)
        while i < len(f) and K:
            f[i] = -f[i]
            res += 2 * f[i]
            K -= 1
            i += 1
        if K % 2 == 0:
            return res
        else:
            if f and z:
                min_num = min(f[-1], z[0])
                return res - 2 * min_num
            if f:
                min_num = f[-1]
                return res - 2 * min_num
            if z:
                min_num = z[0]
                return res - 2 * min_num


a = Solution()
# print(a.largestSumAfterKNegations(A = [4,2,3], K = 1))
# print(a.largestSumAfterKNegations(A = [3,-1,0,2], K = 3))
# print(a.largestSumAfterKNegations(A = [2,-3,-1,5,-4], K = 2))
print(a.largestSumAfterKNegations([-8, 3, -5, -3, -5, -2], 6))
