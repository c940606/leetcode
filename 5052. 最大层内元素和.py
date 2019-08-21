# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        from collections import deque
        res = 1
        depth = 1
        queue = deque()
        queue.appendleft(root)
        cur = float("-inf")
        while queue:
            n = len(queue)
            tmp_sum = 0
            for _ in range(n):
                tmp = queue.pop()
                tmp_sum += tmp.val
                if tmp.left:
                    queue.appendleft(tmp.left)
                if tmp.right:
                    queue.appendleft(tmp.right)
            if tmp_sum > cur:
                res = depth
                cur = tmp_sum
            depth += 1
        return res


