# Definition for a binary tree node.
from listcreatTree import creatTree
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def binaryTreePaths(self, root):
		"""
		给定一个二叉树，返回所有从根节点到叶子节点的路径。
		:type root: TreeNode
		:rtype: List[str]
		"""
		res = []
		def helper(root,temp):
			if not root:
				return
			if not root.right and not root.left:
				res.append(temp+[str(root.val)])
			# res.append(root.val)
			helper(root.left,temp+[str(root.val)])
			helper(root.right,temp+[str(root.val)])
		helper(root,[])
		print(res)
		return list(map(lambda x:"->".join(x),res))
t = creatTree()
t_list = [1,2,3,"#",5]
tree = t.list_to_tree(t_list,TreeNode,0)
a = Solution()
print(a.binaryTreePaths(tree))


