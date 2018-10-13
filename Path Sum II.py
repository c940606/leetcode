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
		if not root:
			return []
		res = []
		def helper(root,temp_sum,temp_list):
			print(temp_sum, temp_list)
			# if temp_sum > sum:
			# 	return
			if not root.right and not root.left and temp_sum+root.val == sum:
				res.append(temp_list+[root.val])
				return
			if root.left:
				helper(root.left,temp_sum+root.val,temp_list+[root.val])
			if root.right:
				helper(root.right,temp_sum+root.val,temp_list+[root.val])
		helper(root,0,[])
		return res

t = creatTree()
t_list = [-2,"#",-3]
tree = t.list_to_tree(t_list,TreeNode,0)
a = Solution()
print(a.pathSum(tree,-5))



# a = Solution()
# print(a.pathSum(tree,-5))


