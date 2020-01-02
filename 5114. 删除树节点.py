from typing import List


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for idx, p in enumerate(parent):
            graph[p].append(idx)

        # print(graph)

        def cal_sum(root):
            cur = 0
            cur += value[root]

            for j in graph[root]:
                cur += cal_sum(j)
            value[root] = cur
            return cur

        cal_sum(0)

        def dfs(root):
            if value[root] == 0:
                return 0
            res = 1
            for j in graph[root]:
                res += dfs(j)

        return dfs(0)


a = Solution()
print(a.deleteTreeNodes(nodes=7, parent=[-1, 0, 0, 1, 2, 2, 2], value=[1, -2, 4, 0, -2, -1, -1]))
# print(a.deleteTreeNodes())
