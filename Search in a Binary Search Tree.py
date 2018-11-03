# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def searchBST(self, root, val):
		"""
		:type root: TreeNode
		:type val: int
		:rtype: TreeNode
		"""
		# if not root:
		#     return None
		if root and root.val == val:
			return root
		if root and root.val > val:
			return self.searchBST(root.left,val)
		if root and root.val < val :
			return self.searchBST(root.right,val)
		return None
		# 非递归
		# if not root:
		#     return None
		# while root :
		#     if root.val == val:
		#         return root
		#     elif root.val > val :
		#         root = root.left
		#     elif root.val < val :
		#         root = root.right
		# return None