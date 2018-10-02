# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def convertBST(self, root):
		"""
		给定一个二叉搜索树（Binary Search Tree），
		把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

		:type root: TreeNode
		:rtype: TreeNode
		"""
		if not root:
			return root
		inorder = []
		def helper1(root):
			if not root:
				return
			helper1(root.left)
			inorder.append(root.val)
			helper1(root.right)
		helper1(root)
		n = len(inorder)
		i = n-2
		while i>=0:
			inorder[i] += inorder[i+1]
			i -= 1
		self.loc = 0
		def helper2(root):
			if not root:
				return
			helper2(root.left)
			root.val = inorder[self.loc]
			self.loc += 1
			helper2(root.right)
		helper2(root)
		return root

	def convertBST1(self, root):
		if not root:
			return root
		self.s= 0
		def helper(root):
			if not root:
				return
			helper(root.right)
			self.s += root.val
			root.val = self.s
			helper(root.left)
		helper(root)
		return root
