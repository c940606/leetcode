# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent1(self, root: TreeNode) -> int:

        res = 0

        def dfs(root, flag):
            nonlocal res
            if not root: return
            if flag == 0:
                res += root.val
            if root.val % 2 == 0:
                flag = 2
            dfs(root.left, flag - 1)
            dfs(root.right, flag - 1)

        def helper(root):
            if not root:
                return
            dfs(root, 2 if root.val % 2 == 0 else -1)
            helper(root.left)
            helper(root.right)

        return res

    def sumEvenGrandparent(self, root: TreeNode, p=1, gp=1) -> int:
        if not root: return 0
        left = self.sumEvenGrandparent(root.left, root.val, p)
        right = self.sumEvenGrandparent(root.right, root.val, p)
        return left + right + root.val * (1 - gp % 2)
