# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = 0
        stack = []
        while i < len(S):
            height, val = 0, ""
            while i < len(S) and S[i] == "-":
                i += 1
                height += 1
            while i < len(S) and S[i] != "-":
                i += 1
                val += S[i]
            while len(stack) > height:
                stack.pop()
            node = TreeNode(int(val))
            if stack and stack[-1].left == None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
