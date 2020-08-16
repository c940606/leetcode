# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq


class Solution:
    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)

        def merge(left, right):
            if left > right:
                return
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            l1 = merge(left, mid)
            l2 = merge(mid + 1, right)
            return mergeTwoLists(l1, l2)

        def mergeTwoLists(l1, l2):
            if not l1 or not l2:
                return l1 or l2
            if l1.val < l2.val:
                l1.next = mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = mergeTwoLists(l1, l2.next)
                return l2

        return merge(0, n - 1)
