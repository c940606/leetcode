# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = 0

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root: return self.res
        if self.isSameVal(root, root.val): self.res += 1
        self.countUnivalSubtrees(root.left)
        self.countUnivalSubtrees(root.right)
        return self.res

    def isSameVal(self, root, val):
        if not root: return True
        return root.val == val and self.isSameVal(root.left, val) and self.isSameVal(root.right, val)
