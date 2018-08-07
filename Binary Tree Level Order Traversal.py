# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []

		res,cur_level = [],[root]
		while cur_level:
			temp = []
			next_level = []
			for i in cur_level:
				temp.append(i.val)

				if i.left:
					next_level.append(i.left)
				if i.right:
					next_level.append(i.right)
			res.append(temp)
			cur_level = next_level
		return res








def listCreatTree(root,ilist,i):
	if i < len(ilist):
		if ilist[i] == "#":
			return None
		else:
			root = TreeNode(ilist[i])
			# print(i,root.val)
			root.left= listCreatTree(root.left,ilist,2*i+1)
			root.right = listCreatTree(root.right,ilist,2*i+2)
			return root
	return root


# llist = ['1', '2', '3', '#', '4', '5']
llist = [3,9,20,"#","#",15,7]
llist1 = [1,2,3,4,5,6,8]
root = listCreatTree(TreeNode,llist,0)
print(root)
a = Solution()
print(a.levelOrder(root))