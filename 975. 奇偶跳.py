class Solution:
    def oddEvenJumps(self, A):
        """
        跳高:尽量跳最小的
        调低:尽量跳最大的
        :type A: List[int]
        :rtype: int
        """

        n = len(A)
        next_high = [0]*n
        next_low = [0]*n
        stack = []
        for val, idx in sorted([(val,idx) for idx,val in enumerate(A)]):
            while stack and stack[-1] < idx:
                next_high[stack.pop()] = idx
            stack.append(idx)
        # print(next_high)
        stack=[]
        for val, idx in sorted([(-val, idx) for idx,val in enumerate(A)]):
            while stack and stack[-1] < idx:
                next_low[stack.pop()] = idx
            stack.append(idx)
        # print(next_low)
        high = [0]*n
        low = [0]*n
        high[-1] = 1
        low[-1] = 1
        for i in range(n-2,-1,-1):
            high[i] = low[next_high[i]]
            low[i] = high[next_low[i]]
        return sum(high)



a = Solution()
print(a.oddEvenJumps([5,1,3,4,2]))
print(a.oddEvenJumps([2,3,1,1,4]))