# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def reorderList(self, head):
		"""
		给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
		将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
		你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
		---
		给定链表 1->2->3->4, 重新排列为 1->4->2->3.
		---
		给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
		---
		思路:
		:type head: ListNode
		:rtype: void Do not return anything, modify head in-place instead.
		"""
		if not head:
			return
		p = head
		res = []
		while p:
			res.append(p)
			p = p.next
		n = len(res)
		i = 0
		j = n-1
		dummy = ListNode(0)
		cur = dummy
		while i<j:
			cur.next = res[i]
			cur = cur.next
			cur.next = res[j]
			cur = cur.next
			i += 1
			j -= 1
		if i == j:
			cur.next(res[i])
		head = dummy.next
		return dummy.next



