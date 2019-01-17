class Solution(object):
    def isIdealPermutation(self, A):
        """
        全局转置等于局部转置
        局部转置一定是全局转置,换句话说成立情况就是所有都是局部转置
        不会出现A[i] > A{i+2]
        :type A: List[int]
        :rtype: bool
        """
        # max_num = 0
        # n = len(A)
        # for idx in  range(n-2):
        #     max_num = max(max_num, A[idx])
        #     if max_num > A[idx+2]:
        #         return False
        # return True

        for i in range(0, len(A)):
            if abs(i - A[i]) > 1:
                return False
        return True

