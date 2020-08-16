from typing import List
import collections

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        loc = 0
        res = []
        stack = []
        for i in range(1, n + 1):

            res.append("Push")
            stack.append(i)
            # print(stack)

            if  stack and stack[-1] != target[loc]:
                res.append("Pop")
                stack.pop()
            if stack and stack[-1] == target[loc]:
                loc += 1
                if loc == len(target):
                    break
        return res







a = Solution()
print(a.buildArray(target=[2, 3, 4], n=4))
print(a.buildArray(target = [1,2], n = 4))
print(a.buildArray(target = [1,2,3], n = 3))
print(a.buildArray(target = [1,3], n = 3))
print(a.buildArray(target=[1, 2, 3, 5], n = 5))
print(a.buildArray(target=[1], n = 1))