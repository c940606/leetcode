class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_node(node):
    res = []
    p = node
    while p:
        res.append(p.val)
        p = p.next
    return res
def helper(node):
    cur =node
    p = node
    q = p.next
    p.next = None
    while q:
        r = q.next
        q.next = p.next
        p.next = q
        q = r
    return cur

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
print(print_node(a))
print(print_node(helper(a)))
