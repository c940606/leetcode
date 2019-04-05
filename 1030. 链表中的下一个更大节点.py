# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head):
        stack = []
        n = len(head)
        res = [0] * n
        for idx in range(n):
            while stack and head[stack[-1]] < head[idx]:
                res[stack.pop()] = head[idx]
            stack.append(idx)
        return res



a = Solution()
print(a.nextLargerNodes([2, 1, 5]))
