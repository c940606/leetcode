class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        from  collections import deque
        queue = deque()
        queue.appendleft((r0,c0))
        visited = set()
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        visited.add((r0,c0))
        res = [[r0,c0]]
        while queue:
            i,j = queue.pop()
            for x, y in dirs:
                tmp_i = x + i
                tmp_j = y + j
                if 0<=tmp_i< R and 0<=tmp_j<C and (tmp_i,tmp_j) not in visited:
                    res.append([tmp_i,tmp_j])
                    queue.appendleft((tmp_i,tmp_j))
                    visited.add((tmp_i,tmp_j))
        return res

a = Solution()
print(a.allCellsDistOrder(R = 2, C = 2, r0 = 0, c0 = 1))
print(a.allCellsDistOrder(R = 2, C = 3, r0 = 1, c0 = 2))