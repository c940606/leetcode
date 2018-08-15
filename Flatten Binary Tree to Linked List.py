# Definition for a binary tree node.

from listcreatTree import creatTree
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def flatten(self, root):
		"""
		给定一个二叉树，原地将它展开为链表。
		---
		:type root: TreeNode
		:rtype: void Do not return anything, modify root in-place instead.
		"""
		self.dummy = TreeNode(0)
		self.p = self.dummy
		self.tran(root)
		return list(self.dummy.right)

	def tran(self, root):
		if root:
			print(root.val)
			node = TreeNode(root.val)
			# self.p = TreeNode(root.val)
			self.p.right = node
			self.p = node
		if not root:
			return
		if root.left:
			self.tran(root.left)
		if root.right:
			self.tran(root.right)

a = creatTree()
b = Solution()
treelist = [1,2,5,3,4,"#",6]
tree = a.list_to_tree(treelist,TreeNode,0)
print(b.flatten(tree))

