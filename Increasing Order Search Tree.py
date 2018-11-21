# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def increasingBST(self, root):
		"""
		:type root: TreeNode
		:rtype: TreeNode
		"""
		res = []
		def helper(root):
			if not root:
				return
			helper(root.left)
			res.append(root.val)
			helper(root.right)
		helper(root)
		ans = current = TreeNode(None)
		for i in res:
			current.right = TreeNode(i)
			current = current.right
		return ans.right