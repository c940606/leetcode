from listcreatTree import creatTree
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def hasPathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
		self.all_sum = []
		self.find_all_sum(root,0)

		return sum in self.all_sum

	def find_all_sum(self, root,temp):
		# print(root.val)
		if not root:
			return

		if  not root.right and not root.left:
			# print(root.val)
			self.all_sum.append(temp+root.val)
			# print(self.all_sum)
			return
		# elif (not root.right and  root.left) or (not root.left and root.right):
		# 	return
		else:
			print(root.val)
			self.find_all_sum(root.left,temp+root.val)
			# print("s",root.val)

			self.find_all_sum(root.right,temp+root.val)




treelist = [1,2,3,'#',4,5]
treelist1 = [5,4,8,11,"#",13,4,7,2]
tree_obj = creatTree()
tree = tree_obj.list_to_tree(treelist1,TreeNode,0)



a = Solution()
print(a.hasPathSum(tree,0))