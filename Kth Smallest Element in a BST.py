# Definition for a binary tree node.
from listcreatTree import creatTree
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def kthSmallest(self, root, k):
		"""
		给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。
			说明：
			你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。
		---
		输入: root = [3,1,4,null,2], k = 1
		   3
		  / \
		 1   4
		  \
		   2
		输出: 1
		---
		中序遍历
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		res = []
		def zhongXun(root):
			if not root:
				return
			zhongXun(root.left)
			res.append(root.val)
			zhongXun(root.right)
		zhongXun(root)
		# print(res)
		return res[k-1]

	def kthSmallest1(self, root, k):
		self.res = None
		self.count = 0
		def helper(root):
			if not root:
				return
			helper(root.left)
			self.count += 1
			if self.count == k:
				self.res = root.val
				return
			helper(root.right)
		return self.res

treelist = [3,1,4,"#",2]
t = creatTree()
tree = 	t.list_to_tree(treelist,TreeNode,0)
a = Solution()
print(a.kthSmallest1(tree,1))
