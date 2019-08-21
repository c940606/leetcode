class Solution:
    def sortList(self, head: ListNode) -> ListNode:

        if not head and not head.next: return head
        slow = head
        fast = head
        # 用快慢指针分成两部分
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 找到左右部分, 要把左部分最后置空,这样就分成两部分了
        right_part = slow.next
        slow.next = None
        left_part = head
        # 递归下去
        left = self.sortList(left_part)
        right = self.sortList(right_part)
        # 合并
        return self.merge(left, right)

    def merge(self, left, right):
        dummy = ListNode(0)
        p = dummy
        l = left
        r = right
        # 和排队一样
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
                p = p.next
            else:
                p.next = r
                r = r.next
                p = p.next
        if l:
            p.next = l
        if r:
            p.next = r
        return dummy.next

