# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def deleteDuplicates(self, head):
		"""
		给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
		---
		输入: 1->1->2
		输出: 1->2
		:type head: ListNode
		:rtype: ListNode
		"""
		dummy = head
		while head:
			while head.next and head.next.val == head.val:
				head = head.next.next
			head = head.next
		return dummy


