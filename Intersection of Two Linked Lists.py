# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def getIntersectionNode(self, headA, headB):
		"""
		编写一个程序，找到两个单链表相交的起始节点。
		----
		例如，下面的两个链表：

		A:          a1 → a2
						   ↘
							 c1 → c2 → c3
						   ↗
		B:     b1 → b2 → b3
		在节点 c1 开始相交。
		---
		方法一:哈希表(超时)
		方法二:
		就是我们想找最短那一个天从头开始一起找
		:type head1, head1: ListNode
		:rtype: ListNode
		"""
		lookup = []
		while headA:
			lookup.append(headA)
			headA = headA.next
		while headB:
			if headB in lookup:
				return headB
			headB = headB.next
		return None

	def getIntersectionNode1(self, headA, headB):
		if not headA or not headB:
			return  None
		p1 = headA
		length1 = 0
		p2 = headB
		length2 = 0
		while p1:
			length1 += 1
			p1 = p1.next
		while p2:
			length2 += 1
			p2  = p2.next
		p1 = headA
		p2 = headB
		if length1 > length2:
			for i in range(length1-length2):
				p1 = p1.next
		else:
			for i in range(length2 - length1):
				p2 = p2.next
		while p1:
			if p1 is p2:
				return p1
			p1 = p1.next
			p2 = p2.next
		return None

