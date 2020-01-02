# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []

        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            height = max(left, right)
            if len(res) == height:
                res.append([])
            res[height].append(root.val)
            #print(height, root.val)
            return height + 1
        helper(root)
