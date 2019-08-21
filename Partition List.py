# Definition for singly-linked list.
from List_to_ListNode import listToListNode, listNodeToString


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition1(self, head, x):
        """
        给定一个链表和一个特定值 x，对链表进行分隔，
        使得所有小于 x 的节点都在大于或等于 x 的节点之前。
        你应当保留两个分区中每个节点的初始相对位置。
        ---
        输入: head = 1->4->3->2->5->2, x = 3
        输出: 1->2->2->4->3->5
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        up_x = []
        dummy = ListNode(-1)
        beg = dummy
        while head:
            if head.val < x:
                beg.next = head
                beg = head
            else:
                up_x.append(head)
            head = head.next
        if not up_x:
            up_x[-1].next = None
            for item in up_x:
                beg.next = item
                beg = item
        return dummy.next

    def partition(self, head, x):
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        # print(listNodeToString(dummy1.next))
        # print(listNodeToString(dummy2.next))
        p1.next = dummy2.next
        p2.next = None
        return dummy1.next


a = Solution()
test = listToListNode([1, 4, 3, 2, 5, 2])
print(listNodeToString(a.partition(test, 3)))
