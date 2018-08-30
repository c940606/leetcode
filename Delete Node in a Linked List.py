# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def deleteNode(self, node):
		"""
		请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
		现有一个链表 -- head = [4,5,1,9]，它可以表示为:
		4 -> 5 -> 1 -> 9
		---
		输入: head = [4,5,1,9], node = 5
		输出: [4,1,9]
		解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
		---
		思路：
		加个 dummy
		前后指针
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""
		dummy = ListNode(0)
		dummy.next = head
		front = dummy
		last = head
		while last != node:
			front = front.next
			last = last.next
		front.next = last.next
