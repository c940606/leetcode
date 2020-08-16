class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        node = []

        def dfs(root):
            if not root:
                return
            node.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        def constr(node):
            if not node:
                return
            mid = len(node) // 2
            root = TreeNode(node[mid])
            root.left = constr(node[:mid])
            root.right = constr(node[mid + 1:])
            return root

        return constr(sorted(node))
