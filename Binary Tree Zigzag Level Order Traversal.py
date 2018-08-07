# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class creatTree:
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
	def zigzagLevelOrder(self, root):
		"""
		给定一个二叉树，返回其节点值的锯齿形层次遍历。
		（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
		---
		思路:
		1.层次遍历
			用栈

		2. 设置标志
			偶数:从左往右
			奇数:从右往左 ---->取反
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		# 为空
		if not root:
			return []
		res,cur_node = [],[root]
		flag = 0
		while cur_node:
			temp = []
			next_node = []
			for item in cur_node:
				temp.append(item.val)
				if item.left:
					next_node.append(item.left)
				if item.right:
					next_node.append(item.right)
			if flag%2 == 0:
				res.append(temp)
			else:
				res.append(temp[::-1])
			flag += 1
			cur_node = next_node
		return res
tree_list = [3,9,20,"#","#",15,7]
creat_tree = creatTree()
tree = creat_tree.list_to_tree(TreeNode,tree_list,0)
a = Solution()
print(a.zigzagLevelOrder(tree))

