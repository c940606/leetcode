"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Codec1:

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root: return
        res = TreeNode(root.val)
        if root.children:
            res.left = self.encode(root.children[0])
        cur = res.left
        for node in root.children[1:]:
            cur.right = self.encode(node)
            cur = cur.right
        return res

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data: return
        res = Node(data.val, [])
        cur = data.left
        while cur:
            res.children.append(self.decode(cur))
            cur = cur.right
        return res


class Codec:

    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        from collections import deque
        if not root: return
        new_TreeNode = TreeNode(root.val)
        queue = deque([[new_TreeNode, root]])

        while queue:
            cur_TreeNode, cur_Node = queue.pop()
            if not cur_Node.children: continue
            # 先把第一个孩子放在树左边
            cur_TreeNode.left = TreeNode(cur_Node.children[0].val)
            # 入队列
            queue.appendleft([cur_TreeNode.left, cur_Node.children[0]])
            # 把右边挂兄弟
            cur_TreeNode = cur_TreeNode.left
            for node in cur_Node.children[1:]:
                new_node = TreeNode(node.val)
                cur_TreeNode.right = new_node
                cur_TreeNode = cur_TreeNode.right
                queue.appendleft([new_node, node])
        return new_TreeNode

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        from collections import deque
        if not data: return
        new_Node = Node(data.val, [])
        queue = deque([[new_Node, data]])
        while queue:
            cur_Node, cur_data = queue.pop()
            child = cur_data.left
            while child:
                new_node = Node(child.val, [])
                cur_Node.children.append(new_node)
                queue.appendleft([new_node, child])
                child = child.right
        return new_Node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
