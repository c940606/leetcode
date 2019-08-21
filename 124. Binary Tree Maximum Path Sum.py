# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root, res):
        if not root: return float("-inf")
        left = max(0, self.helper(root.left, res))
        right = max(0, self.helper(root.right, res))
        res = max(res, root.val + left + right)
        return root.val + max(left, right)
    def maxPathSum(self, root: TreeNode) -> int:
        res = float("-inf")
        self.helper(root, res)
        return res
