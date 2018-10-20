"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: Node
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		res = []
		cur = [root]
		while cur:
			next = []
			temp = []
			for node in cur:
				temp.append(node.val)
				next += node.children
			res.append(temp)
			cur = next
		return res