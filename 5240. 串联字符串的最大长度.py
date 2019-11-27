from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        filter_arr = [set(a) for a in arr if len(set(a)) == len(a)]
        # print(filter_arr)
        self.res = 0

        # visited = set()
        def helper(tmp, arr):
            ans = []
            for a in arr:
                if len(tmp | a) == len(tmp) + len(a):
                    ans.append(a)
            return ans

        def dfs(tmp, arr, visited):

            # print(visited,tmp,  arr)
            if not arr:
                # print(tmp)
                self.res = max(len(tmp), self.res)
                return
            for a in arr:
                if len(a & visited) == 0:
                    t = a | tmp
                    visited.update(tmp)
                    dfs(t, helper(t, arr), visited)

        for a in filter_arr:
            dfs(a, helper(a, filter_arr), set())
        return self.res


a = Solution()
print(a.maxLength(arr=["un", "iq", "ue"]))
print(a.maxLength(arr=["cha", "r", "act", "ers"]))
print(a.maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]))
print(a.maxLength(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]))
print(a.maxLength(
    ["ogud", "ejipchfydrgl", "b", "kjxmzhnuoisgqvawel", "mizlcgdqebwuotfnk", "bjvkrgeozidytquchlw", "tzjqwumkirxeal",
     "x", "rkpuabmo", "mxndpcqzua"]))
