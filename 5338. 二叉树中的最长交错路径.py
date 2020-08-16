# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestZigZag1(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root):
            nonlocal ans
            res = [0, 0]
            if root.left:
                _left = dfs(root.left)
                res[0] = res[1] + 1
            if root.right:
                _right = dfs(root.right)
                res[1] = res[0] + 1
            ans = max(ans, res[0], res[1])
            return res

        dfs(root)
        return ans

    def longestZigZag(self, root: TreeNode) -> int:
        visited = set()
        def dfs1(root, flag):
            if not root:
                return 0
            visited.add((root, flag))
            res = 0
            if flag:
                res = max(res, dfs(root.left, not flag))
            else:
                res = max(res, dfs(root.right, not flag))

            return res
        ans = 0
        def dfs2(root):
            nonlocal ans
            if not root:
                return

            if (root, True) not in visited:
                ans = max(ans, dfs1(root, True))
            if (root, False) not in visited:
                ans = max(ans, dfs1(root, False))
            dfs2(root.left)
            dfs2(root.right)

        dfs2(root)
        return ans



