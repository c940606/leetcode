import collections


class Solution:
    def countTriplets(self, A: 'List[int]') -> 'int':

        N = len(A)
        ans = 0
        count = collections.Counter()

        for i in range(N):
            for j in range(N):
                count[A[i]&A[j]] += 1

        for k in range(N):
            for v in count:
                if A[k] & v == 0:
                    ans += count[v]
        return ans

    def countTriplets1(self, A: 'List[int]') -> 'int':
        res = 0
        A.sort()
        n = len(A)
        for i in range(n):
            for j in range(i,n):
                tmp = A[i] & A[j]
                for k in range(j,n):
                    re = tmp & A[k]
                    if re == 0 :
                        if i==j and j ==k:
                             res += 1
                        elif i ==j or i == k or j == k:
                            res += 3
                        else:
                            res += 6
        return res
a = Solution()
print(a.countTriplets1([2,1,3]))