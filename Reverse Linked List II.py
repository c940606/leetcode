class Solution:
	def reverseBetween(self, head, m, n):
		"""
		反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
		说明:
		1 ≤ m ≤ n ≤ 链表长度。
		---
		输入: 1->2->3->4->5->NULL, m = 2, n = 4
		输出: 1->4->3->2->5->NULL
		---
		:type head: ListNode
		:type m: int
		:type n: int
		:rtype: ListNode
		"""

		dummy = ListNode(-1)
		dummy.next = head
		p = dummy
		for _ in range(m-1):
			p = p.next
		tail = p.next
		pre = None
		cur = p.next
		for _ in range(n-m+2):
			temp = cur.next
			cur.next = pre
			pre = cur
			cur = temp
		p.next = pre
		tail.next = cur
		return dummy.next

	def reverseBetween1(self, head, m, n):
		dummy = ListNode(-1)
		dummy.next = head
		pre = dummy
		for _ in range(m-1):
			pre = pre.next
		node = None
		cur = pre.next
		for _ in range(n-m+1):
			temp = cur.next
			cur.next = node
			node = cur
			cur = temp
		pre.next.next= cur
		pre.next = node
		return dummy.next


