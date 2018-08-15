# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def buildTree(self, preorder, inorder):
		"""
		根据一棵树的前序遍历与中序遍历构造二叉树。
		---
		前序遍历 preorder = [3,9,20,15,7]
		中序遍历 inorder = [9,3,15,20,7]
		---
		思路：
		前序：从根开始
		中序：从左开始
		:type preorder: List[int]
		:type inorder: List[int]
		:rtype: TreeNode
		"""
		if not preorder:
			return None
		# 找到根的索引
		x = inorder.index(preorder[0])
		root = TreeNode(preorder[0])
		root.left = self.buildTree(preorder[1:x+1],inorder[0:x])
		root.right = self.buildTree(preorder[x+1:],inorder[x+1:])
		return root
a = Solution()
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(a.buildTree(preorder,inorder).val)