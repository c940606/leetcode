# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: strt
        """

        def height(root):
            if not root: return 0
            return max(height(root.left), height(root.right)) + 1

        res = ["#"] * (2 ** height(root) - 1)

        def helper(root, loc):
            if loc >= len(res): return
            if not root: return
            res[loc] = str(root.val)
            helper(root.left, 2 * loc + 1)
            helper(root.right, 2 * loc + 2)

        helper(root, 0)
        # print(res)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return
        data = data.split(",")

        # print(data)
        # if not data: return
        def helper(loc):
            if loc >= len(data) or data[loc] == "#": return
            node = TreeNode(int(data[loc]))
            node.left = helper(2 * loc + 1)
            node.right = helper(2 * loc + 2)
            return node

        return helper(0)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
class Codec1:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preorder(root):
            if not root:
                res.append("#")
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        d = iter(data.split(","))

        def helper():
            tmp = next(d)
            # print(tmp)
            if tmp == "#": return
            node = TreeNode(int(tmp))
            node.left = helper()
            node.right = helper()
            return node

        return helper()


class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        res = []
        queue = deque()
        if root: queue.appendleft(root)
        while queue:
            tmp = queue.pop()
            if tmp:
                res.append(tmp.val)
                queue.appendleft(tmp.left)
                queue.appendleft(tmp.right)
            else:
                res.append("#")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = iter(data.split(","))
        root = TreeNode(next(data))
        queue = deque([root])
        while queue:
            tmp = queue.pop()
            left_val = next(data)
            if left_val != "#":
                tmp.left = TreeNode(int(left_val))
                queue.appendleft(tmp.left)
            right_val = next(data)
            if right_val != "#":
                tmp.right = TreeNode(int(right_val))
                queue.appendleft(tmp.right)
        return root

