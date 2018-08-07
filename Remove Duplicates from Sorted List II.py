# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def deleteDuplicates(self, head):
		"""
		给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
		:type head: ListNode
		:rtype: ListNode
		"""
		dummy = ListNode(-1)
		dummy.next = head
		cur = head
		lookup = {}
		while cur:
			if cur.val in lookup:
				lookup[cur.val] += 1
			else:
				lookup[cur.val] = 0
			cur = cur.next
		cur = dummy
		while cur.next:
			if lookup[cur.next.val]>1:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return dummy.next

	def deleteDuplicates1(self, head):
		if head == None or head.next == None:
			return head
		dummy = ListNode(-1)
		dummy.next = head
		pre = dummy
		cur = dummy.next
		while cur:
			while cur.next and pre.next.val == cur.next.val:
				cur = cur.next
			if pre.next == cur:
				pre = cur
			else:
				pre.next = cur.next
			cur = cur.next
		return dummy.next





a = Solution()
obj = [1,2,3,3,4,4,5]
print(a.deleteDuplicates(obj))

