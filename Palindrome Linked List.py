# Definition for singly-linked list.
class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	def isPalindrome(self, head):
		"""
		请判断一个链表是否为回文链表。
		----
		输入: 1->2
		输出: false
		---
		输入: 1->2->2->1
		输出: true
		----
		思路：
		找到中点
		:type head: ListNode
		:rtype: bool
		"""
		if not head:
			return False
		p = head
		res = []
		while p.next:
			res.append(p.val)
			p = p.next
		return res == res[::-1]

	def isPalindrome1(self, head):
		# 先找中点
		slow = head
		fast = head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		# 翻转后面的
		pre = None
		while slow:
			temp = slow.next
			slow.next = pre
			pre = slow
			slow = temp
		while pre:
			if pre.val != head.val:
				return False
			pre = pre.next
			head = head.next
		return True