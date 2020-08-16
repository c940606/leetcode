from typing import List
import collections

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        to = {}
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            to[(x, y)] = 1
            to[(y, x)] = -1
            
        visited = set([0])
        
        bfs = [0]
        res = 0
        while bfs:
            nxt = []
            for node in bfs:
                for tmp in graph[node]:
                    if tmp in visited: continue
                    if to[(tmp, node)] != 1:
                        res += 1
                    visited.add(tmp)
                    nxt.append(tmp)
            bfs = nxt
        return res
    
a = Solution()
print(a.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(a.minReorder(n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]))
print(a.minReorder(n = 3, connections = [[1,0],[2,0]]))