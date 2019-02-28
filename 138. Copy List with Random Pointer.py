"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dict = {}
        m = head
        n = head
        while m :
            dict[m] = m.random
            m = m.next
        while n :
            dict[n] .next = n.next
            dict[n].random = dict[n]
            n = n.next
        return dict[head]
