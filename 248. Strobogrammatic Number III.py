class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        from collections import deque

        def cmp(tmp):
            if tmp and int(low) <= int(tmp) <= int(high):
                return True
            return False

        queue = deque()
        queue.appendleft("")
        res = 0
        while queue:
            tmp = queue.pop()
            if cmp(tmp):
                res += 1
            if len(tmp) % 2 == 0:
                mid = len(tmp) // 2
                num1 = tmp[:mid + 1] + tmp[mid:mid + 1] + tmp[mid + 1:]

