import functools


class Solution:
    @functools.lru_cache(None)
    def removeBoxes(self, boxes):
        if not boxes:
            return 0
        res = float("-inf")
        for i in range(len(boxes)):
            if i > 0 and boxes[i - 1] == boxes[i]:
                continue
            j = i
            while j < len(boxes) and boxes[j] == boxes[i]:
                j += 1
            res = max(res, (j - i) ** 2 + self.removeBoxes(boxes[:i] + boxes[j:]))
        return res


a = Solution()
print(a.removeBoxes((2, 1, 1, 2, 2)))
print(a.removeBoxes((1, 3, 2, 2, 2, 3, 4, 3, 1)))
print(a.removeBoxes((1, 2, 3, 4, 5, 6, 7, 8, 9)))
print(a.removeBoxes())
