# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def oddEvenList(self, head):
		"""
		给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
		请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
		请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
		----
		输入: 1->2->3->4->5->NULL
		输出: 1->3->5->2->4->NULL
		--
		思路:
		用dummy法

		:type head: ListNode
		:rtype: ListNode
		"""
		dummy = ListNode(0)
		l = dummy
		p = 0
		if head:
			p = head
		# flag = 1
		while p:
			l.next = ListNode(p.val)
			l = l.next
			if p.next and p.next.next:
				p = p.next.next
			else:
				break
		q = 0
		if head and head.next:
			q = head.next
		while q:
			l.next = ListNode(q.val)
			l = l.next
			if q.next and q.next.next:
				q = q.next.next
			else:
				break
		return dummy.next

	# def oddEvenList1(self, head):
	# 	if not head:
	# 		return head
	# 	dummy = ListNode(0)
	# 	beg = dummy
	# 	odd = 0
	# 	even = 0
	# 	if head:
	# 		odd = head
	# 	if head and head.next:
	# 		even = head.next
	# 	while odd or even:
	# 		beg.next = ListNode(odd.val)
	# 		beg = beg.next
	# 		beg.next = ListNode(even.val)

