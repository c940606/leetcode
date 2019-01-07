# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def constructFromPrePost(self, pre, post):
		"""
		:type pre: List[int]
		:type post: List[int]
		:rtype: TreeNode
		"""
		if not pre:
			return
		root = TreeNode(pre[0])
		pre = pre[1:]
		post = post[:-1]
		if not pre:
			return root
		idx = post.index(pre[0])
		root.left = self.constructFromPrePost(pre[:idx+1], post[:idx+1])
		root.right = self.constructFromPrePost(pre[idx+1:], post[idx+1:])
		return root
