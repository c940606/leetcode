# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def longestUnivaluePath(self, root):
		"""
		给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
		注意：两个节点之间的路径长度由它们之间的边数表示。
		---
				  5
				 / \
				4   5
			   / \   \
			  1   1   5
			  输出2
		---
		思路:
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		self.res = 0
		def helper(root,val):
			if not root:
				return 0
			left = helper(root.left,root.val)
			right = helper(root.right,root.val)
			self.res = max(left+right,self.res)
			if root.val == val:
				return max(left,right) + 1
			else:
				return 0
		helper(root,None)
		return self.res