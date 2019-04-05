class Solution:
    def advantageCount(self, A, B) :
        if not A:
            return []
        n = len(B)
        A.sort()
        con_B = []
        res = [None] * n
        for idx,val in enumerate(B):
            con_B.append((val,idx))
        con_B.sort()
        i = 0
        yongguo = set()
        for val,idx in con_B:
            while i < n:
                if A[i] > val:
                    res[idx] = A[i]
                    yongguo.add(i)
                    i += 1
                    break
                i += 1
        #print(res)
        #print(set(range(n))-yongguo)
        res_set = set()
        for idx,val in enumerate(res):
            if val == None:
                res_set.add(idx)
        for x,y in zip(res_set,set(range(n))-yongguo):
            res[x] = A[y]
        return res
a = Solution()
print(a.advantageCount(A = [2,7,11,15], B = [1,10,4,11]))
print(a.advantageCount(A = [12,24,8,32], B = [13,25,32,11]))
