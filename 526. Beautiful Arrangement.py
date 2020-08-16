class Solution:
    def countArrangement(self, N: int) -> int:
        import  functools
        
        
        cur = set(range(1, N + 1))
        visited = set()
        res = 0
        @functools.lru_cache(None)
        def dfs(i, cur):
            # print(i, cur)
            # nonlocal res
            if i == N + 1:
                return 1
            res = 0
            # for num in cur - visited:
            #     if i % num == 0 or num % i == 0:
            #         visited.add(num)
            #         res += dfs(i + 1)
            #         visited.remove(num)

            for  k in range(N):
                num = 1 << k
                if not cur & num and ((k + 1) % i == 0 or i % (k + 1) == 0):
                    res += dfs(i + 1, cur | num)
            return res
                    
                    
        return dfs(1, 0)
        # return res
a = Solution()
print(a.countArrangement(16))
ans = []
for i in range(1, 16):
    ans.append(a.countArrangement(i))
print(ans)
            