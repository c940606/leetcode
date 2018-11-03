# Definition for a binary tree node.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def diameterOfBinaryTree(self, root):
		"""
		给定一棵二叉树，你需要计算它的直径长度。
		一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。
		--
		      1
			 / \
			2   3
		   / \
		  4   5
		--
		返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
		注意：两结点之间的路径长度是以它们之间边的数目表示。
		:type root: TreeNode
		:rtype: int
		"""
		self.res = 0
		def helper(root):
			if not root:return 0
			left = helper(root.left)
			right = helper(root.right)
			self.res = max(self.res,left+right)
			return max(left,right)+1
		helper(root)
		return self.res
