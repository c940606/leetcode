class Solution:
    def canThreePartsEqualSum(self, A) :
        A_sum = sum(A)
        if A_sum % 3 != 0:
            return False
        avg = A_sum // 3
        cur = 0
        cou = 0
        for i in range(len(A)):
            cur += A[i]
            if cur == avg:
                cur = 0
                cou += 1
        if cou == 3:
            return True
        return False


a = Solution()
print(a.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(a.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(a.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))