# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree1(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder: return None
        root = TreeNode(postorder[-1])
        loc = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[: loc], postorder[:loc])
        root.right = self.buildTree(inorder[loc + 1:], postorder[loc:-1])
        return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        from collections import defaultdict
        n = len(preorder)
        inorder_map = defaultdict(int)
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx

        def helper(in_start, in_end, post_start, post_end):
            if in_start == in_end:
                return null
            root = TreeNode(postorder[post_end - 1])
            loc = inorder[postorder[post_end - 1]]
            root.left = helper(in_start, loc, post_start, post_start + loc - in_start)
            root.right = helper(loc + 1, in_end, post_start + loc - in_start, post_end - 1)
            return root

        return helper(0, n, 0, n)
