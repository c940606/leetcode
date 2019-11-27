import functools


class Solution:
    @functools.lru_cache(None)
    def removeBoxes1(self, boxes):
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

    def removeBoxes(self, boxes):
        @functools.lru_cache(None)
        def helper(left, right, k):
            if left > right:
                return 0
            if left == right:
                return (k + 1) * (k + 1)
            while left < right and boxes[left + 1] == boxes[left]:
                k += 1
                left += 1
            res = (k + 1) * (k + 1) + helper(left + 1, right, 0)
            for m in range(left + 1, right + 1):
                if boxes[m] == boxes[left]:
                    res = max(res, helper(left + 1, m - 1, 0) + helper(m, right, k + 1))
            return res

        return helper(0, len(boxes) - 1, 0)


a = Solution()
print(a.removeBoxes((2, 1, 1, 2, 2)))
print(a.removeBoxes((1, 3, 2, 2, 2, 3, 4, 3, 1)))
print(a.removeBoxes((1, 2, 3, 4, 5, 6, 7, 8, 9)))
# print(a.removeBoxes())
