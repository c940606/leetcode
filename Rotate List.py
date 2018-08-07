# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def rotateRight(self, head, k):
		"""
		给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数
		输入: 1->2->3->4->5->NULL, k = 2
		输出: 4->5->1->2->3->NULL
		解释:
		向右旋转 1 步: 5->1->2->3->4->NULL
		向右旋转 2 步: 4->5->1->2->3->NULL
		:type head: ListNode
		:type k: int
		:rtype: ListNode
		"""
		if not head or not head.next:
			return head
		step = 1
		j = head
		while j.next:
			j = j.next
			step += 1
		while k%step:
			p,q = head,head.next
			while q.next:
				q = q.next
				p = p.next
			p.next = None
			q.next = head
			head = q
			k -= 1
		return head
