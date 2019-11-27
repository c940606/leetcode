class Solution:
    def removeZeroSumSublists1(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        stack = []
        p = head
        while p:
            if not stack:continue
            if stack[-1].val + p.val == 0:
                stack.pop()
                stack[-1].next = p.next
            else:
                stack.append(p)
            p = p.next
        return dummy.next

    def removeZeroSumSublists(self, head: ListNode) -> ListNode:


        dummy = ListNode(-1000)
        lookup = {0:dummy}
        dummy.next =head
        p = head
        cur = 0
        while p:
            cur += p.val
            if -cur in lookup:
                lookup[-cur].next = p.next
            lookup[cur] = p
            p = p.next
        return dummy.next
# [1,2,3,-3,4]
# [1,2,3,-3,-2]
# [1, -1]
# [0]
