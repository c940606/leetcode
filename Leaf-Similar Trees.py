# Definition for a binary tree node.
from listcreatTree import  creatTree
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def leafSimilar(self, root1, root2):
		"""\
		举个例子，如上图所示，给定一颗叶值序列为 (6, 7, 4, 9, 8) 的树。
		如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
		如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。
		--
		思路：
		把两个叶子结点放入列表中
		比较
		:type root1: TreeNode
		:type root2: TreeNode
		:rtype: bool
		"""
		leaf1 = []
		leaf2 = []
		self.findLeaf(leaf1,root1)
		self.findLeaf(leaf2,root2)
		return leaf1 == leaf2
	def findLeaf(self,temp,root):
		if not root:
			return 
		if not root.right and not root.left:
			temp.append(root.val)
			return
		self.findLeaf(temp,root.left)
		self.findLeaf(temp,root.right)
treelist = [1,2,3,4,5]
t = creatTree()
tree = t.list_to_tree(treelist,TreeNode,0)
print(tree.val)
a = Solution()
print(a.leafSimilar(tree,tree))
