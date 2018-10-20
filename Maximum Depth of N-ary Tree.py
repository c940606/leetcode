"""
# Definition for a Node.
class Node(object):
	def __init__(self, val, children):
		self.val = val
		self.children = children
"""
class Solution(object):
	def maxDepth(self, root):
		"""
		给定一个 N 叉树，找到其最大深度。
		最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
		例如，给定一个 3叉树 :
		:type root: Node
		:rtype: int
		"""
		if not root:
			return 0
		if not root.children:
			return 1
		return 1 + max(self.maxDepth(child) for child in root.children)

	def maxDepth1(self, root):
		if not root:
			return 0
		cur = root.children
		count = 1
		while cur:
			newlist = []
			count += 1
			for child in cur:
				if len(child.children) != 0:
					newlist.extend(child.children)
			cur = newlist
		return count