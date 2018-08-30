# Definition for a binary tree node.
from listcreatTree import creatTree
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def largestValues(self, root):
		"""
		您需要在二叉树的每一行中找到最大的值。
		---
		输入:
				  1
				 / \
				3   2
			   / \   \
			  5   3   9

		输出: [1, 3, 9]
		---
		层次遍历
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return
		res = []
		cur = [root]
		while cur:
			next_level = []
			temp = []
			for item in cur:
				temp.append(item.val)
				if item.left:
					next_level.append(item.left)
				if item.right:
					next_level.append(item.right)
			cur = next_level
			res.append(temp)
		return list(map(max,res))

treelist = [1,2,3,4,5,6,7]
t = creatTree()
tree = t.list_to_tree(treelist,TreeNode,0)
a = Solution()
print(a.largestValues(tree))