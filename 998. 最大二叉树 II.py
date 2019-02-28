# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        pre = None
        cur = root
        while cur and cur.val > val:
            pre, cur = cur, cur.right
        node = TreeNode(val)
        node.left = cur
        if pre:
            pre.right = node
        return root if root.val > val else node

    def insertIntoMaxTree1(self, root: 'TreeNode', val: 'int') -> 'TreeNode':
        if root and root.val > val:
            root.right = self.insertIntoMaxTree1(root.right, val)
            return root
        node = TreeNode(val)
        node.left = root
        return node
