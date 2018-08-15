# Definition for a binary tree node.
from listcreatTree import creatTree


class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def pathSum(self, root, sum):
		"""
		:type root: TreeNode
		:type sum: int
		:rtype: List[List[int]]
		"""
		self.sum_route = []
		self.findSum(root,sum,[],0)
		return self.sum_route

	def findSum(self, root, sum, temp_list,temp_num):
		# print(root.val)
		if   not root:
			return
		if  not root.right and not root.left and sum == temp_num+root.val:
			# print(root.val)
			self.sum_route.append(temp_list+[root.val])
			# print(self.all_sum)
			return

		else:
			self.findSum(root.left,sum,temp_list+[root.val],temp_num+root.val)
			self.findSum(root.right,sum, temp_list + [root.val], temp_num + root.val)

treelist = [1,2,3,'#',4,5]
treelist1 = [5,4,8,11,"#",13,4,7,2]
treelist2 = [-2,"#",-3]
tree_obj = creatTree()
tree = tree_obj.list_to_tree(treelist2,TreeNode,0)



a = Solution()
print(a.pathSum(tree,-5))


