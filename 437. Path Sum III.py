# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, _sum: int) -> int:
        res = 0

        def dfs(root, _sum):
            nonlocal res
            if not root: return
            if _sum - root.val == 0: res += 1

            _sum -= root.val
            dfs(root.left, _sum)
            dfs(root.right, _sum)

        def helper(root):

            if not root: return
            dfs(root, _sum)
            # print(res)
            helper(root.left)
            helper(root.right)

        helper(root)

        return res 
