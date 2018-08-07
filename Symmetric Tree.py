# Definition for a binary tree node.
import pydotplus
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def isSymmetric(self, root):
		"""
		给定一个二叉树，检查它是否是镜像对称的。
		例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return False
		return self.symmeTric(root.left,root.right)

	def symmeTric(self, left, right):
		if not left and not right:
			return True

		elif left and right and left.val == right.val:
			return self.symmeTric(left.left,right.right) and self.symmeTric(left.right,right.left)
		else:
			return False


Node1 = TreeNode(1)
Node2 = TreeNode(2)
Node3 = TreeNode(2)
Node4 = TreeNode(3)
Node5 = TreeNode(4)
Node6 = TreeNode(4)
Node7 = TreeNode(3)
Node1.left = Node2
Node1.right = Node3
Node2.left = Node4
Node2.right = Node5
Node3.left = Node6
Node3.right = Node7
a = Solution
print(a.isSymmetric(Node1))



