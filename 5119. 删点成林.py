class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        from collections import deque
        cur = [root]
        for to_node in to_delete:

            for i in range(len(cur)):
                tmp_root = cur[i]
                queue = deque()
                queue.appendleft(tmp_root)
                while queue:
                    tmp = queue.pop()
                    if tmp.val == to_node:
                        if tmp.left:
                            cur.append(tmp.left)
                        if tmp.right:
                            cur.append(tmp.right)
                        tmp = None
                        break
        return cur
