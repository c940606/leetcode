class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0
        res = 0
        def dfs(root, cur):
            nonlocal res
            if not root: return
            if cur <= root.val: res += 1
            dfs(root.left, max(root.val, cur))
            dfs(root.right, max(root.val, cur))

        dfs(root, float("-inf"))
        return res