# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def countNodes1(self, root):
		"""
		给出一个完全二叉树，求出该树的节点个数。
		说明：
		完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
		并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
		----
		输入:
			1
		   / \
		  2   3
		 / \  /
		4  5 6
		输出: 6
		---
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		if not root.left and not root.right:
			return 1
		return self.countNodes1(root.left) + self.countNodes1(root.right) + 1

	def countNodes2(self, root):
		if not root:
			return 0
		p,q =root,root
		leftheight = 0
		rightheight = 0
		while p:
			p = p.left
			leftheight += 1
		while q:
			q = q.right
			rightheight += 1
		if leftheight == rightheight:
			return 2 **leftheight - 1
		else:
			return 1 + self.countNodes2(root.left) + self.countNodes2(root.right)