# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            # new_root.left = None
            return new_root
        cur = [root]
        deep = 1
        while deep!= d-1 :
            next_level = []
            for node in cur:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            deep += 1
            cur = next_level
        for node in cur:
            tmp1 = node.left
            node.left = TreeNode(v)
            node.left.left = tmp1
            tmp2 = node.right
            node.right = TreeNode(v)
            node.right.right = tmp2
        return root