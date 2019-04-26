# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = []
        for l in lists:
            p = l
            while p:
                heapq.heappush(head, p.val)
                p = p.next
        dummy = ListNode(0)
        p = dummy
        while head:
            tmp = heapq.heappop(head)
            p.next = ListNode(tmp)
            p = p.next
        return dummy.next

    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:
        queue = []
        for idx, l in enumerate(lists):
            if l:
                heapq.heappush(queue, (l.val, idx))
                lists[idx] = l.next
        dummy = ListNode(0)
        p = dummy
        while queue:
            tmp, idx = heapq.heappop(queue)
            p.next = ListNode(tmp)
            p = p.next
            if lists[idx]:
                heapq.heappush(queue, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next
