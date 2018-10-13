# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def invertTree(self, root):
		"""
		翻转一棵二叉树。
		----
			 4
		   /   \
		  2     7
		 / \   / \
		1   3 6   9

			 4
		   /   \
		  7     2
		 / \   / \
		9   6 3   1
		---
		思路:
		递归
		:type root: TreeNode
		:rtype: TreeNode
		"""
		if not root:
			return
		root.left ,root.right = root.right,root.left
		self.invertTree(root.right)
		self.invertTree(root.left)
		return root