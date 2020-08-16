# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        list_head = []
        p = head
        while p:
            list_head.append(p.val)
            p = p, next
        n = len(list_head)
        self.res = False

        def dfs(root, i):
            if i == n:
                return True
            if root.val != list_head[i]:
                return False
            if dfs(root.left, i + 1) or dfs(root.right, i + 1):
                return True

            return False

        def helper(root):
            if not root:
                return
            if self.res: return
            if root.val == list_head[0]:
                if dfs(root, 0):
                    self.res = True
            helper(root.left)
            helper(root.right)

        helper(root)
        return self.res
