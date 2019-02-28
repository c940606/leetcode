# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        1. 找中间值,用快慢指针
           1->2->3->4->5
                ↑
        2. 翻转中间值后面的链表
            1->2->3->5->4
        3. 然后一个一个拼接
            1->5->2->4->3
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        # 找中间值
        low = head
        fast = head
        while fast.next and fast.next.next:
            low = low.next
            fast = fast.next.next
        # 翻转中间值后面的
        preMid = low
        cur = low.next
        node = None
        while cur:
            tmp = cur.next
            cur.next = node
            node = cur
            cur = tmp
        preMid.next = node
        # 一个一个拼接
        p1 = head
        p2 = preMid.next
        while p1 != preMid:
            preMid.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = preMid.next
