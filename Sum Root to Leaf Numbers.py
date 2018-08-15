# Definition for a binary tree node.
from listcreatTree import creatTree
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def sumNumbers(self, root):
		"""
		给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。
			例如，从根到叶子节点路径 1->2->3 代表数字 123。
			计算从根到叶子节点生成的所有数字之和。
			说明: 叶子节点是指没有子节点的节点。
		---
		思路 ：
		把从根到叶子结点数放进数组里
		:type root: TreeNode
		:rtype: int
		"""
		if not root :
			return 0
		self.res = []
		self.dfs(root,"")
		return (self.res)

	def dfs(self, root, s):
		# print(val)
		# if root:
		#
		if  not root.left and not root.right:
			# print(root.val)
			self.res.append(int(s+str(root.val)))
			return
		# if not root :
		# 	print(root.val)
		# 	self.res.append(int(s))
		# 	return
		else:
			if root.left:
				self.dfs(root.left,s+str(root.val))
			if root.right:
				self.dfs(root.right,s+str(root.val))
a = Solution()
treelist = [4,9,0,5,1]
treelist1= [0,2]
t = creatTree()
tree = t.list_to_tree(treelist,TreeNode,0)
print(a.sumNumbers(tree))
