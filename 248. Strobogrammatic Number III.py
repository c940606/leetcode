class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        from collections import deque
        queue = deque(["", "1", "0", "8"])
        res = 0
        lookup = []
        visited = set()
        while queue:
            tmp = queue.pop()
            if tmp != "" and int(low) <= int(tmp) <= int(high):
                if len(tmp) > 1 and tmp[0] == "0":
                    pass
                else:
                    lookup.append(tmp)
                    res += 1
            if len(tmp) + 2 <= len(high):
                for item in ["0" + tmp + "0", "1" + tmp + "1", "6" + tmp + "9", "8" + tmp + "8", "9" + tmp + "6"]:
                    if item not in visited:
                        visited.add(item)
                        queue.appendleft(item)
        return res


a = Solution()
# print(a.strobogrammaticInRange("100", "1000"))
# print(a.strobogrammaticInRange("0", "0"))
print(a.strobogrammaticInRange("0", "1680"))
print(a.strobogrammaticInRange("0", "100000000000000"))
