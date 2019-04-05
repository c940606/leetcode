# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        cur = [root]
        i = 1
        res = 0
        num = 2
        while any(cur):
            next_time = [None] * num
            for idx, val in enumerate(cur):
                if val == None:
                    continue
                if val.left:
                    next_time[2 * idx] = val.left
                if val.right:
                    next_time[2 * idx + 1] = val.right
            left = 0
            right = num - 1
            while next_time[left] == None:
                left += 1
            while next_time[right] == None:
                right -= 1
            res = max(res, right - left + 1)
            cur = next_time
            num *= 2
        return res

    def widthOfBinaryTree1(self, root):
        if not root:
            return 0

        cur = [root]
        lookup = {root: 0}
        res = 0
        while cur:
            next_time = []
            start = lookup[cur[0]]
            end = lookup[cur[-1]]
            for tmp in cur:
                if tmp.left:
                    next_time.append(tmp.left)
                    lookup[tmp.left] = lookup[tmp] * 2
                if tmp.right:
                    next_time.append(tmp.right)
                    lookup[tmp.right] = lookup[tmp] * 2 + 1
            res = max(res, end - start + 1)
            cur = next_time
        return res

    def widthOfBinaryTree2(self, root):
        self.res = 0

        def dfs(root, idx, level, start):
            if not root: return
            if len(start) == level:
                start.append(idx)
            else:
                self.res = max(self.res, idx - start[level] + 1)
            dfs(root.left, idx * 2, level + 1, start)
            dfs(root.right, idx + 2 + 1, level + 1, start)

        dfs(root, 0, 0, [])

        return self.res
