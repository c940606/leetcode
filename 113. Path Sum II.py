from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, _sum: int) -> List[List[int]]:
        res = []

        def dfs(root, _sum, tmp):
            if not root: return
            if not root.left and not root.right and _sum - root.val == 0:
                res.append(tmp + [root.val])
                return
            _sum -= root.val
            dfs(root.left, _sum, tmp + [root.val])
            dfs(root.right, _sum, tmp + [root.val])

        dfs(root, _sum, [])
        return res
