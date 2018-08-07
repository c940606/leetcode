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
	def levelOrderBottom(self, root):
		"""
		给定一个二叉树，返回其节点值自底向上的层次遍历。
		（即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		res,cur_level = [],[root]
		while cur_level:
			temp = []
			next_level = []
			for item in cur_level:
				temp.append(item.val)
				if item.left:
					next_level.append(item.left)
				if item.right:
					next_level.append(item.right)
			res.append(temp)
			cur_level = next_level
		return res[::-1]
tree_list = [3,9,20,"#","#",15,7]
creat_tree = creatTree()
tree = creat_tree.list_to_tree(TreeNode,tree_list,0)
a = Solution()
print(a.levelOrderBottom(tree))