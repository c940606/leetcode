# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    递归
    非递归
    '''

    def inorderTraversal4(self, root):
        """
        给定一个二叉树，返回它的中序 遍历
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        else:
            self.inorderTraversal(root.left)
            print(root.val)
            self.inorderTraversal(root.right)

    def inorderTraversal1(self, root):
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            if stack:
                temp = stack.pop()
                res.append(temp.val)
                root = temp.right
        return res

    def inorderTraversal2(self, root):
        res = []
        stack = []
        p = root
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                p = p.right
        return res

    def inorderTraversal(self, root):
        res = []
        stack = []
        # 用p当做指针
        p = root
        while p or stack:
            # 把左子树压入栈中
            while p:
                stack.append(p)
                p = p.left
            # 输出 栈顶元素
            tmp = stack.pop()
            res.append(tmp.val)
            # 看右子树
            p = tmp.right
        return res


a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.right = b
b.left = c
S = Solution()
# S.inorderTraversal(a)
print("----")
print(S.inorderTraversal2(a))
