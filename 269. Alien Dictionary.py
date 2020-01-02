from collections import defaultdict
from collections import deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = defaultdict(int)
        all_alp = set()
        if len(words) < 1: return ""
        all_alp.update(words[0])
        for i in range(1, len(words)):
            all_alp.update(words[i])
            for x, y in zip(words[i - 1], words[i]):
                if x == y: continue
                else:
                    if y not in graph[x]:
                        graph[x].add(y)
                        indegree[y] += 1
                    break
        print(graph, indegree)
        res = ""
        queues = deque(alp for alp in all_alp if indegree[alp] == 0)
        while queues:
            tmp = queues.pop()
            res += tmp
            for t in graph[tmp]:
                indegree[t] -= 1
                if indegree[t] == 0:
                    queues.appendleft(t)
        print(res)
        return res if len(res) == len(all_alp) else ""

a = Solution()
# print(a.alienOrder([
#     "wrt",
#     "wrf",
#     "er",
#     "ett",
#     "rftt"
# ]))
# print(a.alienOrder(["z", "z", "z"]))
# print(a.alienOrder(["x", "y", "x"]))
# print(a.alienOrder(["zy","zx"]))
# print(a.alienOrder(["ab", "adc"]))
# print(a.alienOrder(["aac","aabb","aaba"]))
# print(a.alienOrder(["wrt","wrf","er","ett","rftt"]))
# print(a.alienOrder(["za","zb","ca","cb"]))
print(a.alienOrder(["wnlb"]))
