# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def findSecondMinimumValue(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		res = []

		def helper(root):
			if not root:
				return
			res.append(root.val)
			helper(root.left)
			helper(root.right)

		helper(root)

		res = set(res)
		# print(res)
		if len(res) < 2: return -1
		res.remove(min(res))
		# print(res)
		return min(res)

	def findSecondMinimumValue1(self, root):