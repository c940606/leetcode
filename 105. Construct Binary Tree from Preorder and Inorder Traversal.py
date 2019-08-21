# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        root = TreeNode(preorder[0])
        loc = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: loc + 1], inorder[: loc])
        root.right = self.buildTree(preorder[loc + 1:], inorder[loc + 1:])
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        from collections import defaultdict
        n = len(preorder)
        inorder_map = defaultdict(int)
        for idx, val in enumerate(inorder):
            inorder_map[val] = idx

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start == pre_end:
                return None
            root = TreeNode(preorder[pre_start])
            loc = inorder_map[preorder[pre_start]]
            root.left = helper(pre_start + 1, pre_start + 1 + loc - in_start, in_start, loc)
            root.right = helper(pre_start + 1 + loc - in_start, pre_end, loc + 1, in_end)
            return root

        return helper(0, n, 0, n)
    
