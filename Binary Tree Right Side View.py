# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def rightSideView(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []
		cur = [root]
		res = [root.val]
		while cur:
			temp = []
			for node in cur:
				if node.left:
					temp.append(node.left)
				if node.right:
					temp.append(node.right)
			if temp:
				res.append(temp[-1].val)
			cur = temp
		return res
