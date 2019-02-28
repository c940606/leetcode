class Solution:
    def multiply(self, A):
        # write code here
        front_mul = [1]
        last_mul = [1]
        for a in A[:-1]:
            front_mul.append(front_mul[-1]*a)
        for b in A[:0:-1]:
            last_mul.append(last_mul[-1]*b)
        last_mul = last_mul[::-1]
        return [a*b for a,b in zip(front_mul,last_mul)]

a = Solution()
print(a.multiply([1,2,3,4,5]))