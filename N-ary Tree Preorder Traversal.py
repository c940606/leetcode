"""
# Definition for a Node.
class Node(object):
	def __init__(self, val, children):
		self.val = val
		self.children = children
"""
class Solution(object):
	def preorder(self, root):
		"""
		:type root: Node
		:rtype: List[int]
		"""
		res = []
		def helper(root):
			if not root:
				return
			res.append(root.val)
			for child in root.children:
				helper(child)
		helper(root)
		return res

	def preorder1(self, root):
		if not root:
			return []
		res = []
		cur = [root]
		while cur:
			node = cur.pop()
			res.append(node.val)
			for child in node.children[::-1]:
				if child:
					cur.append(child)
		return res