class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList1(self, head: 'Node') -> 'Node':
        dict = {}
        m = head
        n = head
        while m:
            dict[m] = m.random
            m = m.next
        while n:
            dict[n].next = n.next
            dict[n].random = dict[n]
            n = n.next
        return dict[head]

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return None
        # 复制节点
        cur = head
        while cur:
            # 保存下一个节点
            tmp = cur.next
            # 后面跟着同样的节点
            cur.next = Node(cur.val, None, None)
            # 拼接
            cur.next.next = tmp
            cur = tmp
        # 复制random指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        # 拆分
        cur = head
        copy_head = head.next
        copy_cur = copy_head
        while copy_cur.next:
            # 组head
            cur.next = cur.next.next
            cur = cur.next
            # 组 copy_head
            copy_cur.next = copy_cur.next.next
            copy_cur = copy_cur.next
        # 把链表结束置空
        cur.next = copy_cur.next
        copy_cur.next = None
        return copy_head
