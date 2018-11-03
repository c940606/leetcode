# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
        helper(root)
        n = len(res)
        min_num = res[1]-res[0]
        for i in range(2,n):
            if min_num > res[i]-res[i-1]:
                min_num = res[i]-res[i-1]
        return min_num