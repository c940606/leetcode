# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def removeElements(self, head, val):
		"""
		删除链表中等于给定值 val 的所有节点。
		---
		输入: 1->2->6->3->4->5->6, val = 6
		输出: 1->2->3->4->5
		:type head: ListNode
		:type val: int
		:rtype: ListNode
		"""
		dummy = ListNode(0)
		dummy.next = head
		front = dummy
		last = head
		while last:
			if last.val == val:
				front.next = last.next
				last = last.next
				continue
			front = front.next
			last = last.next
		return dummy.next
