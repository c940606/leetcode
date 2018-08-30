# Definition for a binary tree node.
from listcreatTree import creatTree
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def sumOfLeftLeaves(self, root):
		"""
		计算给定二叉树的所有左叶子之和。
		---
			3
		   / \
		  9  20
			/  \
		   15   7
		在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
		---
		思路：
		用递归把所有左子树找出来

		:type root: TreeNode
		:rtype: int
		"""
		left = []
		def find_left(root):
			if not root:
				return
			if root.left :
				print(root.left.val)
				if not root.left.left and not root.left.right:
					left.append(root.left.val)
			find_left(root.left)
			find_left(root.right)
		find_left(root)
		print(left)
		return sum(left)

treelist = [1,2,3,4,"#","#",5]
treelist1 = [3,9,20,"#","#",15,7]
t = creatTree()
tree = t.list_to_tree(treelist,TreeNode,0)
a = Solution()
print(a.sumOfLeftLeaves(tree))