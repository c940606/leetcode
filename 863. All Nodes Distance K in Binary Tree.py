# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        res = []
        def helper(root,h):
            if root == target:
                return h
            if root.left:
                return helper(root.left,h+1)
            if root.right:
                return helper(root.right,h+1)
        target_height = helper(root,0)
        if target_height>=K:

        else:


        def helper1(node,K):
            if K == 0:
                res.append(node.val)
                return
            if node.left:
                helper1(node.left,K-1)
            if node.right:
                helper1(node.right,K-1)
        helper1(target,K)
        print(res)

    def distanceK1(self, root, target, K):
        from collections import defaultdict
        graph = defaultdict(list)
        def dfs(root):
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                dfs(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                dfs(root.right)
        dfs(root)
        cur = [target.val]
        vistied = {target.val}
        while K :
            next_time = []
            for a in cur:
                for b in graph[a]:
                    if b not in vistied:
                        next_time.append(b)
                        vistied.add(b)
            cur = next_time
            K -= 1
        return cur