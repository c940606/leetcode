# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        from collections import defaultdict
        res = []
        lookup = defaultdict(int)
        def helper(root):
            if not root:
                return "#"
            s = helper(root.left)+"," + helper(root.right) + "," + str(root.val)
            if lookup[s] == 1:
                res.append(root)
            lookup[s] += 1
            return s
        helper(root)
        return res