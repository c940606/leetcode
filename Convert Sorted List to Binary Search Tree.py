# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def sortedListToBST(self, head):
		"""
		给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
		本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
		--
		把链表转化成列表
		:type head: ListNode
		:rtype: TreeNode
		"""
		Linklist = self.linktolist(head)
		return self.jup(Linklist)



	def linktolist(self,head):
		Linklist = []
		p = head
		while p:
			Linklist.append(p.val)
			p = p.next
		return Linklist

	def jup(self, Linklist):
		if not Linklist:
			return None
		n = len(Linklist)
		mid = n//2
		root = TreeNode(Linklist[mid])
		root.left= self.jup(Linklist[:mid])
		root.right=self.jup(Linklist[mid+1:])
		return root

