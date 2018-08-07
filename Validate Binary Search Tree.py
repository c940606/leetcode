# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class CreatTree:
	def list_to_tree(self,root,tree_list,i):
		if i < len(tree_list):
			if tree_list[i] == "#":
				return None
			else:
				root = TreeNode(tree_list[i])
				root.left = self.list_to_tree(root.left,tree_list,i*2+1)
				root.right = self.list_to_tree(root.right,tree_list,i*2+2)
				return root
		return root




class Solution:
	def isValidBST(self, root):
		"""
		给定一个二叉树，判断其是否是一个有效的二叉搜索树。
		---
		输入:[5,1,4,"#","#",3,6]
		输出:False
		----
		思路:
		递归
		搜索树在一定的范围里

		:type root: TreeNode
		:rtype: bool
		"""
		return self.isBST(root,float("-inf"),float("inf"))

	def isBST(self, root, min_val, max_val):

		if root == None:
			return True
		# print(root.val)
		if root.val >= max_val or root.val <= min_val:
			return False
		return self.isBST(root.left,min_val,root.val) and self.isBST(root.right,root.val,max_val)

a = Solution()
list_tree = [5,1,4,"#","#",3,6]
list_tree1 = [2,1,3]
creatTree = CreatTree()
tree = creatTree.list_to_tree(TreeNode,list_tree1,0)
print(a.isValidBST(tree))

