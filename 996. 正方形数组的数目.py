class Solution:
    def numSquarefulPerms(self, A: 'List[int]') -> 'int':
        from collections import Counter,defaultdict
        c = Counter(A)
        lookup = defaultdict(set)
        n = len(A)
        for i in c :
            for j in c:
                if int((i+j)**0.5) ** 2 == i +j :
                    lookup[i].add(j)
        self.res = 0
        def dfs(x,left):
            c[x] -= 1
            if left == 0:
                self.res += 1
            for y in lookup[x]:
                if c[y]:
                    dfs(y,left-1)
            c[x] += 1
        for x in c:
            dfs(x,n-1)
        return self.res

a = Solution()
print(a.numSquarefulPerms([1,17,8]))
