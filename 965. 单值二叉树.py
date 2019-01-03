# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isUnivalTree(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		tmp = root.val
		cur = [root]
		while cur:
			next_level = []
			for node in cur:
				if node.left:
					if node.left.val != tmp:
						return False
					next_level.append(node.left)

				if node.right:
					if node.right.val != tmp:
						return False
					next_level.append(node.right)
			cur = next_level
		return True

	def isUnivalTree1(self, root):
		def dfs(node):
			return not node or node.val == root.val and dfs(node.left) and dfs(node.right):
		return dfs(root)