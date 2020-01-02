# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = 0
        p = head
        while p:
            res = res * 2 + p.val
            p = p.next
        return res