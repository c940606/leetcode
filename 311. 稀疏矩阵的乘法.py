class Solution:
    def multiply(self, A, B):

        res = [[0] * len(B[0]) for _ in range(len(A))]
        #print(res)

        def helper(a, b):
            ans = 0
            for i, j in zip(a, b):
                ans += i * j
            return ans

        for idxa, a in enumerate(A):
            for idxb, b in enumerate(zip(*B)):
                # print(idxa,idxb,a,b)
                res[idxa][idxb] = helper(a, b)
        return res


a = Solution()
print(a.multiply([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]]))
print(a.multiply([[1, -5]], [[12], [-1]]))
