# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def insertIntoBST(self, root, val):
		"""
		:type root: TreeNode
		:type val: int
		:rtype
		"""
		node = root
		while node:
			if node.val < val:
				if node.right:
					node = node.right
				else:
					node.right = TreeNode(val)
					break
			else:
				if node.left:
					node = node.left
				else:
					node.left = TreeNode(val)
					break
		return root

	def insertIntoBST1(self, root, val):
		if not root:
			return TreeNode(val)
		if root.val < val:
			root.right = self.insertIntoBST(root.right, val)
		else:
			root.left = self.insertIntoBST(root.left,val)
		return root
