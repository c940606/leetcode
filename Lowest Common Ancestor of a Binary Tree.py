# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		"""
		给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
		百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，
		最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
		例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
		    _______3______
		   /              \
		___5__          ___1__
		/      \        /      \
		6      _2       0       8
			 /  \
			 7   4
		---
		输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
		输出: 3
		解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
		---
		输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
		输出: 5
		解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		def findPath(root,path,node):
			if not root:
				return False
			path.append(root)
			if root == node:
				return True
			if (root.left and findPath(root.left,path,node) ) or (root.right and findPath(root.right,path,node)):
				return True
			path.pop()
			return False
		path_p ,path_q = [],[]
		if not findPath(root,path_p,p) or not findPath(root,path_q,q):
			return -1
		i = 0
		while i < len(path_q) and i < len(path_p):
			if path_q[i] != path_p[i]:
				break
			i += 1
		return path_q[i-1]

	def lowestCommonAncestor1(self, root, p, q):
		if not root or root == p or root == q:
			return root
		left =self.lowestCommonAncestor(root.left,p,q)
		right = self.lowestCommonAncestor(root.right,p,q)
		if left and right :
			return root
		return left or right
