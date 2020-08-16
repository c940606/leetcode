class Solution:
    def minDays(self, n: int) -> int:
        import heapq
        head = [n]
        step = 0
        visited = set()
        while head:
            # print(head)
            nxt = []
            for tmp in head:
                if tmp - 1 == 0:
                    return step + 1
                if tmp - 1 not in visited:
                    nxt.append(tmp - 1)
                    visited.add(tmp - 1)
                if tmp % 2 == 0 and tmp - tmp // 2 == 0:
                    return step  + 1
                if tmp % 2 == 0 and tmp - tmp // 2 not in visited:
                    nxt.append(tmp - tmp // 2)
                    visited.add(tmp - tmp // 2)
                if tmp % 3 == 0 and tmp - 2 * (tmp // 3) == 0:
                    return step - 1
                if tmp % 3 == 0 and tmp - 2 * (tmp//3) not in visited:
                    nxt.append(tmp - 2 * (tmp // 3))
                    visited.add(tmp - 2 * (tmp // 3))
            head = nxt
            step += 1

    
    
a = Solution()
print(a.minDays(9900))


