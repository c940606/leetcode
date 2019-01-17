# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        if not root:
            return [[] for _ in range(k)]
        n = 0
        p = root
        res = [[] for _ in range(k)]
        while p:
            n += 1
            p = p.next
        shang, yu = divmod(n, k)
        i = 0
        beg = root
        end = None
        while i < k and beg:
            res[i] = beg
            tmp = shang
            if yu > 0:
                tmp += 1
            while beg and tmp:
                end = beg
                beg = beg.next
                tmp -= 1
            end.next = None
            i += 1
            yu -= 1
        return res