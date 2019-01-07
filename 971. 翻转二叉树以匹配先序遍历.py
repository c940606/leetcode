# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def flipMatchVoyage(self, root, voyage):
		"""
		:type root: TreeNode
		:type voyage: List[int]
		:rtype: List[int]
		"""
		res = []
		self.i = 0

		def helper(root):
			if not root:
				return True
			if root.val != voyage[self.i]:
				return False
			self.i += 1
			if root.left and root.left.val == voyage[self.i]:
				return helper(root.left) and helper(root.right)
			elif root.right and root.right.val == voyage[self.i]:
				if root.left:
					res.append(root.val)
				return helper(root.right) and helper(root.left)
			return root.left == root.right == None

		return res if helper(root) else [-1]
