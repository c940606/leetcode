# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        dummy = TreeNode(-1)
        dummy.left = root

        def dfs(parent, cur):
            if not cur:
                return
            if cur.val == key:
                # 叶子节点
                if not cur.left and not cur.right:
                    if parent.left == cur:
                        parent.left = None
                    else:
                        parent.right = None
                # 左右节点有一个
                elif not (cur.left and cur.right):
                    child = None
                    if cur.left:
                        child = cur.left
                    else:
                        child = cur.right
                    if parent.left == cur:
                        parent.left = child
                    else:
                        parent.right = child

                # 左右都有节点
                else:
                    # 找右子树最小值
                    tmp_parent = cur
                    tmp = tmp_parent.right
                    while tmp and tmp.left:
                        tmp_parent = tmp
                        tmp = tmp.left
                    #
                    cur.val = tmp.val
                    if tmp_parent.left == tmp:
                        tmp_parent.left = tmp.right
                    else:
                        tmp_parent.right = tmp.right
                return
            dfs(cur, cur.left)
            dfs(cur, cur.right)

        dfs(dummy, root)
        return dummy.left
