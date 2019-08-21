# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees2(self, n):
        """
        给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。
        ---
        输入: 3
        输出:
        [
          [1,null,3,2],
          [3,2,null,1],
          [3,1,null,null,2],
          [2,1,3],
          [1,null,2,null,3]
        ]
        :type n: int
        :rtype: List[TreeNode]
        """

        def helper(start, end):
            res = []
            if start > end:
                res.append(None)
                return res
            if start == end:
                res.append(TreeNode(start))
                return res
            for i in range(start, end + 1):
                left = helper(start, i - 1)
                right = helper(i + 1, end)
                for lnode in left:
                    for rnode in right:
                        root = TreeNode(i)
                        root.left = lnode
                        root.right = rnode
                        res.append(root)
            return res

        return helper(1, n)

    def generateTrees1(self, n):
        from collections import defaultdict
        lookup = defaultdict(list)

        def helper(start, end):
            if start > end:
                return [None]
            if (start, end) in lookup:
                return lookup[(start, end)]
            for val in range(start, end + 1):
                for left in helper(start, val - 1):
                    for right in helper(val + 1, end):
                        root = TreeNode(val)
                        root.left, root.right = left, right
                        lookup[(start, end)].append(root)
            return lookup[(start, end)]

        return helper(1, n)

    def generateTrees(self, n: int) -> List[TreeNode]:

        def helper(start, end):
            res = []
            if start > end:
                res.append(None)
            for val in range(start, end + 1):
                for left in helper(start, val - 1):
                    for right in helper(val + 1, end):
                        root = TreeNode(val)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res

        return helper(1, n)
