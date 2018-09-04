# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def postorderTraversal(self, root):
		"""
		给定一个二叉树，返回它的 后序 遍历。
		---
		输入: [1,null,2,3]
		   1
			\
			 2
			/
		   3

		输出: [3,2,1]
		---
		思路:
		左 --> 右 --> 根
		:type root: TreeNode
		:rtype: List[int]
		"""
		res = []
		def helper(root):
			if not root:
				return
			helper(root.left)
			helper(root.right)
			res.append(root.val)
		helper(root)
		return res

	def postorderTraversal1(self, root):
		res = []
		stack = []
		flag_stack = []

		while stack or root:
			while root:
				stack.append(root)
				flag_stack.append(0)
				root = root.left
			while stack and flag_stack[-1] == 1:
				flag_stack.pop()
				res.append(stack.pop())


			if stack:
				flag_stack.pop()
				flag_stack.append(1)
				root = stack[-1]
				root = root.right
		return res