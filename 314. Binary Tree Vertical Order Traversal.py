from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict, deque
        if not root: return []
        queue = deque([(0, root)])
        lookup = defaultdict(list)
        while queue:
            idx, node = queue.pop()
            lookup[idx].append(node.val)
            if node.left:
                queue.appendleft((idx - 1, node.left))
            if node.right:
                queue.appendleft((idx + 1, node.right))

        return [val for idx, val, in sorted(lookup.items(), key=lambda x: x[0])]

    def verticalOrder1(self, root: TreeNode) -> List[List[int]]:
        from collections import defaultdict
        if not root: return []

        lookup = defaultdict(list)

        def dfs(root, loc, depth):
            if not root:
                return
            lookup[loc].append([depth, root.val])
            dfs(root.left, loc - 1, depth + 1)
            dfs(root.right, loc + 1, depth + 1)

        dfs(root, 0, 0)
        return [[b for a, b in sorted(v, key=lambda x: x[0])] for k, v in sorted(lookup.items())]
