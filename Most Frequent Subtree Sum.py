# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def findFrequentTreeSum(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root:
			return []
		if not root.left and not root.right:
			return [root.val]
		lookup = {}
		def sum_tree(root):
			if not root:
				return 0
			temp = root.val
			temp += sum_tree(root.left)
			temp += sum_tree(root.right)
			if temp in lookup:
				lookup[temp] += 1
			else:
				lookup[temp] = 1
			return temp
		sum_tree(root)
		max_num = max(lookup.values())
		return [x for x in lookup if lookup[x] == max_num]

