# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	'''
	递归
	非递归
	'''
	def inorderTraversal(self, root):
		"""
		给定一个二叉树，返回它的中序 遍历
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return
		else:
			self.inorderTraversal(root.left)
			print(root.val)
			self.inorderTraversal(root.right)

	def inorderTraversal1(self, root):
		stack = []
		res = []
		while root or stack:
			while root:
				stack.append(root)
				root = root.left
			if stack:
				temp = stack.pop()
				res.append(temp.val)
				root = temp.right
		return res







a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.right = b
b.left = c
S = Solution()
S.inorderTraversal(a)
print("----")
print(S.inorderTraversal1(a))