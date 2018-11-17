# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def findBottomLeftValue(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return
		cur = [root]
		while cur:
			temp = []
			for node in cur:
				if node.left :
					temp.append(node.left)
				if node.right:
					temp.append(node.right)
			if not temp:
				return cur[0].val
			cur = temp