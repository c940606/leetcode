# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class creatTree:
	def list_to_tree(self,root,tree_list,i):
		if i < len(tree_list):
			if tree_list[i] == "#":
				return None
			else:
				root = TreeNode(tree_list[i])
				root.left = self.list_to_tree(root.left,tree_list,i*2+1)
				root.right = self.list_to_tree(root.right,tree_list,i*2+2)
				return root
		return root
class Solution:
	def maxDepth(self, root):
		"""
		给定一个二叉树，找出其最大深度。
		二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
		说明: 叶子节点是指没有子节点的节点。
		----
		思路:
		递归:
		终止条件:左右树都没有空
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		return self.depth(root,1)

	def depth(self, root,dep):
		if not root:
			return dep
		if not root.right and not root.left:
			return dep
		print(dep)
		return max(self.depth(root.left,dep+1),self.depth(root.right,dep+1))

	def maxDepth1(self, root):
		if not root:
			return 0
		return max(self.maxDepth1(root.left),self.maxDepth1(root.right))+1
a = Solution()
list_tree = [5,1,4,"#","#",3,6,7,8,9,10,1,2,4,2,5]
list_tree1 = [3,9]
creatTree = creatTree()
tree = creatTree.list_to_tree(TreeNode,list_tree,0)
print(a.maxDepth1(tree))


