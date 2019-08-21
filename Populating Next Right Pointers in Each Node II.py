# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect1(self, root):
        if not root:
            return
        cur = [root]
        while cur:
            temp = []
            for node in cur:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            n = len(temp)
            for i in range(n - 1):
                temp[i].next = temp[i + 1]
            cur = temp

    def connect(self, root):
        cur = root
        head = None
        tail = None
        while cur:
            while cur:
                if cur.left:
                    if not head:
                        head = cur.left
                        tail = cur.left
                    else:
                        tail.next = cur.left
                        tail = tail.next
                if cur.right:
                    if not head:
                        head = cur.right
                        tail = cur.right
                    else:
                        tail.next = cur.right
                        tail = tail.next
                cur = cur.next
            cur = head
            head = None
            tail = None
        return root
