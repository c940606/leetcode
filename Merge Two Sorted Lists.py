# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def mergeTwoLists(self, l1, l2):
		"""
		将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
		--------------
		输入：1->2->4, 1->3->4
		输出：1->1->2->3->4->4
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		head = ListNode(0)
		p = head

		while l1 and  l2 :
			if l1.val < l2.val:
				p.next = l1
				l1 = l1.next
			else:
				p.next = l2
				l2 = l2.next
			p = p.next
		if l1 ==  None:
			p.next = l2
		if l2 == None:
			p.next = l1

		return head.next