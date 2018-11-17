# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def sortList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head:
			return head
		print("未排序:",self.print_list(head))
		dummy = ListNode(0)
		dummy.next = head
		pre_cur = dummy
		cur = head
		while cur:
			print(self.print_list(head))
			p = dummy
			q = head
			next_cur = cur.next
			while p != pre_cur:
				print("-.-",cur.val)
				if q.val > cur.val:
					pre_cur.next = next_cur
					p.next = cur
					cur.next = q
					q = cur
				p = p.next
				q = q.next
			pre_cur = cur
			cur = next_cur

		print("排序后:",self.print_list(dummy.next))
		return dummy.next

	def sortList1(self, head):
		"""
		分而治之
		:param head:
		:return:
		"""
		if head==None or head.next == None:
			return head
		mid = self.findMid(head)
		l1 = head
		l2 = mid.next
		mid.next = None
		# print("...")
		l1 = self.sortList1(l1)
		l2 = self.sortList1(l2)
		l3 = self.merger(l1,l2)
		print(self.print_list(l3))
		return l3
	def print_list(self,a_list):
		b = a_list
		res = []
		while b:
			res.append(b.val)
			b = b.next
		return res

	def findMid(self, head):
		if not head or not head.next:
			return head
		slow = head
		fast = head
		while fast.next  and  fast.next.next:
			slow = slow.next
			fast = fast.next.next
		return slow

	def merger(self,l1,l2):
		if l1 == None :
			return l2
		if l2 == None:
			return l1
		dummy = ListNode(-1)
		cur = dummy
		while l1 and l2:
			if l1.val < l2.val:
				cur.next = l1
				l1 = l1.next
			else:
				cur.next = l2
				l2 = l2.next
			cur = cur.next
		if l1:
			cur.next = l1
		if l2:
			cur.next = l2
		return dummy.next


node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
a= Solution()
print(a.sortList1(node1))