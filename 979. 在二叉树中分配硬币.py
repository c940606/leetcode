# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def dfs(root):
            if not root:return 0
            left,right = dfs(root.left),dfs(root.right)
            self.res = abs(left) + abs(right)
            return root.val + left + right -1
        dfs(root)
        return self.res