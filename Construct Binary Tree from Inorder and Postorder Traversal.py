# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def buildTree(self, inorder, postorder):
		"""
		根据一棵树的中序遍历与后序遍历构造二叉树。
		---
		中序遍历 inorder = [9,3,15,20,7]
		后序遍历 postorder = [9,15,7,20,3]
		---
		思路
		中序：左-->根-->右
		后序：左--->右--->根

		:type inorder: List[int]
		:type postorder: List[int]
		:rtype: TreeNode
		"""
		if not inorder:
			return None
		val = postorder[-1]
		# print(val)
		x = inorder.index(val)
		# print(x)
		root = TreeNode(val)

		root.left = self.buildTree(inorder[:x],postorder[:x])
		root.right = self.buildTree(inorder[x+1:],postorder[x:-1])
		return root
a = Solution()
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
print(a.buildTree(inorder,postorder).val)

