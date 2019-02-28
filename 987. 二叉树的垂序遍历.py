# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        from collections import defaultdict
        lookup = defaultdict(list)

        def preorder(root, x, y):
            if not root:
                return
            lookup[x].append((y, root.val))
            preorder(root.left, x - 1, y + 1)
            preorder(root.right, x + 1, y + 1)

        preorder(root, 0, 0)
        print(lookup)
        for key in lookup:
            lookup[key].sort()
        keys_list = list(lookup.keys())
        keys_list.sort()
        return [[x[1] for x in lookup[k]] for k in keys_list]
