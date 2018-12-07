# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ""
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        num2 = ""
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        dummy = ListNode(0)
        p = dummy
        for num in str(int(num1) + int(num2)):
            # print(num)
            p.next = ListNode(int(num))
            p = p.next
        return dummy.next