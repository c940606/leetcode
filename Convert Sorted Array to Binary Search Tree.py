# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def sortedArrayToBST(self, nums):
		"""
		将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
		本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
		---
		思路:
		每次左右树个数一样就行
		:type nums: List[int]
		:rtype: TreeNode
		"""
		if not nums:
			return None
		n = len(nums)
		mid = n//2
		num = nums[mid]
		root = TreeNode(num)
		root.left = self.sortedArrayToBST(nums[:mid])
		root.right = self.sortedArrayToBST(nums[mid+1:])
		return root
nums = [-10,-3,0,5,9]
a = Solution()
print(a.sortedArrayToBST(nums))
