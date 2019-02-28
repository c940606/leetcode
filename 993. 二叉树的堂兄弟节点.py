# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: 'TreeNode', x: 'int', y: 'int') -> 'bool':
        if not root:
            return False
        cur = [root]
        while cur:
            next_level = []
            next_val = []
            for node in cur:
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.right.val == x and node.left.val ==y):
                        return False
                if node.left:
                    next_val.append(node.left.val)
                    next_level.append(node.left)
                if node.right:
                    next_val.append(node.right.val)
                    next_level.append(node.right)
            if x in next_val and y in next_val:
                return True
            elif x not in next_val and y not in next_val:
                cur = next_level
            else:
                return False
        return False
