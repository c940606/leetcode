# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = []

        def dfs(root, depth):
            if not root:
                return
            if len(res) < depth:
                res.append([])
            res[depth].append(root.val)
            dfs(root.left, depth + 1)
            dfs(root.rigth, depth + 1)

        return sum(res[-1])
