# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isCompleteTree(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		from collections import deque
		q = deque([root])
		flag = 1
		while q:
			node = q.popleft()
			if node.left:
				if not flag: return False
				q.append(node.left)
			else:
				flag = 0
			if node.right:
				if not flag: return False
				q.append(node.right)
			else:
				flag = 0
		return True
