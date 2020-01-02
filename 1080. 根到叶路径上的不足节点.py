# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:

        def dfs(root, cur):
            if not root:return
            dfs(root.left, cur + root.val)
            dfs(root.right, cur + root.val)
        dfs(root, 0)
