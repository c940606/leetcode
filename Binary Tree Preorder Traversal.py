# Definition for a binary tree node.
from listcreatTree import creatTree
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def preorderTraversal(self, root):
		"""
		给定一个二叉树，返回它的 前序 遍历。
		----
		输入: [1,null,2,3]
		   1
			\
			 2
			/
		   3

		输出: [1,2,3]
		---
		前序 跟 --> 左 --> 右
		:type root: TreeNode
		:rtype: List[int]
		"""
		self.res = []
		self.helper(root)
		return self.res

	def helper(self,root):
		if not root:
			return
		self.res.append(root.val)
		self.helper(root.left)
		self.helper(root.right)

	def preorderTraversal1(self, root):
		res = []
		if not root:
			return res
		stack = []
		stack.append(root)
		while stack:
			node = stack.pop()
			res.append(node.val)
			if node.right:
				stack.append(node.right)
			if node.left:
				stack.append(node.left)
		return res

treelist = [1,"#",2,3,4,5]
tree = creatTree()
t = tree.list_to_tree(treelist,TreeNode,0)
a = Solution()
print(a.preorderTraversal(t))