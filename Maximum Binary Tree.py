# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def constructMaximumBinaryTree(self, nums):
		"""
		给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
		二叉树的根是数组中的最大元素。
		左子树是通过数组中最大值左边部分构造出的最大二叉树。
		右子树是通过数组中最大值右边部分构造出的最大二叉树。
		通过给定的数组构建最大二叉树，并且输出这个树的根节点。
		---

		:type nums: List[int]
		:rtype: TreeNode
		"""
		if not nums:
			return
		max_val = max(nums)
		max_index = nums.index(max_val)
		# print(max_index)
		root = TreeNode(max_val)
		# print(root)
		root.left = self.constructMaximumBinaryTree(nums[:max_index])
		root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
		return root

	# def creatTree(self, root, nums):
	# 	if not nums:
	# 		return
	# 	max_val = max(nums)
	# 	max_index = nums.index(max_val)
	# 	# print(max_index)
	# 	root = TreeNode(max_val)
	# 	self.creatTree(root.left,nums[:max_index])
	# 	self.creatTree(root.right, nums[max_index + 1:])
a = Solution()
print(a.constructMaximumBinaryTree([3,2,1,6,0,5]))

