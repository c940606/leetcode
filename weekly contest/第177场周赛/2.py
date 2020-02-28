from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        visited = set()
        def dfs(i):
            if i in visited:
                self.flag = False
                return False
            visited.add(i)
            for j in [leftChild[i], rightChild[i]]:
                if j != -1 and not dfs(j):
                    return False
            return True

        return dfs(0) and len(visited) == n


a = Solution()
print(a.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
print(a.validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]))
print(a.validateBinaryTreeNodes(n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1]))
