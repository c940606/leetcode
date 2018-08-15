class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class creatTree:
	def list_to_tree(self,treelist,root,i):
		if i<len(treelist):
			if treelist[i] == "#":
				return None
			else:
				root = TreeNode(treelist[i])
				root.left = self.list_to_tree(treelist,root.left,i*2+1)
				root.right = self.list_to_tree(treelist,root.right,i*2+2)
				return root
		return root



