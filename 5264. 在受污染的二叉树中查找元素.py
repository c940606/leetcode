# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:
    self.lookup = set()

    def __init__(self, root: TreeNode):

        def helper(root, val):
            if not root:
                return
            root.val = val
            self.lookup.add(val)
            if root.left:
                root.left.val = val * 2 + 1
                helper(root.left, val * 2 + 1)
            if root.rigth:
                root.rigth.val = val * 2 + 2
                helper(root.rigth, val * 2 + 2)

        helper(root, 0)

    def find(self, target: int) -> bool:
        return target in self.lookup

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
