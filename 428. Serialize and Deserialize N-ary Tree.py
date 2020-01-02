"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        res = []

        def helper(root):
            if not root: return
            res.append(str(root.val))
            res.append(str(len(root.children)))
            for ch in root.children:
                helper(ch)

        helper(root)
        return ",".join(res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data: return
        data = iter(data.split(","))

        def helper():
            tmp = int(next(data))
            num = int(next(data))
            root = Node(tmp, [])
            for _ in range(num):
                root.children.append(helper())
            return root

        return helper()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
from collections import deque


class Codec1:

    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        res = []
        if root:
            queue = deque([root])
            while queue:
                tmp = queue.pop()
                res.append(str(tmp.val))
                res.append(str(len(tmp.children)))
                for ch in tmp.children:
                    queue.appendleft(ch)
        return ",".join(res)

    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """
        if not data: return
        data = map(int, (data.split(",")))
        res = Node(next(data), [])
        queue = deque([res])
        queue_num = deque([next(data)])

        while queue:
            node = queue.pop()
            num = queue_num.pop()
            for _ in range(num):
                tmp = next(data)
                tmp_num = next(data)
                cur = Node(tmp, [])
                node.children.append(cur)
                queue.appendleft(cur)
                queue_num.appendleft(tmp_num)
        return res
