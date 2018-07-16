# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def swapPairs(self, head):
		"""
		给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
		----
		给定 1->2->3->4, 你应该返回 2->1->4->3.
		:type head: ListNode
		:rtype: ListNode
		"""
		if head == None or head.next == None:
			return head
		dummy = ListNode(-1)
		dummy.next = head
		cur = dummy
		while cur.next and cur.next.next:
			cur_one,cur_two,cur_three = cur.next,cur.next.next,cur.next.next.next
			cur.next = cur_two
			cur_two.next = cur_one
			cur_one.next = cur_three
			cur = cur_one
		return dummy.next