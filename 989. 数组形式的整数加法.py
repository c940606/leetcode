class Solution:
    def addToArrayForm(self, A: 'List[int]', K: 'int') -> 'List[int]':
        A = "".join([str(a) for a in A])
        return [int(i) for i in str(int(A) + K)]


a = Solution()
print(a.addToArrayForm(A=[9, 9, 9, 9, 9, 9, 9, 9, 9, 9], K=1))
