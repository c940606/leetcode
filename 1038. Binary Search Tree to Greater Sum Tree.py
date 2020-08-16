class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        cur = 0
        if not root: return root

        def dfs(root):
            nonlocal cur
            if not root.left and not root.right:
                return
            dfs(root.right)
            root.val += cur
            cur += root.val
            dfs(root.left)

        dfs(root)
        return root







