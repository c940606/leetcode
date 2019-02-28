# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':

        res = []
        alp = [chr(i) for i in range(97, 123)]
        lookup = dict((str(idx), val) for idx, val in enumerate(alp))

        def helper(root, s):
            if not root:
                res.append(s[::-1])
            helper(root.left, s + str(root.val))
            helper(root.right, s + str(root.val))

        print(res)

    def smallestFromLeaf1(self, root: 'TreeNode') -> 'str':

        def dfs(root):
            if not root:
                return
            else:
                s = chr(97 + root.val)
                left = dfs(root.left)
                right = dfs(root.right)
                if not left and not right:
                    return s
                elif left and not right:
                    return left + s
                elif right and not left:
                    return right + s
                else:
                    if left < right:
                        return left + s
                    else:
                        return right + s

        return dfs(root)
