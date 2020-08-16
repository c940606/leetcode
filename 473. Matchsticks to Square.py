from typing import List
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if len(nums) < 4: return False
        div, mod = divmod(sum(nums), 4)
        # print(div, mod)
        if mod != 0:
            return False
        nums.sort(reverse=True)
        edges = [0] * 4

        def dfs(i):
            if i == len(nums):
                if len(set(edges)) == 1:
                    return True
                return False
            for k in range(4):
                if edges[k] + nums[i] > div: continue
                edges[k] += nums[i]
                if dfs(i + 1): return True
                edges[k] -= nums[i]
            return False
        return dfs(0)

    def makesquare1(self, nums: List[int]) -> bool:
        import collections
        if len(nums) < 4: return False
        div, mod = divmod(sum(nums), 4)
        if mod != 0:
            return False

        c = collections.Counter(nums)

        def dfs(cnt, edges):
            if edges == 0:
                if cnt == 0:
                    return True
                return dfs(cnt - 1, div)
            for k in c:
                if c[k] > 0 and k <= edges:
                    c[k] -= 1
                    if dfs(cnt, edges - k):
                        return True
                    c[k] += 1
            return False

        return dfs(3, div)


a = Solution()
print(a.makesquare1(
    [6961655, 6721573, 5852338, 4455955, 7980746, 4533546, 1148969, 101844, 9721301, 4048728, 4397033, 2520627, 2522511,
     6094454, 1023140]))
