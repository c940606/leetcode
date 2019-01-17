class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        from collections import deque
        if preorder == "#":
            return True
        preorder = preorder.split(",")
        if len(preorder) % 2 == 0 or (preorder[0] == "#" and len(preorder) > 0):
            return False
        stack = deque()
        for val in preorder:
            if val == "#":
                while stack and stack[-1] == "#":
                    stack.pop()
                    if not stack:
                        return False
                    stack.pop()
            stack.append(val)
        return len(stack) == 1 and stack[0] == "#"

    def isValidSerialization1(self, preorder):
        if preorder == "#":
            return True
        preorder = preorder.split(",")
        if len(preorder) % 2 == 0 or (preorder[0] == "#" and len(preorder) > 0):
            return False
        diff = 1
        for node in preorder:
            diff -= 1
            if diff < 0:
                return False
            if node != "#":
                diff += 2
        return diff == 0


a = Solution()
print(a.isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"))
# print(a.isValidSerialization1("1,#"))
# print(a.isValidSerialization1("9,#,#,1"))
