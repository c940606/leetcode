# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        M = 10 ** 9 + 7
        self.res = 0
        self.all_route = []

        def dfs(root, tmp):
            if not root: return
            if not root.left and not root.right:
                # self.all_route.append(tmp+str(root.val))
                self.res += int(tmp + str(root.val), 2) % M
                return
            tmp += str(root.val)
            dfs(root.left, tmp)
            dfs(root.right, tmp)

        dfs(root, "")
        # print(self.all_route)
        return self.res % M

    def sumRootToLeaf1(self, root: TreeNode) -> int:
        M = 10 ** 9 + 7

        def dfs(root, val):
            if not root: return 0
            val = (val * 2 + root.val) % M
            if root.left == root.right:
                return val
            return (dfs(root.left, val) + dfs(root.right, val)) % M

        return dfs(root, 0)
