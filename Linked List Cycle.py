# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def hasCycle(self, head):
		"""
		给定一个链表，判断链表中是否有环。
		----
		思路:
		双指针

		:type head: ListNode
		:rtype: bool
		"""
		b = head
		d = head
		while d and d.next:
			b = b.next
			d = d.next.next
			if b ==d :
				return True
		return False