"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList1(self, root: 'Node') -> 'Node':
        if not root: return
        # 当一个中间节点
        head = Node(-1, None, None)
        # 记录为先前节点,找到下一个节点才能串起来
        prev = head
        # 中序遍历的非递归
        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            # 改变左右方向
            prev.right = p
            p.left = prev
            # 改变先前节点
            prev = p
            p = p.right
        # 将head 删掉
        head.right.left = prev
        prev.right = head.right
        return head.right

    def treeToDoublyList2(self, root: 'Node') -> 'Node':
        if not root: return
        # 当一个中间节点
        head = Node(-1, None, None)
        # 记录为先前节点,找到下一个节点才能串起来
        prev = head

        # 中序遍历的递归
        def inorder(root):
            nonlocal prev
            if not root:
                return
            inorder(root.left)
            prev.right = root
            root.left = prev
            prev = prev.right
            inorder(root.right)

        inorder(root)
        # 将head 删掉
        head.right.left = prev
        prev.right = head.right
        return head.right

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return
        left = self.treeToDoublyList(root.left)
        right = self.treeToDoublyList(root.right)
        root.left = root
        root.right = root
        return self.connect(self.connect(left, root), right)

    def connect(self, node1, node2):
        if not (node1 and node2):
            return node1 or node2
        tail1, tail2 = node1.left, node2.left
        tail1.right = node2
        node2.left = tail1
        tail2.right = node1
        node1.left = tail2
        return node1
