class Solution:
    def numberOfWays(self, n: int) -> int:
        if n==0 or n==1:
            return 1
        return (4*n-2)*self.numberOfWays(n-1)//(n+1)