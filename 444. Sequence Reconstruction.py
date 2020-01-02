from collections import defaultdict
from typing import List


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegree = defaultdict(int)
        # seqs = [seq for seq in seqs if seq]
        all_num = set(org)
        graph_num = set()
        for item in seqs:
            graph_num.update(item)
            if len(item) > 1:
                for i in range(1, len(item)):
                    if item[i] not in graph[item[i - 1]]:
                        graph[item[i - 1]].add(item[i])
                        indegree[item[i]] += 1
        if all_num - graph_num: return False
        i = 0
        while i < len(org):
            # or sum(1 for num in all_num if indegree[num] == 0) > 1
            if indegree[org[i]] != 0:
                return False
            all_num -= {org[i]}
            cnt = 0
            for tmp in graph[org[i]]:
                indegree[tmp] -= 1
                if indegree[tmp] == 0:
                    cnt += 1
            if cnt > 1: return False
            i += 1
        # print(all_num)
        return True


a = Solution()
print(a.sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3], [2, 3]]))
print(a.sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3]]))
print(a.sequenceReconstruction([1], [[], []]))
print(a.sequenceReconstruction([1, 2, 3], [[1, 2]]))
print(a.sequenceReconstruction([1], []))
print(a.sequenceReconstruction([1], [[1], [1], [1]]))
print(a.sequenceReconstruction([1, 2, 3, 4, 5], [[1, 2, 3, 4, 5]]))
