# Definition for a binary tree node.
from listcreatTree import creatTree
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	# def pathSum(self, root, sum):
	# 	"""
	# 	给定一个二叉树，它的每个结点都存放着一个整数值。
	# 	找出路径和等于给定数值的路径总数。
	# 	路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
	# 	二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
	# 	---
	# 	root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
	# 			  10
	# 			 /  \
	# 			5   -3
	# 		   / \    \
	# 		  3   2   11
	# 		 / \   \
	# 		3  -2   1
	# 	返回 3。和等于 8 的路径有:
	# 	1.  5 -> 3
	# 	2.  5 -> 2 -> 1
	# 	3.  -3 -> 11
	# 	---
	# 	思路:
	#
	# 	:type root: TreeNode
	# 	:type sum: int
	# 	:rtype: int
	# 	"""
	# 	self.count = 0
	# 	def helper(root,tmp):
	#
	# 		if not root:
	# 			return
	# 		# print(root.val)
	# 		if tmp+root.val == sum:
	# 			# print(root.val)
	# 			self.count += 1
	# 			# return
	# 		helper(root.left,tmp+root.val)
	# 		helper(root.right, tmp + root.val)
	# 		# print("---")
	# 		helper(root.left,0)
	#
	# 		helper(root.right,0)
	# 	helper(root,sum)
	# 	# self.pathSum(root.left)
	# 	return self.count
	def __init__(self):
		self.count = 0
	def pathSum1(self, root, sum):
		if not root:
			return

		self.helper(root,0,sum)
		print(self.count)
		self.pathSum1(root.left,sum)
		self.pathSum1(root.left,sum)
		return self.count

	def helper(self,root, tmp,sum):
		if not root:
			return
		if tmp == sum :
			self.count += 1

		self.helper(root.left, tmp + root.val,sum)
		self.helper(root.right, tmp + root.val,sum)


t = creatTree()
t_list = [10,5,-3,3,2,"#",11,3,-2,"#",1]
t_list1 = [1,"#",2,"#",3,"#",4,"#",5]
tree = t.list_to_tree(t_list,TreeNode,0)
a  = Solution()
print(a.pathSum1(tree,8))
