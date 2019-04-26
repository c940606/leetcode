# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        data = []
        p = head
        while p:
            data.append(p.val)
            p = p.next
        dummy = ListNode(0)
        l = dummy
        n = len(data)
        for i in range(0, n, k):
            if i + k <= n:
                tmp = data[i:i + k][::-1]
            else:
                tmp = data[i:]
            for node in tmp:
                l.next = ListNode(node)
                l = l.next
        return dummy.next

    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        curr = head
        count = 0
        while cur and count != k:
            curr = curr.next
            count += 1
        if count == k:
            curr = self.reverseKGroup1(curr, k)
            while count:
                tmp = head.next
                head.next = curr
                curr = head
                head = tmp
                count -= 1
            head = curr
        return head
