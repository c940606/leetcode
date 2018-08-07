# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def generateTrees(self, n):
		"""
		给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
		---
		输入: 3
		输出:
		[
		  [1,null,3,2],
		  [3,2,null,1],
		  [3,1,null,null,2],
		  [2,1,3],
		  [1,null,2,null,3]
		]
		:type n: int
		:rtype: List[TreeNode]
		"""
