"""
# Definition for a Node.
class Node(object):
	def __init__(self, val, children):
		self.val = val
		self.children = children
"""
class Solution(object):
	def postorder(self, root):
		"""
		:type root: Node
		:rtype: List[int]
		"""
		res = []
		def helper(root):
			if not root:
				return
			for child in root.children:
				helper(child)
			res.append(root.val)
		helper(root)
		return res

	def postorder1(self, root):
		res = []
		if not root:
			return res
		stack = [root]
		while stack:
			curr = stack.pop()
			res.append(curr.val)
			stack.extend(curr.children)
		return res[::-1]
