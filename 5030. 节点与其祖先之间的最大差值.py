# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = float("-inf")

        def dfs(root, root_to_leaf):
            if not root.right and not root.left:
                root_to_leaf.append(root.val)
                self.res = max(self.res, max(root_to_leaf) - min(root_to_leaf))
                return
            if root.left:
                dfs(root.left, root_to_leaf + [root.val])
            if root.right:
                dfs(root.right, root_to_leaf + [root.val])

        dfs(root, [])
        return self.res

    def maxAncestorDiff1(self, root, min_num=float("inf"), max_num=float("-inf")):
        if not root: return max_num - min_num
        max_num = max(max_num, root.val)
        min_num = min(min_num, root.val)
        return max(self.maxAncestorDiff1(root.left, min_num, max_num),
                   self.maxAncestorDiff1(root.right, min_num, max_num))
