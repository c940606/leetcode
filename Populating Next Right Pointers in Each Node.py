# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
	# @param root, a tree link node
	# @return nothing
	def connect(self, root):
		if not root:
			return
		cur = [root]
		while cur:
			temp = []
			for node in cur:
				if node.left:
					temp.append(node.left)
				if node.right:
					temp.append(node.right)
			n = len(temp)
			for i in range(n-1):
				temp[i].next = temp[i+1]
			cur = temp

	def connect1(self, root):
		if root:
			if root.left:
				root.left.next = root.right
			if root.right and root.next:
				root.right.next = root.next.left
			self.connect1(root.left)
			self.connect1(root.right)
