# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isBalanced(self, root):
		"""
		给定一个二叉树，判断它是否是高度平衡的二叉树。
		本题中，一棵高度平衡二叉树定义为：
		一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
		---

		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return True
		return abs(self.height(root.right)-self.height(root.left))<2 and self.isBalanced(root.left) and self.isBalanced(root.right)

	def height(self, node):
		if not node:
			return 0
		return 1+max(self.height(node.right),self.height(node.left))