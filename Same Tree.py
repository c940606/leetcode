# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isSameTree(self, p, q):
		"""
		给定两个二叉树，编写一个函数来检验它们是否相同。
		如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
		:type p: TreeNode
		:type q: TreeNode
		:rtype: bool
		"""
		if (not q and p) or (not p and q):
			return False
		if not q and not p:
			return True
		if q == p :
			return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
		return False


