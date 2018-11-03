# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def findTarget(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: bool
		"""
		res = []
		def helper(root):
			if not root:return
			helper(root.left)
			res.append(root.val)
			helper(root.right)
		helper(root)
		n = len(res)
		if n < 1:
			return False
		i = 0
		j = n-1
		while i < j :
			temp = res[i] + res[j]
			if temp == k:
				return True
			elif temp > k :
				j -= 1
			else:
				i += 1
		return False

	def findTarget1(self, root, k):
		if not root:
			return False
		bfs = [root]
		s = set()
		for i in bfs:
			if k-i.val in s:return True
			s.add(i.val)
			if i.left:bfs.append(i.left)
			if i.right:bfs.append(i.right)
		return False