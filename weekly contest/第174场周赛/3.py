# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        _sum = 0
        res = 0
        M = 10 ** 9 + 7

        def dfs(root):
            nonlocal _sum
            if not root:
                return
            _sum += root.val
            dfs(root.left)
            dfs(root.right)

        def dfs1(root):
            nonlocal res, _sum
            if not root:
                return 0
            left = dfs1(root.left)
            right = dfs1(root.right)
            res = max(res, (_sum - left) * left, (_sum - right) * right)
            return left + right + root.val

        dfs(root)
        dfs1(root)
        return res % M
