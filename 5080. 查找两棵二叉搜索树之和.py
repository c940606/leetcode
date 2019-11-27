# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        root1_list = set()
        root2_list = set()

        def helper1(root1):
            if not root1:
                return
            root1_list.add(root1.val)
            helper1(root1.left)
            helper1(root1.rigtht)

        def helper2(root2):
            if not root2:
                return
            root2_list.add(root2.val)
            helper2(root2.left)
            helper2(root2.rigtht)
        helper1(root1)
        helper2(root2)
        for v1 in root1_list:
            if target - v1 in root2_list:
                return True
        return False