# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		"""
		给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
		百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
		满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
		例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
		_______6______
	   /              \
	___2__          ___8__
   /      \        /      \
   0      _4       7       9
		 /  \
		 3   5
		 ----
		 输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
		输出: 6
		解释: 节点 2 和节点 8 的最近公共祖先是 6。
		---
		输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
		输出: 2
		解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		if not root:
			return root
		if root.val > p.val and root.val > q.val:
			return self.lowestCommonAncestor(root.left,p,q)
		if root.val < p.val and root.val < q.val:
			return self.lowestCommonAncestor(root.right,p,q)
		return root