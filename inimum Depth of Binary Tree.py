# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def minDepth(self, root):
		"""
		给定一个二叉树，找出其最小深度。
		最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
		说明: 叶子节点是指没有子节点的节点。
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		if not root.left or not root.right:
			return 1 + max(self.minDepth(root.right), self.minDepth(root.left))
		return 1+min(self.minDepth(root.right),self.minDepth(root.left))