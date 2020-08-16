# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l3 = ListNode(0)
        while True:
            if not l1:
                num = l2.val
            elif not l2:
                num = l1.val
            else:
                num = l1.val + l2.val
            l3.val, dig = (num + l3.val) % 10, (num + l3.val) // 10
            if (not l1 or not l1.next) and (not l2 or not l2.next):
                if dig > 0:
                    l3.next = ListNode(dig)
                return head
            l3.next = ListNode(dig)
            l3 = l3.next
            if l1 and l1.next:
                l1 = l1.next
            else:
                l1 = 0
            if l2 and l2.next:
                l2 = l2.next
            else:
                l2 = 0

    def addTwoNumbers(self, l1, l2):
        carry = 0

        def get_len(l):
            length = 0
            while l:
                length += 1
                l = l.next
            return length

        def add(l1, l2, offset):
            nonlocal carry
            if not l1: return
            if offset == 0:
                nxt = add(l1.next, l2.next, offset)
                carry, mod = divmod(l1.val + l2.val + carry, 10)
            else:
                nxt = add(l1.next, l2, offset - 1)
                carry, mod = divmod(carry + l1.val, 10)
            res = ListNode(mod)
            res.next = nxt
            return res

        l1_len = get_len(l1)
        l2_len = get_len(l2)
        if l1_len > l2_len:
            res = add(l1, l2, l1_len - l2_len)
        else:
            res = add(l2, l1, l2_len - l1_len)
        if carry:
            head = ListNode(1)
            head.next = res
            return head
        return res
