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