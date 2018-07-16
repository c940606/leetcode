# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
	def removeNthFromEnd(self, head, n):
		"""
		给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
		---------------------------------------------
		给定一个链表: 1->2->3->4->5, 和 n = 2.
		当删除了倒数第二个节点后，链表变为 1->2->3->5.
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		new_node = ListNode(0)
		new_node.next = head
		p = new_node
		q = new_node
		for i in range(n):
			p = p.next
		while p.next:
			p = p.next
			q = q.next
		q.next = q.next.next
		return new_node.next

