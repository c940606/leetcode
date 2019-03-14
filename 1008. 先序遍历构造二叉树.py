# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        inorder = sorted(preorder)

        def buildTree( preorder, inorder):
            if not preorder:
                return None
            # 找到根的索引
            x = inorder.index(preorder[0])
            root = TreeNode(preorder[0])
            root.left = buildTree(preorder[1:x + 1], inorder[0:x])
            root.right = buildTree(preorder[x + 1:], inorder[x + 1:])
            return root
        return buildTree(preorder,inorder)